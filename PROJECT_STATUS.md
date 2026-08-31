# Project Status

## Current version

Pre-release / Phase 0 — Development Environment

## Completed

- Defined the project vision and phased learning roadmap.
- Created the minimal project documentation.
- Performed the initial local toolchain check.
- Installed Git, initialized the local repository, and selected `main` as the default branch.
- Practiced the working tree and staging area with the initial documentation.
- Created the first commit and pushed `main` to the public GitHub repository.
- Connected VS Code to the Git executable installed at `E:\Git\cmd\git.exe`.
- Created and activated an isolated Python 3.12.13 virtual environment in `.venv`.
- Verified that Git ignores the virtual environment and that the VS Code terminal can find both Python and Git.
- Installed and verified Node.js 24.20.0 LTS with npm 11.19.0.
- Assessed Docker prerequisites and identified the host virtualization limitation.

## In progress

- Finish the Phase 0 environment checkpoint and prepare Phase 1.

## Blocked

- Local Docker Desktop and WSL 2 are blocked because this Windows system runs inside a Sangfor aCloud VM without nested virtualization (`VirtualizationFirmwareEnabled`, `VMMonitorModeExtensions`, and `SecondLevelAddressTranslationExtensions` are all `False`).

## Next

1. Commit the Phase 0 environment assessment.
2. Start Phase 1 with an in-memory FastAPI health endpoint, which does not require Docker.
3. Revisit Docker when a host with nested virtualization or a remote Linux Docker engine is available.

## Known bugs

- None; application code has not started.

## Technical debt

- Formal setup instructions still need to be consolidated after the backend package is introduced.
- The development environment cannot currently run local Linux containers; PostgreSQL and Redis container workflows require a different host or remote Docker engine.
