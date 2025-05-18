# time-tracker-agent

**Category:** Automated Time Tracking  
**Tags:** automatic-tracking, open-source, productivity, reporting

## Description

time-tracker-agent is an open-source application designed to track the time spent on desktop applications. It is useful for productivity analysis and reporting.

## Features
- Runs as a Windows service.
- Provides an API endpoint (http://*:5050).
- Built on .NET Core 3.1.
- Tracks active window and detects the current running application.
- Records time spent on each application.
- Logs idle time when the user is inactive.
- Saves tracking data in an XML file at `%ProgramData%/TimeTrackerAgent/Data` on Windows.
- Can be extended to support other platforms (e.g., Linux).
- Includes a project for installation using WiX.

## Pricing
- Open-source (free to use)

## Source
[https://github.com/Stigmatoz/time-tracker-agent](https://github.com/Stigmatoz/time-tracker-agent)
