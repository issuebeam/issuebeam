# Evolutiva: Retention Policy (Purge automatico dei pending)

## Obiettivo
Mantenere pulito il database SQLite `intake_events` sul Raspberry Pi eliminando automaticamente tutti i record di feedback/email che sono rimasti nello stato `pending` per più di 30 giorni. 

Questo assicura che il database non si riempia di "spam" o di utenti inattivi che non completano il processo di double opt-in, mantenendo l'archivio leggero e pienamente conforme ai principi di minimizzazione dei dati (Privacy/GDPR).

## Architettura Proposta
Lo script dovrà girare direttamente sul server backend (Raspberry Pi).

1. **Script Python (`purge_pending.py`)**: Uno script interno al progetto `issuebeam-intake` che:
   - Si connette al DB in `/data/intake.sqlite`
   - Esegue la query: `DELETE FROM intake_events WHERE status = 'pending' AND created_at < datetime('now', '-30 days');`
   - Registra nei log quanti record "orfani" sono stati spazzati via.

2. **Schedulazione (Cron Job)**:
   - Verrà aggiunto un comando nel crontab nativo del Raspberry Pi che esegue l'operazione in modo del tutto automatico ogni notte (es. a mezzanotte).
   - Comando ipotetico: `0 0 * * * docker exec issuebeam-intake python /app/scripts/purge_pending.py`

## Criteri di Accettazione (Do of Done)
- [ ] I record con stato `verified` **NON** vengono toccati.
- [ ] I record `pending` inseriti da meno di 30 giorni **NON** vengono cancellati, per dare tempo al dev di cliccare il link nella mail.
- [ ] L'esecuzione notturna del purge non causa downtime o errori sull'endpoint API che accetta i nuovi feedback.
