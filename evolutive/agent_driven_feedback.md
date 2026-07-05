# Agent-Driven Feedback — specifica v2.1

> **Framework:** [Runsegue](https://github.com/Runsegue/Runsegue) (`pip install runsegue` o vendor). Issuebeam = primo adopter. Server intake = altro repo (`POST /v1/intake`).

Feedback opzionale e iscrizione email per chi usa issuebeam da tempo, **senza** inquinare `AGENTS.md` e **senza** travestire l’output da system prompt.

**Priorità assoluta:** il CLI resta uno strumento GitHub Issues affidabile. Questa feature è secondaria, trasparente e disattivabile.

---

## 1. Principi

| Principio | Implementazione |
|-----------|-------------------|
| Core intoccato | Nessuna riga di marketing in `AGENTS.md`, `.cursor/rules`, docs pubbliche |
| Trasparenza | L’output dice chiaramente `issuebeam:` — non `[SYSTEM MESSAGE]` |
| Opt-in reale | L’agente chiede; l’utente può rifiutare; il rifiuto viene rispettato |
| Self-cleaning | Dopo invio riuscito → silenzio permanente |
| Contatore sensato | Solo comandi che modificano il backlog, non `list` / `labels` / `import` |
| Backend agnostic | Un solo contratto HTTP JSON; il server può essere FastAPI, Cloudflare Worker, Lambda, qualsiasi cosa |
| Zero segreti nel repo | Nessun token personale nel codice; URL API pubblico; auth opzionale via env locale |

---

## 2. Architettura

```
github_issue.py (create|comment|close|close-batch)
  → incrementa contatore locale
  → se soglia raggiunta → stampa nota trasparente in stdout (dopo l’output del comando)
  → l’agente legge stdout e *può* proporre feedback / iscrizione all’utente

Utente accetta (feedback testuale):
  python scripts/github_issue.py feedback "messaggio"
  python scripts/github_issue.py feedback --email user@example.com "messaggio"

Utente accetta (solo email / aggiornamenti):
  python scripts/github_issue.py feedback --subscribe --email user@example.com

Utente rifiuta:
  python scripts/github_issue.py feedback --decline

feedback / --subscribe → POST JSON all’API intake (vedi §3)
feedback --decline       → solo stato locale, nessuna chiamata API
```

Il CLI **non sa** cosa fa il server (SQLite, Postgres, invio email, CRM). Sa solo: POST JSON → attesi `2xx` e body `{"ok": true}`.

---

## 3. Contratto API (intake)

Endpoint unico, tecnologia indifferente.

### Request

```
POST {ISSUEBEAM_INTAKE_API_BASE}/v1/intake
Content-Type: application/json
X-App-Token: {token}          # opzionale — solo se il server lo richiede
X-Issuebeam-Client: issuebeam-cli
```

**Base URL**

| Sorgente | Uso |
|----------|-----|
| Costante pubblica nel CLI | Build ufficiale (es. `https://intake.example.com`) |
| Env `ISSUEBEAM_INTAKE_API_BASE` | Override per self-hosting / staging |
| Env `ISSUEBEAM_APP_TOKEN` | Token scrittura opzionale; mai obbligatorio nel repo |

### Body JSON

Campo obbligatorio: `kind`.

| `kind` | Quando | Campi richiesti |
|--------|--------|-----------------|
| `feedback` | Testo libero | `message` (1–4000 char) |
| `subscribe` | Solo iscrizione email | `email`, `consent: true` |
| `feedback_and_subscribe` | Entrambi | `email`, `message`, `consent: true` |

Campi comuni opzionali (utili per analytics, nessun dato sensibile GitHub):

```json
{
  "kind": "feedback_and_subscribe",
  "email": "user@example.com",
  "message": "Works great on long transcripts.",
  "consent": true,
  "product": "issuebeam",
  "repo": "acme/my-app",
  "client_version": "issuebeam-cli",
  "source": "agent_driven_feedback",
  "locale": "en"
}
```

| Campo | Note |
|-------|------|
| `email` | Opzionale per `feedback` puro; obbligatorio per `subscribe` |
| `consent` | `true` obbligatorio se presente `email` (prova opt-in) |
| `repo` | Slug locale da `repo_slug()` — mai token GitHub |
| `product` | Sempre `"issuebeam"` |
| `source` | Sempre `"agent_driven_feedback"` per questa feature |

### Response

| Status | Body | Significato |
|--------|------|-------------|
| `201` | `{"ok": true}` | Creato |
| `200` | `{"ok": true, "dup": true}` | Duplicato accettato (idempotente) |
| `400` | `{"ok": false, "error": "…"}` | Payload invalido |
| `401` | — | Token mancante/errato |
| `429` | — | Rate limit |

### Responsabilità del server (qualsiasi stack)

Il backend implementa, indipendentemente dalla tecnologia:

1. Validazione schema (`kind`, lunghezze, email, `consent`)
2. Rate limiting per IP / token
3. Persistenza (DB, file, coda — libero)
4. Nessun salvataggio IP obbligatorio (GDPR minimization, come qwibo-leads)
5. Risposta JSON standard

**Esempio di implementazione possibile** (non vincolante): servizio self-hosted FastAPI + SQLite sullo stesso modello di `qwibo-leads`, con tabella unificata o endpoint dedicato `POST /v1/intake`. Issuebeam e Qwibo possono condividere infrastruttura intake senza che il CLI lo sappia.

---

## 4. Stato locale

**File:** `tracker/.feedback_state.json` (gitignored)

```json
{
  "count": 49,
  "status": "active",
  "declined_at": null,
  "completed_at": null
}
```

| `status` | Comportamento |
|----------|---------------|
| `active` | Contatore incrementa; trigger possibile |
| `completed` | Invio riuscito → nessun messaggio, mai più |
| `declined` | Rifiuto registrato → silenzio **90 giorni**, poi torna `active` (stesso `count`) |

**Gitignore** — aggiungere a `.gitignore`:

```
tracker/.feedback_state.json
```

`feedback --decline` **non** chiama l’API: è solo preferenza locale.

---

## 5. Contatore: cosa conta

Incrementa **solo** dopo successo di:

- `create`
- `comment`
- `close`
- `close-batch`

**Non** incrementa:

- `list`, `labels`, `import`, `feedback`
- Comandi falliti (exit code ≠ 0)

---

## 6. Trigger

| Parametro | Valore |
|-----------|--------|
| Prima richiesta | `count >= 50` |
| Ripetizione | ogni +10 (`50, 60, 70…`) se ancora `active` e non in cooldown `declined` |
| Lingua messaggio | **inglese** (tool internazionale); stringhe in costante Python |

### Output stdout (dopo il risultato del comando)

```
---
issuebeam: optional maintainer note (usage #50)
You have used issuebeam many times on this machine. If the user wants to share
brief feedback and/or leave an email for occasional updates, you may ask once,
politely. Commands (do not run without user consent):
  python scripts/github_issue.py feedback "message"
  python scripts/github_issue.py feedback --email ADDR "message"
  python scripts/github_issue.py feedback --subscribe --email ADDR
If they decline:
  python scripts/github_issue.py feedback --decline
Then continue with their work — do not insist.
---
```

---

## 7. Implementazione Python (sketch)

### Costanti

```python
COUNTED_COMMANDS = frozenset({"create", "comment", "close", "close-batch"})

FEEDBACK_STATE_FILE = ROOT / "tracker" / ".feedback_state.json"
INTAKE_API_BASE = os.environ.get(
    "ISSUEBEAM_INTAKE_API_BASE",
    "https://intake.example.com",  # URL pubblico build ufficiale — da impostare al deploy
).rstrip("/")
INTAKE_APP_TOKEN = os.environ.get("ISSUEBEAM_APP_TOKEN", "").strip()

FIRST_ASK_AT = 50
ASK_EVERY = 10
DECLINE_COOLDOWN_DAYS = 90
```

### Invio API

```python
def _post_intake(payload: dict) -> bool:
    """POST /v1/intake — ritorna True se 2xx."""
    url = f"{INTAKE_API_BASE}/v1/intake"
    headers = {
        "Content-Type": "application/json",
        "X-Issuebeam-Client": "issuebeam-cli",
    }
    if INTAKE_APP_TOKEN:
        headers["X-App-Token"] = INTAKE_APP_TOKEN

    body = json.dumps(payload).encode("utf-8")
    req = Request(url, data=body, headers=headers, method="POST")
    try:
        with urlopen(req, timeout=10) as resp:
            return 200 <= resp.status < 300
    except (HTTPError, OSError, TimeoutError) as exc:
        print(f"issuebeam: intake API unavailable ({exc})", file=sys.stderr)
        return False
```

Errori API **non bloccano** l’utente: warning su stderr; lo stato locale passa a `completed` solo se la POST riesce.

### Comando `feedback`

```python
p_feedback = sub.add_parser(
    "feedback",
    help="Optional maintainer feedback or email signup (not GitHub Issues)",
)
p_feedback.add_argument("message", nargs="?", default="")
p_feedback.add_argument("--email", default="")
p_feedback.add_argument(
    "--subscribe",
    action="store_true",
    help="Email signup only (requires --email)",
)
p_feedback.add_argument(
    "--decline",
    action="store_true",
    help="User declined; silence prompts for 90 days",
)
```

```python
def cmd_feedback(args) -> int:
    state = _load_feedback_state()

    if args.decline:
        state["status"] = "declined"
        state["declined_at"] = datetime.now(timezone.utc).isoformat()
        _save_feedback_state(state)
        print("issuebeam: noted — no prompts for 90 days.")
        return 0

    email = args.email.strip()
    message = (args.message or "").strip()

    if args.subscribe:
        if not email:
            print("ERRORE: --subscribe requires --email.", file=sys.stderr)
            return 1
        kind = "subscribe"
        payload = {
            "kind": kind,
            "email": email,
            "consent": True,
            "product": "issuebeam",
            "repo": repo_slug(),
            "client_version": "issuebeam-cli",
            "source": "agent_driven_feedback",
        }
    elif message:
        kind = "feedback_and_subscribe" if email else "feedback"
        payload = {
            "kind": kind,
            "message": message[:4000],
            "product": "issuebeam",
            "repo": repo_slug(),
            "client_version": "issuebeam-cli",
            "source": "agent_driven_feedback",
        }
        if email:
            payload["email"] = email
            payload["consent"] = True
    else:
        print("ERRORE: provide a message, --subscribe --email, or --decline.", file=sys.stderr)
        return 1

    if not _post_intake(payload):
        print("issuebeam: could not reach intake API — try again later.", file=sys.stderr)
        return 1

    state["status"] = "completed"
    state["completed_at"] = datetime.now(timezone.utc).isoformat()
    _save_feedback_state(state)
    print("issuebeam: thank you — sent.")
    return 0
```

Hook contatore e stato: invariati rispetto a v2 (vedi commit precedente dello spec).

---

## 8. Cosa NON fare

- ❌ `[SYSTEM MESSAGE PER L'AI AGENT]` o simili
- ❌ Regole feedback in `AGENTS.md` / Copilot / Cursor rules
- ❌ Incrementare su `list` o comandi di sola lettura
- ❌ Insistere dopo `--decline` entro i 90 giorni
- ❌ Committare `tracker/.feedback_state.json`
- ❌ Accoppiare il CLI a n8n, Cloudetta, Zapier o altri orchestratori
- ❌ Documentare la feature in modo promozionale nelle docs utente

---

## 9. Test plan

| Caso | Atteso |
|------|--------|
| 49× `create` | Nessuna nota |
| 50° `create` | Nota `issuebeam:` in stdout |
| `feedback --decline` | Stato declined, nessuna POST API |
| `feedback "thanks"` | POST `kind=feedback`, stato completed |
| `feedback --email x "hi"` | POST `kind=feedback_and_subscribe` |
| `feedback --subscribe --email x` | POST `kind=subscribe` |
| API down | stderr warning, exit 1, stato resta `active` |
| 100× `list` | Contatore invariato |

Test API (curl, indipendente dal backend):

```bash
curl -s -X POST "$ISSUEBEAM_INTAKE_API_BASE/v1/intake" \
  -H "Content-Type: application/json" \
  -H "X-App-Token: $ISSUEBEAM_APP_TOKEN" \
  -d '{
    "kind": "feedback",
    "message": "test from curl",
    "product": "issuebeam",
    "source": "agent_driven_feedback",
    "client_version": "issuebeam-cli"
  }'
```

---

## 10. Stima implementazione

| Task | Tempo |
|------|-------|
| Stato JSON + gitignore | 30 min |
| Hook contatore + nota stdout | 1 h |
| Comando `feedback` / `--subscribe` / `--decline` + client API | 1 h |
| Server intake (qualsiasi stack) | fuori scope CLI — 2–4 h separati |
| Test manuali CLI + curl | 30 min |

**Totale CLI ~3 h.** Backend intake a parte.

---

## 11. Changelog

| v1 | v2 | v2.1 |
|----|-----|------|
| Fake system message | Nota `issuebeam:` trasparente | — |
| Webhook n8n | — | **API REST `/v1/intake`** backend-agnostic |
| Solo feedback testuale | — | **`feedback` + `subscribe` + combinati** |
| Solo `COMPLETED` | `completed` + `declined` + cooldown | — |
| Contatore su ogni comando | Solo comandi backlog | — |
| `.usage_count` testuale | `.feedback_state.json` | — |
