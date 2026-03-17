## Overview

Jira includes native time tracking functionality that allows teams to log work hours, set time estimates, and track time remaining on issues. While basic compared to dedicated time tracking tools, Jira's built-in capabilities meet the needs of many development teams already using the platform.

## Core Time Tracking Features

**Time Fields** - Each Jira issue includes:
- **Original Estimate** - Initial time estimate for the work
- **Remaining Estimate** - How much time is left to complete
- **Time Spent** - Actual logged hours on the issue
- **Work Ratio** - Automatic calculation of progress (Time Spent / Original Estimate)

**Logging Work** - Multiple ways to track time:
- Log work dialog with time entry and work description
- Automatic remaining time adjustment
- Date selection for backdated entries
- Work log visibility controls (public, group, role-restricted)

**Time Formats** - Flexible time entry:
- Hours (2h, 8h)
- Days (1d, 5d)
- Weeks (1w)
- Combined (1w 2d 3h)
- Minutes (30m, 45m)

## Agile Board Integration

**Scrum Features**:
- Time tracking integrated with sprint planning
- Burndown charts can use time (hours/days) instead of story points
- Capacity planning based on team available hours
- Sprint reports showing time spent vs estimated

**Kanban Features**:
- Time in status tracking
- Cycle time analytics
- Cumulative flow diagrams with time metrics

## Reporting Capabilities

**Built-in Reports**:
- Time Tracking Report - Summary of work logged by user and issue
- Workload Pie Chart - Distribution of time across issues
- Time Since Issues Report - How long issues have been in certain states
- User Workload Report - See individual team member time allocation

**JQL Time Queries** - Filter issues by:
- `originalEstimate > 4h` - Issues estimated over 4 hours
- `timeSpent > 0` - Issues with logged time
- `remainingEstimate = 0` - Issues with no remaining work

## Limitations of Native Tracking

- No timer functionality (must manually enter time)
- Limited reporting compared to dedicated time tracking tools
- No billable vs non-billable categorization
- No invoicing or client billing features
- Basic time analytics without advanced insights
- Sub-task time doesn't automatically roll up to parent

## Popular Jira Time Tracking Apps

Many teams augment Jira's native capabilities with marketplace apps:

**Tempo Timesheets** - Most popular, adds:
- Timer functionality
- Advanced reporting and analytics
- Billable hours tracking
- Budget management
- Approvals workflow
- Integration with accounting systems

**Hubstaff for Jira** - Provides:
- Automatic time tracking
- Activity monitoring
- Screenshots (optional)
- GPS tracking for field teams

**Everhour** - Offers:
- Browser extension with timer
- Budget tracking
- Improved reporting
- Client billing features

**Clockify** - Free tier includes:
- Jira integration
- Timer and manual entry
- Basic reporting
- Unlimited users

## When Native Tracking Is Sufficient

- Development teams tracking for sprint planning and velocity
- Internal projects without client billing
- Teams wanting simplicity over advanced features
- Organizations already managing complex toolchains
- Agile teams using story points as primary metric

## When to Upgrade

- Client billing and invoicing requirements
- Detailed time analytics and reporting needs
- Budget tracking against projects
- Approval workflows for timesheets
- Automatic tracking and productivity monitoring
- Integration with accounting/payroll systems

## Configuration

Jira administrators can:
- Enable/disable time tracking site-wide
- Set default time units (hours, days)
- Define working hours per day
- Control work log visibility and permissions
- Customize issue screens to show/hide time fields

## Pricing

Time tracking is included in all Jira Software and Jira Work Management tiers at no additional cost. Third-party time tracking apps have separate pricing, typically per user per month.