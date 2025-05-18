# Ultimate Time Tracker

[Source Code](https://github.com/larose/utt)

## Description
Ultimate Time Tracker (utt) is a simple, Python-based command-line application for tracking time. It is designed for users seeking straightforward time logging and reporting via the terminal.

## Features
- **Command-line Interface**: Operate entirely from the terminal using simple commands.
- **Easy Installation**: Install via PyPI with `pip install utt`.
- **Task Logging**: Log tasks after completion using the `add` command.
- **Start Day Tracking**: Use the `hello` command to start tracking your day.
- **Activity Types**: Supports three types of activities: working, break, and ignored (distinguished by naming conventions).
- **Timesheet Editing**: Edit your timesheet directly in your preferred text editor via the `edit` command.
- **Reporting**: Generate detailed timesheets and reports for a specific day, date, or range, including:
  - Summary (total working and break time)
  - Grouping by project
  - Grouping by activity name
  - Timeline of activities
- **Project Tracking**: Assign activities to projects with a simple prefix syntax (e.g., `project-1:`).
- **Current Activity Tracking**: View and customize the current activity in reports.
- **Stretch Feature**: Extend the latest task to the current time with the `stretch` command.
- **Plugins**: Support for plugins to extend functionality (plugin system available, but no official plugins yet).
- **Configuration**: Customizable settings, including experimental timezone support.
- **Bash Completion**: Provides bash command auto-completion via `argcomplete`.
- **Open Source**: Licensed under GPLv3.

## Pricing
- Ultimate Time Tracker is open source and free to use.

## Tags
open-source, command-line, python, logging

## Category
time-tracking-cli-tools