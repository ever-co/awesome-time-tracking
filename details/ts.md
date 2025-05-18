# ts

[Source Code](https://github.com/ses4j/ts)

**Category:** Time Tracking CLI Tools  
**Tags:** open-source, timesheet, programmers, contractors

## Description
**ts** is an open-source, text-based timesheet parser designed for contractors and programmers to efficiently track work hours. It uses human-friendly, computer-parseable text files—one file per contract—for logging time entries in a simple, programmer-oriented format.

## Features
- **Text-Based Timesheet Parsing:** Allows users to log work hours using plain text files.
- **Programmer-Friendly Format:** Entries are easy to write and read, designed with programmers in mind.
- **Per-Contract Files:** Organize timesheets by keeping one file per contract.
- **Canonicalization:** Automatically parses and standardizes timesheet entries.
- **Global Configuration Support:** User default settings can be managed via a `~/.tsconfig.yml` file (or `%USERPROFILE%.tsconfig.yml` on Windows).
- **Invoice Generation:** Generate PDF invoices from timesheet entries using an invoice marker and the `-i/--invoice` option. Supports custom invoice file naming templates with variables (e.g., `{invoice_code}`).
- **Comment Support:** Include comments in timesheets that can be added to invoices.

## Pricing
This tool is open-source and free to use under its respective license.