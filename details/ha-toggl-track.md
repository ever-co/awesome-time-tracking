# ha-toggl-track

A custom Home Assistant component to integrate Toggl Track API for time tracking automation.

- **Source:** [GitHub - kquinsland/ha-toggl-track](https://github.com/kquinsland/ha-toggl-track)
- **Category:** Time Tracking CLI Tools
- **Tags:** integration, api, open-source, automation

## Features
- Integrates Toggl Track with Home Assistant as a custom component.
- Adds sensors to Home Assistant for each Toggl Track workspace.
- Sensors reflect the current time entry's description and attributes for each workspace.
- Configurable polling interval to control how often the Toggl Track API is queried (default: 60 seconds).
- Supports multiple workspaces, with a sensor per workspace.
- Provides Home Assistant services for:
  - Creating new time entries (`toggl_track.new_time_entry`).
  - Stopping the current time entry (`toggl_track.stop_time_entry`).
  - Editing existing time entries (description and tags, `toggl_track.edit_time_entry`).
    - Can create new tags if needed, or remove tags (without deleting them).
- Can be installed via HACS as a custom repository or manually by copying the component folder.
- Requires API token for authentication.

## Pricing
- **Open Source** (No pricing information; available for free under open-source license)

## Installation
- Add the repository as a custom source in HACS or copy the `custom_components/toggl_track` folder manually.
- Configure via Home Assistant UI with your Toggl API token.

## Notes
- Still under development; some features and bugs are being worked on.
- Sensor updates are subject to polling interval and may not reflect real-time changes immediately.