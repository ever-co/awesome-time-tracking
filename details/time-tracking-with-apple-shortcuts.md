## Overview

Apple Shortcuts allows iPhone, iPad, and Mac users to create custom time tracking systems without installing dedicated time tracking apps. These automations can log work sessions, calculate billable hours, and integrate with existing Apple ecosystem apps.

## Basic Time Tracking Shortcuts

### Start/Stop Timer

**Simple Timer Shortcut**:
1. Get current date
2. Ask for project name
3. Store start time in note or file
4. Later: Calculate duration from start to current time
5. Log to Notes, Calendar, or Numbers spreadsheet

### Quick Time Entry

**Manual Entry Shortcut**:
1. Prompt for: Project, Task, Duration
2. Get current date/time
3. Format as CSV or JSON
4. Append to iCloud file or send to Numbers
5. Optional: Send to external service via API

### Pomodoro Timer

**Custom Pomodoro**:
1. Start 25-minute timer
2. Show notification when complete
3. Log pomodoro to tracking system
4. Ask: Another pomodoro or break?
5. Track total pomodoros per project

## Advanced Implementations

### NFC Tag Triggers

**Physical Time Clock**:
- Place NFC tags at workspace
- Tap to clock in/out
- Logs time, location, project automatically
- Works with iPhone XS or newer

### Location-Based Tracking

**Geo-fence Automation**:
- Arrive at client site → Start timer
- Leave site → Stop timer, calculate duration
- Add travel time automatically
- Log to calendar or spreadsheet

### Siri Integration

**Voice Commands**:
- \"Hey Siri, start working on Client A\"
- \"Hey Siri, stop tracking\"
- \"Hey Siri, show my time this week\"
- Hands-free time logging

## Data Storage Options

### Notes App
- Simple, built-in
- Easy to view and edit
- Search functionality
- No advanced reporting

### Numbers (Apple's Excel)
- Spreadsheet format
- Formulas for totals
- Charts and graphs
- Export to CSV

### Calendar Events
- Visual timeline
- Integrates with existing schedule
- Color coding by project
- Block time in advance

### Reminders/To-Do
- Combine with task management
- Check off when complete
- Add notes for details
- Less ideal for duration tracking

### iCloud Files
- CSV or JSON format
- Can be read by other apps
- Sync across devices
- Import to Excel, Google Sheets

## Integration Examples

### Toggl API Integration

**Shortcut to Toggl**:
1. Get time entry details
2. Format JSON payload
3. HTTP POST to Toggl API
4. Confirmation notification
5. Works with free Toggl account

### Airtable Logging

**Send to Airtable Base**:
1. Collect time entry data
2. Send to Airtable API
3. Automatic syncing
4. View in Airtable interface
5. Powerful reporting and views

### Google Sheets

**Append to Sheet**:
1. Format as CSV row
2. Use Google Sheets API
3. Append to specific sheet
4. Access from any device
5. Share with team or clients

## Sample Shortcut Workflows

### Freelancer Billing Tracker

**Complete Workflow**:
1. Morning: \"Start workday\" shortcut
2. Switch projects: Quick project picker
3. Log breaks automatically
4. End of day: Calculate total hours
5. Weekly: Export to invoice template
6. Monthly: Send summary via email

### Consultant Time Logger

**Client-Focused**:
1. Ask for client name (from list)
2. Start timer with notification
3. Idle detection: Prompt after 5 min inactivity
4. Auto-round to 15-minute increments
5. Add billable vs non-billable flag
6. Weekly export with client totals

### Student Study Tracker

**Academic Focus**:
1. Select subject from list
2. Start study session
3. Log Pomodoros completed
4. Track breaks taken
5. Daily/weekly study time reports
6. Goal setting and progress

## Advantages

### Cost
- Completely free
- No subscriptions
- No ads
- Unlimited use

### Privacy
- Data stays on your devices
- iCloud encryption
- No third-party data sharing
- Full control

### Customization
- Build exactly what you need
- Modify anytime
- No feature limitations
- Combine with other automations

### Integration
- Works with all Apple apps
- Siri voice control
- Widget support
- Share across devices

## Limitations

### Technical Skills
- Requires learning Shortcuts app
- Initial setup time investment
- Troubleshooting needed
- Not plug-and-play

### Features
- No automatic categorization
- No built-in analytics
- Manual data management
- Limited reporting compared to dedicated apps

### Platform Lock-in
- iOS/macOS only
- Doesn't work on Windows/Android
- Team collaboration difficult
- Sharing workflows requires Apple devices

### Maintenance
- Must maintain shortcuts yourself
- iOS updates can break shortcuts
- No customer support
- Documentation is community-driven

## Getting Started

### Prerequisites
- iPhone (iOS 14+) or Mac (macOS Big Sur+)
- Basic understanding of if/then logic
- Time to experiment and iterate

### Learning Resources
- Apple Shortcuts User Guide
- YouTube tutorials (Matthew Cassinelli)
- Reddit: r/shortcuts
- RoutineHub.co (share shortcuts)
- MacStories Shortcuts Archive

### First Steps
1. Open Shortcuts app
2. Start with \"Gallery\" templates
3. Modify existing shortcuts
4. Experiment with actions
5. Test thoroughly before relying on

## Pro Tips

- **Backup shortcuts**: Export regularly
- **Use dictionaries**: Store structured data
- **Menu actions**: Create choice-based workflows
- **Repeat actions**: Loop through lists
- **Error handling**: Add \"If\" checks
- **Notifications**: Confirm actions completed
- **Variables**: Store and reuse data
- **Comments**: Document complex shortcuts

## Popular Time Tracking Shortcut Templates

### Available on RoutineHub
- Time Tracker Pro
- Work Log
- Billable Hours
- Study Timer
- Project Time Logger
- Daily Summary

### Features to Look For
- Data format (CSV, JSON)
- Storage location (Notes, Files, Cloud)
- Reporting capabilities
- Project/client management
- Export options

## 2026 Enhancements

**New in iOS 18/macOS 15**:
- Better widgets for quick logging
- Improved automation triggers
- More app integrations
- Enhanced Siri intelligence
- Shared shortcuts via iCloud

## When to Use vs Dedicated App

### Choose Shortcuts if:
- You want free solution
- Privacy is paramount
- Need custom workflow
- Already use Apple ecosystem
- Simple tracking needs

### Choose Dedicated App if:
- Need team collaboration
- Want automatic tracking
- Require advanced reporting
- Need customer support
- Platform agnostic needs