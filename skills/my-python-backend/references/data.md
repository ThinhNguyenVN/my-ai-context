# Data integrity

Inspect the actual ORM, session wiring and migrations. With SQLAlchemy 2 async, pass the session into services; do not import a global session from business code. Generate Alembic revisions only for real model changes; never hardcode a DB URL in migration env.

Keep missing/null values as null when the spec says so — do not coerce to `0`. Review invariants, transactions and idempotency only on the path you touch. Do not pick a new DB/ORM or run destructive migrations.
