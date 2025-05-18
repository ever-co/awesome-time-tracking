# work-snapshots

A tool that takes screenshots every few minutes to help users review and manage their work sessions.

- **Source:** [GitHub Repository](https://github.com/azeemba/work-snapshots)
- **Category:** Automated Time Tracking
- **Tags:** open-source, automatic-tracking, screenshot, usage-monitoring

## Features
- **Automatic Screenshots:** Takes screenshots at regular intervals when specific applications are running.
- **Session Grouping:** Screenshots are grouped into "work sessions" for better review and organization.
- **Tagging:** Each session can be tagged with a project to track time spent on various work items.
- **Activity Visualization:** The "Stats" page provides a heatmap of activity by day and a table summarizing time spent on different projects.
- **Selective Recording:** Recording can be disabled even when tracked applications are open by using a "Force Ignore Activity" function.
- **Tray Application:** Uses a tray icon (via AutoHotKey on Windows, a separate utility on Mac) to control enablement and disablement of screenshot recording.
- **Customizable Application List:** The tray component checks for running programs against a hardcoded list to determine when to record.
- **Cross-Platform Support:** Includes a Mac utility (tray-mac) for similar functionality, with data syncing possible between Mac and other machines.
- **Backend Server:** Python server backend for managing and serving work session data.
- **Frontend UI:** React-based frontend to browse work sessions and individual snapshots.

## Pricing
- **Open Source:** No pricing plans are mentioned; the tool is available as open source software.

## Requirements
- AutoHotKey for tray functionality on Windows.
- Screen recording privileges required on Mac.
- Some configuration (e.g., output directory, application list) is required before running.
