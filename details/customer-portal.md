# Customer Portal

**Category:** Web-based time tracking  
**Brand:** Kimai  
**Website:** <https://www.kimai.org/documentation/plugin-customer-portal.html>

Customer Portal is a Kimai feature that lets you share time tracking statistics and detailed project timesheets with clients or external stakeholders via a secure, secret URL. It focuses on transparent access to tracked time data without requiring full user accounts.

![Customer overview](https://www.kimai.org/images/kimai-screen-customers.png)
![Project overview](https://www.kimai.org/images/kimai-screen-projects.png)

---

## Features

### Secure sharing via secret URLs
- Share customer or project data through unique, secret URLs.  
- Optional password protection for each shared URL.  
- Recipients do not need a Kimai user account.

### Customer-level sharing
- Share all recorded timesheets for a specific customer.  
- Display a table of all projects for that customer, including:
  - Project name
  - Budget statistics (when customer statistics are active)
- Optional additional customer details:
  - **Timesheets options**
    - Show name of the user who tracked the time
    - Show rates (hourly rate, total rate)
  - **Chart options**
    - Annual chart: month-by-month comparison for a selected year
    - Monthly chart: day-by-day comparison for a selected month
  - **Statistics**
    - Budget statistics
    - Time-budget information

### Project-level sharing
- Share all recorded timesheets for a specific project.  
- Optional additional project details:
  - **Timesheets options**
    - Show name of the user
    - Show rates (hourly rate, total rate)
  - **Chart options**
    - Annual chart (month comparison by selected year)
    - Monthly chart (day comparison by selected month)
  - **Statistics**
    - Budget statistics
    - Time-budget information

### Timesheet record merging
Control how individual time records are displayed for a day:
- No merging: each record shown as its own line.  
- Merge all records and show descriptions of all entries.  
- Merge all records and show only the description of the first entry.  
- Merge all records and show only the description of the last entry.

### Password protection
- Assign a password to any shared URL.  
- Recipients must enter the password before they can view customer or project data.

### Language handling
- Language is encoded in the URL prefix, e.g. `/en/auth/customer-portal/0123456789`.  
- Change the language by altering the code in the URL (e.g. `/de/`, `/es/`, `/fr/`).  
- Allows sharing in different interface languages without additional configuration.

### Permissions and access control
- Permission key: `customer_portal`.  
- Controls access to the **Customer portal** menu under `Administration > Customer portal`.  
- Users with this permission can create, edit, and delete all shared URLs.  
- By default, assigned to users with the role `ROLE_SUPER_ADMIN`.

---

## Pricing

No pricing information is provided in the supplied content.