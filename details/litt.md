# litt

A low-intrusion CLI time tracker with a minimal workflow, REST API, and simple JSON storage for easy integration.

Source: [https://github.com/Riebart/litt](https://github.com/Riebart/litt)

Category: time-tracking-cli-tools

Tags: open-source, command-line, api, minimalist

---

## Features
- **Command-Line Interface**: Provides a fast and terse CLI for time tracking.
- **Minimal Workflow Footprint**: Designed for minimal disruption and quick usage, can be integrated into keyboard macros.
- **Simple JSON File Database**: Stores all time tracking data in a single JSON file for easy manual editing and interoperability.
- **REST API**: Exposes a basic REST API for integration with other tools and systems.
- **Stopwatch Mode**: Start/stop a stopwatch to log time entries, suitable for inline workflow usage.
- **Ledger Mode**: Manually add time records with start and end times.
- **Aliases**: Define aliases to quickly assign descriptions, tags, and other options to time entries.
- **Edit/Amend Time Records**: Modify existing records using commands or direct JSON file editing for complex changes.
- **Filtering and Exporting**: List and filter tracked time data, export in CSV, JSON, YAML, and other formats.
- **Tagging**: Add tags to time records for categorization and filtering.
- **Hooks**: Run custom scripts (hooks) at specific events (pre/post commit, config changes, etc.) for automation.
- **Configurable**: Supports persistent and per-command configuration options.
- **Cross-Platform**: Stores data in user home directory on both Linux and Windows.
- **Extensible**: Advanced users can edit the JSON database directly or use tools like `jq`.
- **Short and Long Option Forms**: All CLI options have both short and long forms for convenience.
- **Flexible Date Parsing**: Uses `dateparser` to accept absolute or relative date/time specifications.
- **No Complex History Editing**: Keeps history simple, but allows manual edits for advanced needs.

## Pricing
- **Open Source**: No cost, available under an open source license.

## Installation
- Requires Python and the `dateparser` package. Full dependencies listed in `requirements.txt`.

---

For more details and usage examples, visit the [GitHub repository](https://github.com/Riebart/litt).