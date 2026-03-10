## Overview

Story points are a relative estimation method in Agile that helps teams assess effort, complexity, and risk for backlog items. Unlike time-based estimates (hours or days), story points represent relative complexity, effort, and risk.

## What Are Story Points?

Story points consider:
- **Complexity**: How technically challenging is the work?
- **Risk**: What unknowns or dependencies exist?
- **Amount of work**: How much needs to be done?

Story points do NOT equal hours. A 5-point story isn't "5 hours of work."

## Why Use Story Points Instead of Hours?

### Benefits of Story Points:

1. **Team Collaboration**: Encourages team discussion and consensus
2. **Reduced Bias**: Less emotional attachment than hourly estimates
3. **Better Forecasting**: Improves accuracy over time
4. **Accounts for Uncertainty**: Better for complex, uncertain work
5. **Focuses on Value**: Emphasizes what's being delivered, not just time spent

Researchers have found that this improves estimate accuracy, especially on items with a lot of uncertainty as we find on most software projects.

## The Fibonacci Sequence

Story points typically use a modified Fibonacci sequence:
**1, 2, 3, 5, 8, 13, 20, 40, 100**

Why Fibonacci?
- Reflects uncertainty in larger estimates
- Larger gaps for larger items acknowledges less precision
- Forces meaningful distinctions
- Prevents false precision (no "4.5" story points)

### Scale Interpretation:

- **1-2**: Very small, simple tasks
- **3-5**: Small to medium complexity
- **8-13**: Medium to large complexity
- **20+**: Very large, should probably be broken down
- **100**: Epic/too large to estimate accurately

## Planning Poker

Planning Poker® is a consensus-based technique for agile estimating.

### How It Works:

1. **Present Item**: Team discusses a user story from the backlog
2. **Brief Discussion**: Clarify questions, discuss approach
3. **Private Estimation**: Each member mentally formulates an estimate
4. **Simultaneous Reveal**: Everyone holds up a card with their estimate
5. **Discuss Differences**: If estimates vary, discuss reasoning
6. **Re-estimate**: Repeat until consensus is reached

### Planning Poker Cards:

Cards display values like: **0, ½, 1, 2, 3, 5, 8, 13, 20, 40, 100, ?, ∞**

Special cards:
- **?** = "I don't understand" or "Need more information"
- **∞** (Infinity) = "Too large to estimate"
- **Coffee cup** = "Let's take a break"

### Why Planning Poker Works:

- Prevents anchoring bias (everyone estimates independently)
- Encourages discussion when estimates differ
- Surfaces hidden complexity or risks
- Builds team consensus
- Fast and efficient

## Velocity

Velocity is a metric that measures the amount of work a team can complete during a single sprint or iteration.

### Calculating Velocity:

Velocity = Sum of story points of all **completed** user stories in a sprint

**Example:**
- Sprint 1: 23 points completed
- Sprint 2: 27 points completed
- Sprint 3: 25 points completed
- **Average Velocity**: 25 points per sprint

### Using Velocity for Planning:

Once you know your velocity:
- Forecast how much work fits in upcoming sprints
- Predict project completion dates
- Identify if you're taking on too much work
- Track if changes improve or hurt productivity

### Velocity Rules:

1. **Only Count Completed Work**: Partially done doesn't count
2. **Use Team-Specific Velocity**: Don't compare across teams
3. **Wait 3-5 Sprints**: Velocity stabilizes after a few sprints
4. **Account for Variations**: Use average, not just last sprint
5. **Velocity is a Guide**: Not a commitment or performance metric

## Implementation Steps

### Step 1: Establish a Baseline

Pick a reference story that the whole team understands. Assign it a number (often 3 or 5). Estimate other stories relative to this baseline.

### Step 2: Estimate as a Team

Use Planning Poker or similar technique. Ensure whole team participates.

### Step 3: Track Actuals

Record which stories were completed each sprint and their point values.

### Step 4: Calculate Velocity

After 3-5 sprints, calculate average velocity.

### Step 5: Use for Planning

Plan future sprints based on your established velocity.

### Step 6: Refine Over Time

Adjust estimates based on what you learn. Velocity should stabilize and become more predictable.

## Common Pitfalls

### 1. Treating Points as Hours

Story points are NOT time. Don't convert them to hours.

### 2. Comparing Team Velocities

One team's 50 points ≠ another team's 50 points. Story points are team-specific.

### 3. Using Velocity as Performance Metric

Velocity is for planning, not judging team performance. Pressuring teams to increase velocity leads to point inflation.

### 4. Estimating Too Precisely

Don't argue whether something is 7 vs. 8 points. Use Fibonacci gaps to avoid false precision.

### 5. Incomplete Stories

Only completed stories count toward velocity. Don't count partially done work.

### 6. Changing Point Values After Sprint Starts

Once sprint starts, don't re-estimate. Learn for next time.

## Benefits

- More accurate long-term forecasting
- Improved sprint planning
- Better team collaboration
- Reduced estimation time
- Accounts for uncertainty
- Focuses on value delivery
- Predictable delivery cadence
- Improved stakeholder communication

## Best Practices

### Estimating:

- Estimate as a full team
- Use Planning Poker or similar technique
- Discuss reasoning, especially for outliers
- Break down stories larger than 13-20 points
- Re-estimate only when new information emerges

### Tracking Velocity:

- Calculate after each sprint
- Use rolling average (last 3-5 sprints)
- Chart velocity over time
- Investigate significant variations
- Don't game the system

### Planning:

- Use velocity as a guide, not a rule
- Include buffer for unknowns
- Adjust for team changes or vacation
- Communicate uncertainty to stakeholders

## Tools Supporting Story Points

- Jira
- Azure DevOps
- Rally
- VersionOne
- Trello (with plugins)
- Planning Poker online tools
- Physical Planning Poker cards

## Integration with Time Tracking

While story points avoid time estimates:
- Track actual hours spent per story
- Compare to story point estimates
- Identify patterns (e.g., "8-point stories average 2 days")
- Don't use for commitment, but for team learning

## Who Benefits Most

- Agile/Scrum teams
- Software development teams
- Teams with uncertain or complex work
- Cross-functional teams
- Teams seeking predictable delivery
- Product owners needing roadmap forecasts

## Related Concepts

- **T-Shirt Sizing**: XS, S, M, L, XL as alternative to numbers
- **Ideal Days**: Another relative estimation method
- **#NoEstimates**: Movement advocating for no estimates
- **Monte Carlo Simulation**: Using velocity data for probability forecasts