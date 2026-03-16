## Overview

Capacity planning uses time tracking data to understand team availability, predict project durations accurately, allocate resources optimally, and make realistic commitments based on actual historical performance rather than optimistic estimates.

## Core Concepts

### Available Capacity
Total potential working hours:
```
Team member: 40 hours/week
Minus meetings: -8 hours
Minus admin: -4 hours
Minus breaks: -2 hours
Available capacity: 26 hours/week
```

### Utilization Rate
Actual productive hours vs available:
```
Utilization = (Billable Hours / Available Hours) × 100
Target: 60-80% for sustainable performance
<50% = underutilized
>90% = burnout risk
```

### Historical Velocity
Actual delivery speed from past data:
```
Points completed per sprint
Features shipped per month
Tickets resolved per week
Use for future forecasting
```

## Data Collection

### Essential Metrics
- Hours worked per person per week
- Time by project/client
- Task completion times
- Meeting and admin overhead
- Interruption frequency
- Leave and absences
- Ramp-up time for new team members

### Historical Analysis Period
- Minimum: 3 months of data
- Ideal: 6-12 months
- Account for seasonality
- Remove outliers carefully
- Weight recent data higher

## Capacity Calculation

### Individual Capacity
```
Gross hours: 40/week
- Regular meetings: 6 hours
- Email/comms: 4 hours
- Admin tasks: 2 hours
- Training/learning: 2 hours
- Buffer for urgent: 4 hours
= Net capacity: 22 hours/week for project work
```

### Team Capacity
```
5 team members × 22 hours each = 110 hours/week
Historical utilization: 75%
Realistic weekly capacity: 82.5 hours
Monthly capacity: 330 hours (4 weeks)
```

### Accounting for Absences
```
Annual capacity: 330 hours/month × 12 = 3,960 hours
Vacation (avg 3 weeks/person): -330 hours
Sick leave (avg 5 days/person): -88 hours
Holidays: -132 hours
Adjusted annual: 3,410 hours
```

## Forecasting Project Duration

### Using Historical Data
1. **Similar past projects**: Average duration
2. **Component breakdown**: Sum of typical task times
3. **Velocity-based**: Points / average velocity
4. **Monte Carlo simulation**: Probability ranges

### Example
```
Project estimate: 400 hours
Team capacity: 82.5 hours/week
Basic math: 4.8 weeks

But accounting for:
- 20% buffer (unknowns): +1 week
- Ramp-up (new tech): +0.5 weeks
- Dependencies/waiting: +0.5 weeks

Realistic estimate: 6.8 weeks (~7 weeks)
```

## Resource Allocation

### Demand vs Supply
- **Demand**: All committed projects
- **Supply**: Available team capacity
- **Oversubscription**: Demand > Supply (red flag)
- **Underutilization**: Supply > Demand (opportunity)

### Optimization Strategies
- Stagger project starts
- Adjust timelines
- Add resources (hire/contract)
- Defer lower-priority work
- Negotiate reduced scope

### Skills Matching
- Not all hours are equal
- Senior dev ≠ junior dev
- Specialist vs generalist
- Consider learning curves
- Account for knowledge transfer

## Common Planning Scenarios

### New Project Request
1. Estimate hours required
2. Check available capacity
3. Identify resource conflicts
4. Propose realistic timeline
5. Communicate trade-offs

### Team Member Leave
1. Calculate impact (hours lost)
2. Redistribute work if possible
3. Adjust timelines
4. Communicate to stakeholders
5. Plan handoffs

### Multiple Projects
1. List all commitments
2. Sum total demand
3. Compare to supply
4. Prioritize work
5. Stack-rank projects
6. Communicate capacity constraints

## Tools & Dashboards

### Capacity Planning Software
- **Forecast**: AI-powered capacity planning
- **Resource Guru**: Team scheduling
- **Float**: Resource management
- **Tempo (Jira)**: Capacity reports
- **Mavenlink/Kantata**: PSA capacity

### Key Dashboard Elements
- Team utilization rates
- Upcoming capacity gaps
- Overallocation warnings
- Project pipeline demand
- Skills availability heatmap
- Forecast vs actual trending

## Best Practices

### Build in Buffers
- 20-30% contingency
- Unknown unknowns
- Optimism bias correction
- Interruptions and urgencies

### Update Regularly
- Weekly capacity reviews
- Monthly demand forecasting
- Quarterly planning adjustments
- Annual capacity modeling

### Communicate Constraints
- Transparent about capacity
- Trade-off discussions
- Realistic timelines
- Prioritization conversations
- No sandbagging

### Continuous Improvement
- Compare estimates to actuals
- Identify estimation patterns
- Refine models over time
- Share learnings
- Celebrate accuracy improvements

## Challenges & Solutions

### Inaccurate Estimates
- **Problem**: Past data unreliable
- **Solution**: Start tracking, improve over 3-6 months
- **Interim**: Use industry benchmarks, add larger buffers

### Changing Team Composition
- **Problem**: Turnover affects capacity
- **Solution**: Model ramp-up curves, account for knowledge loss
- **Prevention**: Document processes, pair programming

### Unplanned Work
- **Problem**: Interruptions consume capacity
- **Solution**: Reserve buffer capacity (15-25%), track interruptions
- **Improvement**: Reduce sources of unplanned work

### Optimism Bias
- **Problem**: Teams/managers underestimate duration
- **Solution**: Reference class forecasting (use similar past projects)
- **Check**: If estimate seems too good, it probably is

## Capacity Planning Maturity

### Level 1: No Planning
- Say yes to everything
- Hope for the best
- Constant firefighting
- Poor delivery

### Level 2: Basic Tracking
- Track time manually
- Rough estimates
- Some historical reference
- Occasional misses

### Level 3: Systematic Planning
- Regular capacity reviews
- Data-driven estimates
- Proactive allocation
- Reliable delivery

### Level 4: Predictive Analytics
- Machine learning forecasts
- Scenario modeling
- Optimization algorithms
- Strategic planning

## Metrics to Monitor

### Leading Indicators
- Capacity booked next month
- Pipeline demand
- Resource conflicts identified
- Hiring pipeline

### Lagging Indicators
- Utilization rate achieved
- Estimate accuracy
- On-time delivery %
- Client satisfaction

### Health Metrics
- Overtime hours
- Team burnout indicators
- Turnover rate
- Quality metrics

## Strategic Planning

### Quarterly Planning
1. Review past quarter performance
2. Forecast next quarter demand
3. Assess capacity gaps
4. Plan hiring/contracting
5. Communicate roadmap

### Annual Planning
1. Strategic goals
2. Required capacity
3. Team growth plan
4. Budget allocation
5. Phased delivery timeline

## Communication Templates

### When Declining Work
```
"Our team's current capacity is fully allocated through [date]. 
We can start this project on [realistic date] or 
discuss prioritizing it over [lower priority project]. 
What would you prefer?"
```

### When Adjusting Timelines
```
"Based on our actual velocity and current commitments, 
this project will take [realistic timeline]. 
We can accelerate to [shorter timeline] if we 
[add resources / reduce scope / delay other work]."
```

## ROI of Capacity Planning

### Benefits Quantified
- 15-25% more predictable delivery
- 10-20% better resource utilization
- 30-50% reduction in firefighting
- 20-40% less team burnout
- 2-3x improvement in estimate accuracy

### Cost Avoidance
- Prevent over-commitment penalties
- Reduce rushed/poor-quality delivery
- Avoid burnout-driven turnover
- Minimize opportunity cost of wrong work

## Key Takeaways

1. **Historical data beats optimism**: Use actual past performance
2. **Capacity ≠ Availability**: Account for meetings, admin, interruptions
3. **Buffer is not waste**: Contingency prevents chaos
4. **Communication is key**: Transparent capacity discussions build trust
5. **Continuous refinement**: Improve estimates with each project

## Getting Started

1. **Week 1**: Start tracking all time
2. **Week 4**: Calculate baseline utilization
3. **Month 2**: Compare estimates to actuals
4. **Month 3**: Use data for next project forecast
5. **Month 6**: Refine capacity model
6. **Ongoing**: Weekly capacity reviews

## Quote

"Hope is not a strategy. Capacity planning based on real data turns wishful thinking into reliable delivery."