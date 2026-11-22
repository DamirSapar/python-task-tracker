# Operating Guidelines for AI Agents

## Project Purpose & Architecture
Simple Python-based Task Tracker repository.
- `app/`: Contains data models and service business logic.
- `tests/`: Automated unit test suite using `pytest`.

## Safe Commands
- Install dependencies: `pip install -r requirements.txt`
- Run unit tests: `pytest`
- Check code quality: `flake8 app/`

## Coding Conventions & Test Expectations
- Code must comply with PEP 8 standards.
- Every new feature or fix must include corresponding tests in `tests/`.
- All tests must pass before proposing code changes.

## Prohibited Actions (Operating Boundaries)
- DO NOT store or commit plain-text credentials, API keys, or `.env` files.
- DO NOT push directly to the `main` branch or trigger unreviewed deployments.
- DO NOT remove existing unit tests or edit `requirements.txt` without human verification.
- DO NOT run destructive shell commands (`rm -rf`, disk partitioning, system modification).