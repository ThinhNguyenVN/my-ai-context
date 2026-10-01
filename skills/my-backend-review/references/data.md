# Data integrity

Inspect actual schema/ORM and query path. Review invariants, migrations, transactions, concurrency/idempotency and data separation only where affected. Do not run destructive migrations or choose new DB/ORM. Validate relevant race/integrity scenarios with focused tests.
