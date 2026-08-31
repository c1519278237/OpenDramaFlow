# OpenDramaFlow

An open-source AI filmmaking workflow and production platform.

OpenDramaFlow 是一个开源 AI 影视生成工作流与生产平台，短期聚焦 AI 短剧自动生成。

## Project status

The project is currently in **Phase 1 — Minimal Backend**. The FastAPI application exposes a tested health endpoint; project creation and listing are next.

## Intended workflow

```text
Idea -> Story -> Screenplay -> Assets -> Storyboard
     -> Images -> Videos -> Audio -> Timeline -> Final MP4
```

## Development principles

- Build a real, runnable open-source project rather than a demo script.
- Add one working capability at a time and test it before moving on.
- Use pair programming so the learner writes each important concept at least once.
- Keep AI and storage integrations replaceable through provider interfaces.

## Requirements

Current development requirements:

- Python 3.12+
- Node.js 24 LTS (frontend work starts in a later phase)

Docker, PostgreSQL, and Redis are planned but are not required for the in-memory Phase 1 API.

## Backend quick start

Create and activate a virtual environment, then install the project and its development tools:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Run the development API:

```powershell
python -m uvicorn opendramaflow.main:app --reload
```

Verify the health endpoint at `http://127.0.0.1:8000/health` or open the interactive API documentation at `http://127.0.0.1:8000/docs`.

Run automated checks:

```powershell
python -m pytest
python -m ruff check backend
python -m ruff format --check backend
```

## Documentation

- `PROJECT_STATUS.md` tracks progress, blockers, and technical debt.
- `docs/LEARNING_LOG.md` records concepts and hands-on work completed during development.
