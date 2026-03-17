## Overview

Haystack is a developer productivity platform that empowers engineering teams with real-time insights into their team's performance, helping remove bottlenecks and accelerate delivery by integrating directly with tools like JIRA and GitHub.

## Core Metric Framework

Haystack tracks "North Star" metrics to get a global picture of how engineering teams are performing, with metrics that remain in the control of engineering leaders and have been demonstrated to reflect an engineering team's ability to deliver business value.

## Key Metrics Categories

### DORA Metrics
DORA metrics including deployment frequency and change lead time highlight team-wide efficiencies and collaboration, particularly useful in measuring how collective practices impact delivery velocity and stability.

### Cycle Time
Tracks the time between the first commit and the merging of a pull request, indicating development speed and team performance, broken down into development speed and review speed.

### Review Process Metrics
Review time can be subdivided to help diagnose where slowdowns are occurring in the code review process (First Response Time, Rework Time, and Idle Completion Time).

### Additional Metrics
- **Change Failure Rate**: Percentage of deployments that created a production failure, indicating deployment process robustness
- **Throughput**: Measures team bandwidth and how much work can typically be accomplished, with teams aiming for consistent throughput

## Three Core Pillars

The first-principles approach asks "what would cause the team to fail?" and uncovers critical areas for measurement:
- **Speed**: Can the team deliver quickly enough?
- **Quality**: Does the team deliver code that works as expected?
- **Predictability**: Can the team deliver consistently and on schedule?

## Philosophy

Haystack intentionally decided not to surface metrics that enable micromanagement, specifically not allowing data to be grouped by individual engineers, as the evidence is clear that micromanagement is harmful.

## Integration

Integrates with JIRA, GitHub, and other development tools to provide comprehensive analytics without requiring manual data entry.