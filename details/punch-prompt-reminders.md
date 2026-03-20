## Overview

Punch Prompt Reminders are smart notifications triggered by GPS geofencing that alert employees when they enter or exit designated work locations, prompting them to clock in or out and eliminating the most common cause of inaccurate timesheets—forgetting to manually track time.

## How It Works

### Geofence Setup
Managers define virtual boundaries around:
- Office locations
- Client sites
- Construction job sites
- Service call locations
- Any designated work area

### Location Monitoring
During scheduled work hours, the mobile app:
- Monitors employee location in background
- Detects when boundaries are crossed
- Preserves battery through efficient location services

### Smart Notifications
When employee crosses a geofence:
- **Entering**: "You've arrived at [Job Site]. Clock in?"
- **Exiting**: "You're leaving [Job Site]. Clock out?"
- One-tap action to confirm
- Option to dismiss if false positive

### Manager Alerts
When employees punch in/out outside geofence:
- Notification to supervisor
- GPS coordinates logged
- Helps identify location discrepancies
- Prevents time theft

## Key Benefits

### For Employees
- Never forget to clock in/out
- Accurate time capture without effort
- Peace of mind about timesheet completeness
- Immediate reminders when needed most

### For Managers
- Complete, accurate timesheets
- Verification employees are at correct locations
- Reduced time spent correcting timesheet errors
- Real-time job site attendance visibility

### For Payroll
- Fewer timesheet corrections needed
- Accurate hours for processing
- Reduced payroll disputes
- Audit trail for compliance

## Implementation Example: Timesheet Mobile

### iPhone and Android Support
Both platforms receive:
- Push notifications upon geofence crossing
- One-tap clock in/out
- Visual confirmation of punch
- Offline queueing if no signal

### Customization Options
- Set reminder frequency (every time, once per shift, etc.)
- Adjust geofence radius (100m to 1km typical)
- Configure notification sounds
- Schedule active hours

### Manager Notifications
- Choose which events trigger alerts
- Set notification delivery (email, SMS, push)
- Configure alert thresholds
- Review notification history

## Advanced Features

### Smart Scheduling Awareness
Only prompts during scheduled shifts:
- No reminders outside work hours
- Adapts to shift schedules
- Respects time-off calendars

### Multi-Site Workers
Handles employees who work at multiple locations:
- Different geofences for different sites
- Automatic site identification
- Correct project/client assignment

### Tolerance Zones
Buffer areas to prevent notification spam:
- Doesn't trigger for brief boundary crosses
- Requires being inside for X minutes before prompting
- Prevents alerts from driving past site

## Privacy Considerations

### Location Tracking Limits
- Only active during scheduled work hours
- Stops tracking when clocked out
- Employee can disable outside work
- Complies with privacy laws

### Transparency
- Employees know they're being tracked
- Clear policies documented
- Access to own location data
- Opt-out for privacy concerns

## Use Cases by Industry

### Construction
- Multiple job sites per day
- Verify crews are at correct locations
- Accurate job costing by site

### Field Services
- HVAC, plumbing, electrical contractors
- Service call time verification
- Customer location confirmation

### Healthcare
- Home health aides
- Visiting nurses
- Patient visit verification

### Delivery Services
- Drivers at pickup/dropoff locations
- Route verification
- Stop duration tracking

### Sales
- Outside sales reps
- Client visit logging
- Territory coverage verification

## Integration with Autopunch

Some systems combine with automatic punching:
- **Prompt Mode**: Asks employee to confirm
- **Auto Mode**: Automatically punches in/out
- **Hybrid**: Auto-punch in, prompt to punch out

Employers can choose based on:
- Trust level
- Accuracy needs
- Employee preference
- Regulatory requirements

## Technical Requirements

### Device Support
- iOS (iPhone, iPad)
- Android smartphones
- GPS-enabled devices
- Internet connectivity (cellular or WiFi)

### Battery Impact
- Modern implementations use ~5-10% extra battery
- Geofencing more efficient than continuous GPS
- Background location services optimized
- Minimal impact on device performance

## Compliance Benefits

### Labor Law Compliance
- Accurate work hour records
- Break time tracking
- Overtime calculations
- Audit trail for investigations

### Client Requirements
- Proof of service delivery
- Time spent at customer locations
- Documentation for billing

## ROI Calculation

### Time Saved
For 20-person field team:
- **Before**: 30 min/week/person correcting forgotten punches = 10 hours/week
- **After**: Negligible correction time
- **Savings**: 520 hours annually

At $15/hour administrative cost:
- **Annual savings**: $7,800
- Plus: more accurate billing, reduced disputes

## Common Questions

### "What if I forget my phone?"
Backup methods:
- Call-in IVR system
- Text message punch
- Manual entry with approval

### "Does it drain my battery?"
Minimal impact with modern geofencing:
- Uses cell tower triangulation
- Not continuous GPS tracking
- Background processing optimized

### "What about privacy?"
- Location tracked only during work hours
- Employee controls when tracking active
- Transparent about what's monitored
- Data used only for timekeeping

## Best Practices

1. **Clear Communication**: Explain why geofencing benefits everyone
2. **Test Geofences**: Ensure boundaries are correctly sized
3. **Adjust Sensitivity**: Find balance between reminders and spam
4. **Provide Alternatives**: Manual punch options for edge cases
5. **Respect Privacy**: Stop tracking outside work hours
6. **Regular Review**: Audit alerts to optimize settings