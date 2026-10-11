# API and layering

Keep HTTP adapters thin: parse request, call a service, shape the response. Put business logic in services that do not import FastAPI or the API package, so a script or worker can call the same function.

HTTP clients stay in a clients layer: call the API, return typed data; no business logic or DB. Normalize into domain models before filters or services. Keep import direction `api -> services -> (clients, domain, filters, db)` unless this repo documents another split.

Config belongs in the project's settings module (often pydantic-settings), not scattered `os.environ`. Preserve existing request/response shapes; present breaking API changes before implementing them.
