# Testing

Use pytest as the project runner. Mirror `app/` in `tests/`. Mock external HTTP (`httpx` + `respx` or the repo's existing helper); never hit live third-party APIs in automated tests.

Pick unit vs integration from the failure boundary. Pure filter/domain functions should not need DB or network. Cover changed contracts or persistence on the path you touch. Run the smallest sufficient check; no full-suite habit. Report what you could not verify.
