# timetrace

**timetrace** is a free and open-source CLI tool for tracking working time, offering simple and efficient time logging directly from the command line.

Source: [https://github.com/dominikbraun/timetrace](https://github.com/dominikbraun/timetrace)

Category: Time Tracking CLI Tools

Tags: open-source, command-line, personal-use, simple

---

## Features

- **Simple CLI-based time tracking**: Start, stop, and manage time tracking directly from the terminal.
- **Project and module support**: Organize tracked time by projects and submodules (e.g., `grind-beans@make-coffee`).
- **Tagging**: Add tags to time records for enhanced categorization.
- **Billable/non-billable tracking**: Mark records as billable or non-billable, with support for project-level defaults.
- **Customizable configuration**: Use a config file to set preferences, such as clock format (12/24 hour), decimal hour display, and preferred editor.
- **Record management**: Create, edit, and delete records, including belated record creation and restoration of deleted/edited records and projects.
- **Status reporting**: View current tracking status, total time worked today, and break time.
- **Filtering and listing**: Filter records by date, project, or billable status; list all projects or records for specific periods.
- **Reports**: Generate reports (in beta) with filters for date range, billable status, project, and output format (including JSON export).
- **Shell integration**: Integrate with the Starship shell prompt for real-time status display.
- **Cross-platform installation**: Available via Homebrew, Snap, AUR, Scoop, Docker, and binary releases.

## Pricing

- **Free and open-source**

## Usage Example

- Create a project: `timetrace create project make-coffee`
- Start tracking: `timetrace start make-coffee`
- Add tags: `timetrace start make-coffee +tag1 +tag2`
- Stop tracking: `timetrace stop`
- List records: `timetrace list records today`

## Configuration Options

- Use 12-hour or 24-hour time format
- Display durations in decimal or mixed format
- Set default editor
- Per-project configuration (e.g., always billable)

---

For further details and advanced usage, see the [timetrace GitHub repository](https://github.com/dominikbraun/timetrace).