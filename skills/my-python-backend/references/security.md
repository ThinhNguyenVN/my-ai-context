# Security

Secrets live in gitignored `.env`. Keep `.env.example` in sync with Settings using safe placeholders. Never hardcode API keys, connection strings or realistic-looking secrets in code, tests or committed docs.

Do not invent JWT, OAuth or a new auth library. Follow the current auth model, or none if the MVP has none. Avoid logging secrets and raw credentials. Include concrete impact and a minimal fix for findings.
