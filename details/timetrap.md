# Timetrap

[Timetrap](https://github.com/samg/timetrap) is a simple, open-source, command-line time tracker written in Ruby. It is designed for quick, terminal-based usage and allows users to efficiently track the time spent on various activities through a flexible interface.

## Features

- **Timesheets Management**: Organize tracked time into multiple timesheets.
- **Entry Tracking**: Each timesheet contains entries, each with start time, end time, and an optional note.
- **Command Abbreviation**: All commands can be abbreviated for faster usage.
- **Natural Language Time Parsing**: Accepts natural language time inputs (e.g., "5 minutes ago").
- **Notes Editing**: Add or edit notes for time entries, with support for external editors.
- **Output Formats**: Supports multiple output formats including text, CSV, iCal, JSON, and numeric IDs.
- **Custom Output Formatters**: Easily define custom output formats by implementing a Ruby class.
- **Harvest & Toggl Integration**: Community-supported formatters for integration with Harvest and Toggl time tracking services.
- **AutoSheets**: Automatically select the appropriate timesheet based on directory or custom logic.
- **Rounding**: Option to round entry times to configurable increments (default: 15 minutes).
- **Non-interactive Mode**: Supports a non-interactive flag for scripting and automation.
- **Command Autocomplete**: Bash and Zsh autocompletion for commands and timesheet names.
- **Comprehensive Commands**: Includes commands for archiving, editing, listing, displaying, resuming, deleting entries, and period-based summaries (today, yesterday, week, month).
- **Configuration**: Configurable via an ERB-interpolated YAML file for customizing behavior.
- **SQLite Backend**: Stores data in a local SQLite database.

## Commands Overview
- `archive`: Archive entries.
- `backend`: Open interactive database session.
- `configure`: Manage configuration file.
- `display`: Show timesheet entries.
- `edit`: Edit entries and notes.
- `in`/`out`: Start and stop timers.
- `kill`: Delete entries or timesheets.
- `list`: List all timesheets.
- `now`: Show running entries.
- `resume`: Resume tracking on an entry.
- `sheet`: Switch or create timesheets.
- `today`, `yesterday`, `week`, `month`: Period-based summaries.

## Tags
- open-source
- command-line
- ruby
- personal-use

## Pricing
Timetrap is open-source and free to use.