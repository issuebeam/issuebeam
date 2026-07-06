# Awesome Lists (GitHub)

**URLs:** Vari repository GitHub che iniziano con "Awesome" (es. https://github.com/vinta/awesome-python)
**Type:** Liste curate su GitHub. Ottime per traffico passivo continuo e backlink ad altissimo valore (DA altissimo).

## Status
- [x] **awesome-cli-apps — PR aperta.** [PR #1217](https://github.com/agarrharr/awesome-cli-apps/pull/1217) "Add issuebeam to AI Agents" — aggiunto nella sezione AI → Agents (non Development, categoria più pertinente trovata sul momento). Nessun conflitto, mergeable, in attesa di revisione del maintainer.
- [x] **Awesome Python (vinta/awesome-python) — PR aperta.** Aggiunto in "AI and Agents" → "Agent Skills" (ordine alfabetico tra `graphify` e `nuwa-skill`). PR compilata con il loro template specifico (checklist, criterio "Hidden Gem", sezione "How It Differs" su vendor-agnostic + zero-dependency design).
- [x] **kyrolabs/awesome-agents — PR aperta.** Aggiunto nella sezione "Software Development" (stesso gruppo di OpenHands, Aider), ordine alfabetico. Nessun template specifico richiesto, usata la descrizione standard.
- [x] **Awesome Open Source — Skippato.** Il link originale (Awesome-Windows/Awesome) è 404. Le alternative trovate non sono un fit pulito: oscafrica/awesome-open-source è una lista di risorse *sull'*open source (non di tool), sindresorhus/awesome è una meta-lista di altre liste. Le 3 PR già aperte (CLI apps, Python, Agents) coprono già i target più pertinenti e ad alto traffico.
- [x] **hesreallyhim/awesome-claude-code — Bloccato.** Creazione issue ristretta ai soli collaboratori del repo. Non contribuibile per ora.
- [x] **subinium/awesome-claude-code — Skippato (ineleggibile).** Il repo dichiara esplicitamente "Only repositories with 1,000+ stars are listed." issuebeam non li ha ancora — qualsiasi PR verrebbe chiusa a prescindere dalla categoria. Da riconsiderare in futuro quando/se il progetto cresce.
- [x] **jqueryscript/awesome-claude-code — PR aperta.** Aggiunto in fondo alla sezione "🧠 Agent Skills" (lista ordinata per numero di stelle decrescente, non alfabeticamente — issuebeam ha 0 stelle quindi va in coda). Nessun requisito minimo di stelle su questo repo.

## Strategia
Non puoi semplicemente incollare il tuo progetto. Devi aprire una Pull Request (PR) in questi repository rispettando le loro regole (di solito ti chiedono di aggiungere il tool in ordine alfabetico in una specifica categoria).

## Repository target per issuebeam

1.  **Awesome CLI:** https://github.com/agarrharr/awesome-cli-apps *(nota: il repo è stato rinominato da `awesome-cli` a `awesome-cli-apps`)* — ✅ fatto, vedi Status sopra
    *   *Categoria usata:* AI → Agents (trovata più pertinente di Development)
    *   *Descrizione usata:* `[issuebeam](https://github.com/issuebeam/issuebeam) - Connect AI coding agents directly to GitHub Issues via a standard Python CLI.`

2.  **Awesome Python:** https://github.com/vinta/awesome-python
    *   *Categoria proposta:* DevOps Tools o Command-line Tools
    *   *Descrizione per la PR:* `issuebeam - A zero-dependency CLI to wire AI assistants (Cursor, Claude, Copilot) to GitHub Issues.`

3.  **Awesome Agents:** https://github.com/kyrolabs/awesome-agents — ✅ fatto, vedi Status sopra *(nota: molti repo "awesome-ai-agents-2026" trovati in giro sembrano cloni/spam recenti, evitati)*
    *   *Categoria usata:* Software Development

4.  **Awesome Open Source:** https://github.com/Awesome-Windows/Awesome (essendo cross-platform) o liste generali di tools per sviluppatori.

## Template per la Pull Request
**Titolo:** Add issuebeam to [Categoria]

**Corpo PR:**
Hi! I'd like to add issuebeam to the list. 
It's a lightweight, standard-library-only Python CLI designed to connect AI coding agents (like Cursor, Claude Code, and Copilot) directly to GitHub Issues, preventing bugs from getting lost in AI chat logs.

I have read the contribution guidelines and ordered the list alphabetically. Thank you!
