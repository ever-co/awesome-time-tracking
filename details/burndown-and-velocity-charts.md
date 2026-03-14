## Overview

Burndown and velocity charts are complementary Agile metrics that help teams track progress, estimate capacity, and improve sprint planning. While burndown charts show daily progress toward sprint completion, velocity charts measure team output over multiple sprints.

## Burndown Charts

### What They Show

A burndown chart displays the amount of work remaining in a sprint or release, typically measured in:
- Story points
- Ideal hours
- Tasks remaining

### Key Elements

1. **X-Axis**: Time (days in sprint)
2. **Y-Axis**: Work remaining (story points or hours)
3. **Ideal Line**: Straight diagonal showing perfect burndown rate
4. **Actual Line**: Real progress, updated daily

### Reading Burndown Charts

- **Line above ideal**: Team is behind schedule
- **Line below ideal**: Team is ahead of schedule
- **Flat sections**: No progress for that period
- **Upward spikes**: Scope increase (new work added)

### Benefits

- Provides day-by-day measure of work completed
- Keeps team aware of scope creep
- Predicts likelihood of completing sprint work on time
- Promotes transparency and accountability
- Identifies blockers early

## Velocity Charts

### What They Measure

Velocity represents the amount of work (usually story points) a team completes in a single sprint. Tracking velocity over time helps teams:
- Estimate future sprint capacity
- Identify trends in productivity
- Plan releases more accurately

### Calculation

**Velocity = Sum of story points for all completed user stories in a sprint**

Historical velocity is typically calculated as the average over the last 3-7 sprints.

### Key Metrics

1. **Sprint Velocity**: Work completed in individual sprint
2. **Average Velocity**: Mean velocity over recent sprints
3. **Velocity Trend**: Whether capacity is increasing, decreasing, or stable

### Benefits

- Enables realistic sprint planning
- Improves long-term forecasting
- Identifies process improvements or degradation
- Helps predict release dates
- Supports commitment-based planning

## How They Work Together

### Complementary Insights

- **Velocity**: Focuses on team output over time (macro view)
- **Burndown**: Tracks daily progress within sprint (micro view)

### Combined Usage

1. Use **velocity** to determine sprint capacity during planning
2. Use **burndown** to monitor daily progress during sprint
3. Adjust velocity estimates based on burndown patterns
4. Identify correlations between burndown patterns and final velocity

## Best Practices

### For Burndown Charts

1. **Update Daily**: Track progress at the same time each day
2. **Don't Add Scope Mid-Sprint**: Maintains chart integrity
3. **Investigate Anomalies**: Flat lines or spikes indicate issues
4. **Focus on Trends**: Don't overreact to single-day variations

### For Velocity Tracking

1. **Use Consistent Estimation**: Keep story point scale stable
2. **Track 5-7 Sprints**: Provides reliable average
3. **Don't Game the System**: Inflating velocity defeats the purpose
4. **Account for Team Changes**: Adjust when team composition changes
5. **Consider External Factors**: Holidays, training, incidents affect velocity

## Common Pitfalls

### Burndown Chart Issues

- **The Hockey Stick**: All work completed on last day (poor task breakdown)
- **Stair Steps**: Work updated infrequently instead of daily
- **Scope Creep**: Continuous upward movement from added work

### Velocity Issues

- **Velocity as Performance Metric**: Using it to compare teams or judge individuals
- **Constant Increase Expectation**: Velocity should stabilize, not always increase
- **Ignoring Context**: Changes in team size, technology, or domain affect velocity

## Tools

Most Agile project management tools include built-in charts:

- Jira (with Tempo Timesheets)
- Azure DevOps
- Rally
- VersionOne
- Targetprocess
- ZenHub

## Advanced Variations

### Burnup Charts
Show work completed (increasing line) instead of work remaining, making scope changes more visible.

### Cumulative Flow Diagrams
Track work in different stages (To Do, In Progress, Done) over time, identifying bottlenecks.

### Velocity Range Charts
Show velocity variability with error bars or bands to indicate expected range.

## Metrics to Track Alongside

- Sprint commitment vs. completion rate
- Defect trends
- Cycle time and lead time
- Work in progress (WIP) limits
- Sprint retrospective action items