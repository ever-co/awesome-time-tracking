## Overview

The Program Evaluation and Review Technique (PERT) is used to find the estimated time for activities to be completed when there are many unknown factors. PERT was originally developed by the U.S. Navy in the 1950s to support the Polaris submarine project.

Instead of assuming a single fixed value, this method uses optimistic, most likely, and pessimistic estimates to reflect a full range of potential scenarios for each task or activity.

## The Three Estimates

The three-point estimation technique involves three values:

### 1. Optimistic (O)

This is the "happy path" where everything goes right and the task takes the minimum amount of time that it could take.

**Characteristics:**
- Best-case scenario
- All conditions favorable
- No obstacles or delays
- Team performing at peak
- All resources immediately available

### 2. Most Likely (M)

This is the best guess that you have, if all proceeds somewhat normally and there are a few bumps in the road, the task will take this long.

**Characteristics:**
- Realistic middle ground
- Normal working conditions
- Expected minor issues
- Typical resource availability
- Standard team performance

### 3. Pessimistic (P)

The worst-case scenario where delays, risks, or issues result in higher time or cost.

**Characteristics:**
- Everything that can go wrong does
- Maximum delays and obstacles
- Resource constraints
- Technical difficulties
- External dependencies fail

## PERT Formula

**Expected Time = (Optimistic + 4 × Most Likely + Pessimistic) / 6**

Or: **(O + 4M + P) / 6**

### Why Weight the Most Likely by 4?

The M value, Most Likely, is given 4 weights as the PERT formula is based on probability theory and statistics, specifically Beta Distribution. This weighting reflects that the most likely scenario is more probable than the extremes.

## Example Calculation

**Task:** Develop a new feature

- **Optimistic (O)**: 3 days
- **Most Likely (M)**: 5 days  
- **Pessimistic (P)**: 10 days

**Expected Time** = (3 + 4(5) + 10) / 6 = (3 + 20 + 10) / 6 = 33 / 6 = **5.5 days**

## Standard Deviation

PERT also allows calculation of standard deviation:

**Standard Deviation = (P - O) / 6**

In our example: (10 - 3) / 6 = 7 / 6 = **1.17 days**

This tells you the likely variance from the expected time.

## PERT vs. Triangular Distribution

### PERT Distribution:

- More bell-shaped curve
- Higher peak at most likely estimate
- Assumes values closer to most likely are more probable
- Uses weighted formula
- Better for complex tasks with uncertainty

### Triangular Distribution:

- Simple average of three points
- Formula: (O + M + P) / 3
- All three values weighted equally
- Simpler to calculate
- Better for tasks with limited historical data

## Key Benefits

### 1. More Realistic Estimates

By considering multiple scenarios, estimates are less prone to bias and provide a realistic average.

### 2. Risk Visibility

The process forces teams to identify optimistic and pessimistic outcomes, making hidden risks visible.

### 3. Stakeholder Trust

Presenting a range of values builds trust and helps stakeholders understand variability.

### 4. Better Planning

Understanding potential variance helps with buffer planning and resource allocation.

### 5. Accounts for Uncertainty

Recognizes that not all tasks have predictable durations.

## When to Use PERT

The technique is widely used in project management, particularly for:

- Complex, high-risk tasks
- High-cost activities
- Tasks where historical data is limited
- Projects where risk is a major concern
- Novel or innovative work
- Tasks with significant uncertainty
- Critical path activities

## How to Implement

### Step 1: Identify Tasks

List all project tasks requiring estimation.

### Step 2: Gather Input

For each task, ask:
- "What's the best-case duration?" (O)
- "What's the most realistic duration?" (M)
- "What's the worst-case duration?" (P)

### Step 3: Calculate Expected Time

Apply the PERT formula: (O + 4M + P) / 6

### Step 4: Calculate Standard Deviation (Optional)

Use: (P - O) / 6 to understand variance

### Step 5: Sum for Project Duration

Add expected times for all tasks on critical path.

### Step 6: Include Buffers

Consider adding buffer time based on standard deviations.

## Best Practices

### Involve the Right People

- Get estimates from those doing the work
- Include subject matter experts
- Consider multiple perspectives
- Avoid estimating in isolation

### Be Realistic

- Optimistic doesn't mean "impossible but theoretically possible"
- Pessimistic isn't "the project fails entirely"
- Most likely should be genuinely likely, not aspirational

### Document Assumptions

- Record what each estimate assumes
- Note dependencies and constraints
- Document risk factors considered
- Explain pessimistic scenarios

### Review and Refine

- Update estimates as you learn more
- Compare actuals to estimates
- Improve estimation accuracy over time
- Track which assumptions held true

## Common Pitfalls

### 1. Overly Optimistic "Optimistic"

Avoid best-case estimates that assume perfection. Be realistic about what "best case" means.

### 2. Ignoring Pessimistic Scenarios

Don't dismiss worst-case estimates as "too negative." They're essential for risk planning.

### 3. Single Person Estimating

Estimates from one person are prone to bias. Get team input.

### 4. Not Updating Estimates

As projects progress, update estimates based on actual performance.

### 5. Confusing PERT with Fixed Commitment

PERT provides expected duration, not a guarantee.

## Integration with Project Management

### Critical Path Method (CPM)

Combine PERT estimates with CPM to identify:
- Critical path duration
- Project completion probability
- Buffer requirements
- Risk hotspots

### Risk Management

Use pessimistic estimates to:
- Identify high-risk activities
- Plan mitigation strategies
- Allocate contingency budgets
- Prioritize risk monitoring

### Resource Planning

Expected times help:
- Allocate resources realistically
- Identify resource conflicts
- Plan for variable durations
- Optimize resource utilization

## Tools Supporting PERT

- Microsoft Project
- Primavera P6
- Smartsheet
- Project Management calculators
- Custom Excel templates
- Online PERT calculators

## Measuring Success

- Estimates closer to actuals over time
- Better risk identification
- Fewer schedule surprises
- Improved stakeholder communication
- More accurate project forecasts

## Related Techniques

- **Monte Carlo Simulation**: Uses PERT data for probabilistic analysis
- **Delphi Technique**: Consensus-based estimation method
- **Analogous Estimating**: Based on similar past projects
- **Parametric Estimating**: Using statistical relationships