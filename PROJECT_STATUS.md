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

## In progress

- Verify and establish the Docker development environment.

## Blocked

- `node` and `npm` are not available on the current `PATH`.
- `docker` and Docker Compose are not available on the current `PATH`.

## Next

1. Verify or install Docker and Docker Compose.
2. Record the final Phase 0 toolchain.
3. Prepare the first Phase 1 backend task.

## Known bugs

- None; application code has not started.

## Technical debt

- The exact supported versions and installation instructions are not documented yet because no runtime has been verified.
- No `.gitignore` exists yet; it will be introduced alongside the first real development artifacts.
