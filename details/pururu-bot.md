# pururu-bot

A Discord bot for attendance management, featuring automated tracking, clock-in/clock-out, and absence monitoring, designed for use on a specific Discord server.

- **Category:** Automated Time Tracking
- **Tags:** automation, attendance, chatops, discord
- **Source:** [GitHub Repository](https://github.com/jlvadell/pururu-bot)

## Features
- **Automated Attendance Tracking:** Uses Discord's voice state updates to automatically track user attendance during events or sessions.
- **Clock-in/Clock-out Functions:** Provides tools for users to record their start and end times.
- **Absence Monitoring:** Monitors and records user absences.
- **Google Sheets Integration:** Uses Google Sheets (via Google Sheets API) as the primary database for storing attendance, clocking, and event logs, allowing for easy data visualization and editing.
- **Event Logging:** Records detailed event logs in Google Sheets.
- **Bot Commands:**
  - `/ping`: Checks if the bot is online and returns its current version.
  - `/stats`: Returns a summary of the user's attendance data.
- **Configurable Deployment:** Can be deployed on AWS EC2 instances using GitHub Actions workflows.
- **Customization:** Supports configuration through environment files and allows for some customizations to fit specific server needs.
- **No Special Permissions Required:** Only basic Discord bot permissions are needed.
- **Open Source:** Licensed under the Apache License 2.0.

## Pricing
No pricing information is provided; the project is open source.

## Notes
- This bot is primarily intended for private use on a specific Discord server, but the code is available for others to use or modify.
