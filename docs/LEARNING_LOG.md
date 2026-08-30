# Learning Log

## 2026-08-30 — Phase 0 begins

### What we built

- Minimal README and project-status documentation.
- A durable learning log for future phases.
- A local Git repository using the `main` branch.

### Concepts learned

- A repository is the project boundary whose history Git tracks.
- The working tree is the current set of files visible on disk.
- Untracked files exist in the working tree but are not yet tracked by Git.
- The staging area selects the exact changes that belong in the next commit.
- A runtime environment supplies the executable and dependencies needed to run code.
- A process is a running program; a port lets network clients address a listening process.

### Commands used

- `git --version` checks whether Git can be found and started.
- `git init` creates a local repository without uploading anything.
- `git status` shows the relationship between the working tree, staging area, and repository.
- `git add` stages selected changes for the next commit.
- `git diff --cached` reviews the changes currently selected for commit.
- `python --version` checks the active Python interpreter.
- `node --version` and `npm --version` check the JavaScript runtime and package manager.
- `docker --version` and `docker compose version` check the container toolchain.

### Code I wrote

- Initialized the repository, configured its branch and author identity, and staged the initial documentation.

### Problems encountered

- Git was initially unavailable and was installed before repository initialization.
- The first commit attempt correctly failed because no author identity was configured.
- Node.js, npm, and Docker are not currently discoverable from the command line.
- The generic `python` command fails, although Python 3.12.13 and 3.13.13 interpreters exist under Miniconda.

### What I can now explain

- The difference between a local repository and a remote repository such as GitHub.
- Why the staging area lets one commit contain only related changes.
- The path from an untracked file to a staged change and then a commit.

### What remains unclear

- Which dedicated Python environment configuration the project will use.
- Whether Node.js and Docker are uninstalled or installed outside `PATH`.
