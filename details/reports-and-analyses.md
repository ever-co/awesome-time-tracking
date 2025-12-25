# Reports and Analyses (Kimai)

**Category:** Web-based time tracking  
**Brand:** Kimai  
**Source:** https://www.kimai.org/documentation/reporting.html

## Overview
The *Reports and Analyses* module in Kimai provides analytical views over recorded time entries. It allows users (with appropriate permissions) to break down tracked time by user, time period, and project, and to view aggregated, rounded data that is also used in invoices and exports.

## Features

### Permissions & Access Control
- Access to reporting via the `view_reporting` permission.
- Reports use rounded time data (consistent with invoices and exports).
- Permissions affecting reporting views:
  - `view_other_timesheet`: enables choosing other users in reports.
  - `view_other_reporting`: allows seeing reports that include other users.
  - `view_all_data`: allows viewing data of all users (otherwise limited to team members).
- When `view_other_timesheet` is granted:
  - The displayed username is replaced with a user selection box.
  - Available users to choose from are:
    - All users (if `view_all_data` is granted), or
    - Team members (if the current user is a team leader).

### User Visibility / Reporting FAQ
- Reasons a user may not appear in reports:
  - The current user is not allowed to see that user’s data (permissions restriction).
  - The target user account is **deactivated**:
    - The user will not appear in the dropdown selection.
    - Existing time data for that user is still reported for selected periods.
  - The target user account is flagged as **System-Account**:
    - This flag can be checked in the user profile.
    - Users cannot set these flags for their own account.

### Single-User Time Reports
Reports focused on the working times of a single user.

#### Weekly view for one user
- Displays working times for one user over a single calendar week.
- Adjustable parameters:
  - Calendar week.
  - User (if `view_other_timesheet` is granted).
- Required permission: `view_reporting`.

#### Monthly view for one user
- Displays a full month of working times for one user.
- Adjustable parameters:
  - Month.
  - User (if `view_other_timesheet` is granted).
- Required permission: `view_reporting`.

#### Yearly view for one user
- Displays a full year of working times for one user.
- Adjustable parameters:
  - Year.
  - User (if `view_other_timesheet` is granted).
- Required permission: `view_reporting`.

### Multi-User / List-of-Users Reports
Aggregated working time reports across multiple users.

#### Weekly view for all users
- Displays a full week of working times for all accessible users.
- Adjustable parameter:
  - Week.
- Required permissions:
  - `view_reporting`
  - `view_other_timesheet`
  - `view_other_reporting`

#### Monthly view for all users
- Displays a full month of working times for all accessible users.
- Adjustable parameter:
  - Month.
- Required permissions:
  - `view_reporting`
  - `view_other_timesheet`
  - `view_other_reporting`

#### Yearly view for all users
- Displays a full year of working times for all accessible users.
- Automatically switches between calendar year and financial year, depending on company configuration.
- Adjustable parameter:
  - Year.
- Required permissions:
  - `view_reporting`
  - `view_other_timesheet`
  - `view_other_reporting`

### Project-Based Reports
Reports focused on time and budget at project level.

#### Project overview
- Shows a list of all projects the user has access to, including:
  - Summed-up recorded times.
  - Summed-up monetary amounts.
  - Budget information.
  - Time-budget progress bars.
  - Links to invoice and export screens.
- Filters and options:
  - Filter projects by customer.
  - Option to include/exclude projects without budgets.
  - Option to include/exclude projects without recorded times.
- Required permissions:
  - `view_reporting`
  - `budget_project`

#### Project details
- Shows detailed reports for a single selected project.
- Sums up recorded times grouped by various characteristics (e.g. different report groupings such as user, activity, etc. as supported by Kimai).
- Required permissions:
  - `view_reporting`
  - `details_project`

#### Monthly project report
- Displays a summary of projects that are (or were) visible and active for a selected month.
- Adjustable parameter:
  - Month used to filter projects.
- For the selected month, shows:
  - **Monthly budget** and a progress bar of logged time vs. that budget.
  - Additional indicators for projects with a regular (full-time) allocation (as supported/configured in Kimai).

## Use Cases
- Billing: Use rounded, invoice-ready time data grouped by user or project.
- Performance monitoring: Compare weekly, monthly, and yearly workloads per user or team.
- Workload and budget control: Track project time vs. budget, and monitor monthly project activity.

## Pricing
No pricing information is provided in the supplied content. For current pricing or licensing details, refer to the official Kimai website.