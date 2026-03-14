## Overview

Three-Point Estimation is a time and cost estimation technique that considers uncertainty and risk by using three estimates: optimistic, most likely, and pessimistic. This approach provides a more realistic and reliable estimate than single-point estimates.

## The Three Estimates

1. **Optimistic (O)**: Best-case scenario where everything goes perfectly
2. **Most Likely (M)**: Realistic scenario based on normal conditions
3. **Pessimistic (P)**: Worst-case scenario accounting for major issues

## Calculation Methods

### Triangular Distribution
**Expected Time = (O + M + P) / 3**

Simple average of the three estimates, giving equal weight to all scenarios.

### PERT (Beta Distribution)
**Expected Time = (O + 4M + P) / 6**

Weighted average that gives more weight to the most likely scenario, commonly used in project management.

### Standard Deviation
**SD = (P - O) / 6**

Measures the uncertainty or risk in the estimate.

## Step-by-Step Process

1. Identify the task or activity to estimate
2. Determine the optimistic estimate (best case)
3. Determine the most likely estimate (realistic case)
4. Determine the pessimistic estimate (worst case)
5. Apply the appropriate formula (Triangular or PERT)
6. Calculate standard deviation to understand risk level
7. Use the expected time for planning

## Advantages

- **Risk Awareness**: Accounts for uncertainty and variability
- **Realistic Estimates**: Reduces overly optimistic planning
- **Confidence Levels**: Standard deviation indicates estimate reliability
- **Better Communication**: Helps stakeholders understand potential variance
- **Improved Planning**: Supports buffer time allocation
- **Data-Driven**: Based on analysis rather than gut feeling

## Disadvantages

- More time-consuming than single-point estimates
- Requires experience to provide accurate three estimates
- Can still be subjective if not based on data
- May give false confidence if estimates are poorly chosen

## Best Practices

- Base estimates on historical data when available
- Involve team members with relevant experience
- Document assumptions for each estimate
- Consider external factors and dependencies
- Review and refine estimates as project progresses
- Use pessimistic estimates to identify risk areas
- Combine with other estimation techniques for validation

## Common Use Cases

- Software development sprints and releases
- Construction project scheduling
- Product development timelines
- Service delivery planning
- Resource allocation in uncertain environments

## Example

Task: Develop a new feature
- Optimistic: 5 days (everything goes smoothly)
- Most Likely: 8 days (normal development with minor issues)
- Pessimistic: 15 days (significant technical challenges)

PERT Estimate = (5 + 4×8 + 15) / 6 = 52 / 6 = 8.67 days

Standard Deviation = (15 - 5) / 6 = 1.67 days

This indicates an expected duration of about 9 days with moderate uncertainty.