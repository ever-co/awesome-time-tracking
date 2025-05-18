# gtm

**gtm (Git Task Manager)** is a command-line tool for tracking tasks and time directly through git repositories, designed for developers seeking integrated time and task management within their workflow.

[GitHub Repository](https://github.com/laughedelic/gtm)

---

## Features

- **Time Tracking Integrated with Git:** Track time spent on commits in your git repositories. Each branch has its own timer, which automatically switches when you change branches.
- **Automatic Timer Management:** Timers start and stop automatically as you switch between branches. Global timer control allows you to start/stop timers from any directory.
- **Manual Timer Adjustment:** Adjust timer state if you forgot to start/stop it, using commands to add or subtract minutes.
- **Branch-based Task Management:** Treat each branch as a task. Optionally, bind branches to GitHub issues for task tracking.
- **Issue Integration:** Create and bind GitHub issues to branches. Automatically generate issues with tags based on branch naming conventions.
- **Pull Request Automation:** After pushing commits to a task branch, easily create pull requests linked to the corresponding GitHub issue.
- **Task Switching:** Switch between tasks using either branch names or associated issue numbers.
- **Task Closure:** Use a command to close tasks, which guides you through the necessary steps.
- **Reports Generation:** Generate reports on time spent per project or per task, including weekly reports.
- **Shell Prompt Integration:** Display concise timer information directly in your shell prompt (supports zsh and fish).
- **Multi-repository Support:** Seamlessly manage time tracking across multiple git repositories without manual timer switching.
- **Customizable Configuration:** Configure via git and supports custom hooks, with a warning that it may overwrite existing git hooks.

## Requirements

- Requires `git` and the `ghi` tool (for GitHub issue integration).
- Implemented as a bash script—can be installed by copying to PATH or linking/aliasing.

## Pricing

- **Open Source:** No pricing information; gtm is available for free under an open-source license.

## Tags

`open-source`, `command-line`, `developers`, `task-management`