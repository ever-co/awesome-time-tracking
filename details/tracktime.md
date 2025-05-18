# tracktime

A command-line interface (CLI) program for tracking time on various tasks, storing data in a simple filesystem-backed structure using CSV files.

- **Source:** [GitHub Repository](https://github.com/sumnerevans/tracktime)
- **Category:** Time Tracking CLI Tools
- **Tags:** open-source, command-line, personal-use, simple

---

## Features

- **Time Tracking:** Track time on tasks directly from the command line.
- **Filesystem-backed Storage:** Uses a structured directory system (YEAR/MONTH/DAY) to organize time-tracking CSV files for each day.
- **CSV Format:** All time tracking data is stored in CSV files, allowing for easy editing and backup.
- **Configuration File:** Supports a YAML configuration file (`~/.config/tracktime/tracktimerc`) for user settings, such as:
  - Full name (for reports)
  - Synchronization options
  - Editor and editor arguments
  - GitLab integration (API root and API key)
  - Table format for report export
  - Project rates (for calculating totals in reports)
  - Customer aliases and addresses (for reports)
  - External synchronizer files
  - Minimum daily work threshold (to filter out short workdays)
- **Report Generation:** Can generate reports from tracked data. Export to stdout or PDF (requires `wkhtmltopdf`).
- **External Service Sync:** Ability to sync tracked time with external services, such as GitLab, by pushing changes. (One-way sync only.)
- **Custom Synchronizers:** Supports importing third-party synchronizers.
- **Platform Support:** Installation via PyPi or Arch Linux AUR.

## Pricing

tracktime is open-source software and is free to use.

## Dependencies

- **wkhtmltopdf:** Required for report generation in PDF format.

## License

Open-source (see [GitHub Repository](https://github.com/sumnerevans/tracktime) for details).
