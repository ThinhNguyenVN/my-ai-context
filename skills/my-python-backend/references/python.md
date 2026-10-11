# Python and tooling

Match the repo's Python version and package manager. Prefer `uv` when the project already uses it; do not switch to pip/poetry/conda. Type every function (params + return); avoid `Any` when a `TypedDict` or Pydantic model fits.

Use `async def` for I/O (HTTP, DB). Do not mix blocking calls (`requests`, `time.sleep`) into async code; use `httpx` async and async SQLAlchemy when that is the stack. Catch specific exceptions; log or re-raise with context.

Comment only a non-obvious why. Run the project's lint/format (often `uv run ruff check . && uv run ruff format .`) before calling work done.
