## Overview

A Cumulative Flow Diagram (CFD) is a powerful visualization tool adapted from Kanban methodology for time tracking and workflow analysis. It provides a layered view of all four important metrics simultaneously: work-in-progress, cycle time, lead time, and throughput.

## What It Shows

### Visual Structure

The CFD is a stacked area chart where:
- **X-axis**: Time (days, weeks)
- **Y-axis**: Number of work items
- **Colored bands**: Workflow stages (To Do, In Progress, Review, Done)
- **Band width**: Number of items in each stage
- **Vertical distance**: Cycle or lead time

### The Four Key Metrics

**1. Work-in-Progress (WIP)**
- Width of middle bands
- Indicates current workload
- Shows if WIP limits are respected

**2. Cycle Time**
- Vertical distance between start and completion bands
- Average time from start to finish
- Measured at any point horizontally

**3. Throughput**
- Slope of the top band
- Rate items are completed
- Steeper = higher throughput

**4. Lead Time**
- Vertical distance from request to completion
- Total time in system
- Includes queue time

## Reading the Diagram

### Healthy CFD Patterns

**Smooth, parallel bands:**
- Stable workflow
- Consistent throughput
- Balanced WIP
- Predictable cycle time

**Steady upward slope:**
- Continuous delivery
- Items flowing through system
- Team making progress

### Problem Patterns

**Widening band:**
- WIP accumulation in that stage
- Potential bottleneck
- Need to investigate cause

**Flatline (horizontal band):**
- No progress
- Work stalled
- Immediate attention required

**Fluctuating bands:**
- Inconsistent workflow
- Variable capacity
- External interruptions

**Diverging bands:**
- Growing gap between stages
- Increasing cycle time
- System degradation

## Time Tracking Applications

### Individual Use

Track personal tasks through stages:
- Backlog
- Today's Work
- In Progress
- Completed

CFD reveals:
- How much you take on vs. complete
- Where you get stuck
- Your actual throughput
- Realistic capacity

### Team Management

Monitor team workflow:
- Identify bottlenecks
- Balance workload
- Predict completion dates
- Optimize process

### Project Tracking

Visualize project progress:
- See all work stages
- Identify delays early
- Communicate status visually
- Make data-driven decisions

## Practical Example

### Scenario: Software Development Team

**CFD shows:**
- "In Progress" band widening
- "Code Review" band thinning
- "Done" band flattening

**Diagnosis:**
- Too much concurrent work
- Insufficient review capacity
- Delivery slowdown

**Action:**
- Reduce WIP limits
- Allocate more review time
- Pair program to spread knowledge

**Result:**
- Bands stabilize
- Throughput increases
- Cycle time decreases

## Implementation

### Tools Supporting CFD

- **Jira**: Built-in CFD reports
- **Azure DevOps**: Analytics views
- **GitScrum**: Kanban optimization features
- **Trello + Power-Ups**: Via third-party add-ons
- **Asana**: Through custom reporting

### Manual Creation

1. Track items daily by stage
2. Record cumulative totals
3. Plot as stacked area chart
4. Review weekly for patterns

### Data Requirements

- Date item entered system
- Date moved between stages
- Date completed
- Current stage of active items

## Advanced Analysis

### Calculating Metrics from CFD

**Average Cycle Time:**
- Measure vertical distance
- Sample multiple points
- Calculate mean

**Throughput Rate:**
- Slope of completion band
- Items per unit time
- Trend over periods

**WIP Trends:**
- Band thickness over time
- Increasing or decreasing
- Correlation with cycle time

### Predictive Insights

**Monte Carlo Simulation:**
- Use historical cycle times
- Project completion dates
- Calculate probability ranges

**Capacity Planning:**
- Current throughput
- Backlog size
- Estimated time to clear

## Integration with Time Tracking

### Enhanced Reporting

Combine CFD with time data:
- Hours spent per stage
- Efficiency by workflow phase
- Resource allocation
- Cost per item

### Workflow Optimization

Identify where time is spent:
- Stage with longest duration
- Waiting time vs. active time
- Value-added vs. non-value-added
- Opportunities for automation

## Best Practices

### Regular Review

- Daily: Quick visual check
- Weekly: Detailed analysis
- Monthly: Trend identification
- Quarterly: Process improvement

### Team Discussion

Use CFD in meetings:
- Retrospectives
- Sprint planning
- Standup facilitation
- Stakeholder updates

### Continuous Improvement

1. Identify pattern
2. Hypothesize cause
3. Implement change
4. Observe CFD impact
5. Iterate

## Limitations

- Requires consistent workflow stages
- Needs regular data updates
- Can oversimplify complex processes
- Doesn't show individual item details
- Better for flow than for batch work

## Complementary Visualizations

- **Burndown charts**: Sprint progress
- **Control charts**: Process stability
- **Cycle time histogram**: Distribution
- **Throughput run chart**: Delivery rate over time

## Getting Started

1. Define your workflow stages (3-5 stages)
2. Choose tracking tool
3. Start collecting data
4. Generate CFD weekly
5. Learn to read patterns
6. Make small experiments
7. Measure improvements

## Return on Investment

Teams using CFD report:
- 20-30% faster delivery
- Earlier problem detection
- Better capacity prediction
- Improved team communication
- Data-driven decision making