# Learning Log

## 2026-08-30 — Phase 0 begins

### What we built

- Minimal README and project-status documentation.
- A durable learning log for future phases.
- A local Git repository using the `main` branch.
- A public GitHub repository with local `main` tracking `origin/main`.
- A working VS Code Source Control integration using the installed Git executable.
- An isolated Python 3.12.13 virtual environment for OpenDramaFlow.

### Concepts learned

- A repository is the project boundary whose history Git tracks.
- The working tree is the current set of files visible on disk.
- Untracked files exist in the working tree but are not yet tracked by Git.
- The staging area selects the exact changes that belong in the next commit.
- A commit records local history; a push transfers local commits to a remote repository.
- `origin` is the conventional local name for the primary remote repository.
- VS Code Source Control is a graphical interface over the same Git repository and state model used by the terminal.
- A virtual environment isolates one project's Python interpreter and dependencies from other projects.
- Activating a virtual environment temporarily changes the terminal `PATH`; it does not start a separate Python service.
- PowerShell execution policy can be changed for one process without weakening the permanent system policy.
- A runtime environment supplies the executable and dependencies needed to run code.
- A process is a running program; a port lets network clients address a listening process.

### Commands used

- `git --version` checks whether Git can be found and started.
- `git init` creates a local repository without uploading anything.
- `git status` shows the relationship between the working tree, staging area, and repository.
- `git add` stages selected changes for the next commit.
- `git diff --cached` reviews the changes currently selected for commit.
- `git commit -m "..."` creates a local commit from staged changes.
- `git remote -v` displays configured remote repository addresses.
- `git push -u origin main` pushes `main` and establishes its upstream tracking branch.
- `git log --oneline` displays a compact commit history.
- `python -m venv .venv` creates a project-local Python virtual environment.
- `.\.venv\Scripts\Activate.ps1` activates that environment in PowerShell.
- `where.exe python` shows which Python executable the shell resolves first.
- `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` permits local activation scripts only for the current terminal process.
- `python --version` checks the active Python interpreter.
- `node --version` and `npm --version` check the JavaScript runtime and package manager.
- `docker --version` and `docker compose version` check the container toolchain.

### Code I wrote

- Initialized the repository, configured its branch and author identity, staged the initial documentation, created the first commit, and pushed it to GitHub.
- Created the initial `.gitignore` rules for the Python environment, cache, and local secrets.
- Created, activated, and verified the project-local Python environment.

### Problems encountered

- Git was initially unavailable and was installed before repository initialization.
- The first commit attempt correctly failed because no author identity was configured.
- Node.js, npm, and Docker are not currently discoverable from the command line.
- The generic `python` command fails, although Python 3.12.13 and 3.13.13 interpreters exist under Miniconda.
- VS Code initially could not discover Git because it was installed at a non-default path; setting `git.path` resolved it.
- A Git diff opened in a pager; pressing `q` returned to the command prompt.
- A trailing space in the `.env` ignore pattern was detected during review and must be removed before commit.
- PowerShell initially blocked the activation script; a process-scoped `RemoteSigned` policy resolved it without a permanent policy change.
- The VS Code terminal initially lacked Git on `PATH`; adding `E:\Git\cmd` to the terminal environment resolved it.

### What I can now explain

- The difference between a local repository and a remote repository such as GitHub.
- Why the staging area lets one commit contain only related changes.
- The path from an untracked file to a staged change and then a commit.
- The difference between commit and push, and the relationship between `main` and `origin/main`.
- How VS Code's Changes and Staged Changes sections map to the Git working tree and staging area.
- Why projects use separate virtual environments and what activation changes in the shell.

### What remains unclear

- Which dedicated Python environment configuration the project will use.
- Whether Node.js and Docker are uninstalled or installed outside `PATH`.
