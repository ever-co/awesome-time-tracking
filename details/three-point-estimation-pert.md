## Overview

Three-Point Estimation, also called PERT (Program Evaluation and Review Technique) estimation, is a method for estimating task duration using three scenarios to account for uncertainty and provide more realistic project timelines.

## The Three Estimates

### Optimistic (O)
**Definition**: Best-case scenario time
**Assumptions**:
- Everything goes perfectly
- No obstacles or delays
- Ideal conditions
- Maximum efficiency

**Question**: "What's the fastest this could possibly be done?"

### Most Likely (M)
**Definition**: Realistic scenario time
**Assumptions**:
- Normal working conditions
- Expected challenges accounted for
- Based on experience
- Most probable outcome

**Question**: "Given normal conditions, how long will this take?"

### Pessimistic (P)
**Definition**: Worst-case scenario time
**Assumptions**:
- Significant obstacles encountered
- Multiple setbacks
- Unfavorable conditions
- Still completable (not catastrophic)

**Question**: "If things go badly, what's the maximum reasonable time?"

## Calculation Methods

### Triangular Distribution
**Formula**: (O + M + P) / 3

**When to Use**:
- Equal weight to all three estimates
- Simpler calculation
- Less historical data available

**Example**:
- Optimistic: 4 days
- Most Likely: 6 days
- Pessimistic: 10 days
- **Estimate**: (4 + 6 + 10) / 3 = 6.67 days

### Beta Distribution (PERT Formula)
**Formula**: (O + 4M + P) / 6

**When to Use**:
- Weight most likely estimate more heavily
- More accurate with experienced estimators
- Industry standard for project management

**Example**:
- Optimistic: 4 days
- Most Likely: 6 days  
- Pessimistic: 10 days
- **Estimate**: (4 + 4×6 + 10) / 6 = 6.33 days

### Standard Deviation
**Formula**: (P - O) / 6

**Purpose**: Measures uncertainty
- Higher SD = more uncertainty
- Lower SD = more confidence
- Helps assess risk

**Confidence Intervals**:
- 68% confidence: Estimate ± 1 SD
- 95% confidence: Estimate ± 2 SD
- 99.7% confidence: Estimate ± 3 SD

## Benefits

### More Realistic Estimates
- Accounts for uncertainty
- Balances optimism and pessimism
- Based on range rather than single point
- Reflects real-world variability

### Risk Assessment
- Standard deviation shows uncertainty level
- Identifies high-risk tasks
- Supports contingency planning
- Improves decision-making

### Better Than Single-Point
- Single estimates tend toward optimism
- Doesn't account for unknowns
- Three-point captures range of outcomes
- More defendable to stakeholders

## How to Apply

### Step 1: Break Down Work
- Divide project into tasks
- Make tasks estimable (not too large)
- Identify dependencies

### Step 2: Gather Team Input
- Involve people who'll do the work
- Discuss assumptions
- Consider historical data
- Account for known risks

### Step 3: Create Three Estimates

For each task:
1. **Optimistic**: What if everything goes right?
2. **Most Likely**: What's our realistic estimate?
3. **Pessimistic**: What if we hit obstacles?

### Step 4: Calculate
- Apply formula (usually PERT: (O+4M+P)/6)
- Calculate standard deviation
- Sum estimates for total project time
- Add buffer based on uncertainty

### Step 5: Review and Refine
- Sanity check results
- Compare to historical projects
- Adjust for unique factors
- Get team buy-in

## Common Mistakes

### Too Optimistic Across Board
- All three estimates are optimistic
- Doesn't truly represent worst case
- Solution: Challenge assumptions

### Pessimistic = Catastrophic
- Worst case includes disasters
- Not realistic for planning
- Solution: Pessimistic should be bad but plausible

### Anchor Bias
- First estimate influences others
- All three cluster too closely
- Solution: Estimate independently or use ranges

### Forgetting Dependencies
- Estimates assume parallel work
- Ignore sequential constraints
- Solution: Consider critical path

## Use in Agile

### Story Point Estimation
Can use three-point for complexity:
- Optimistic: 3 points
- Most Likely: 5 points
- Pessimistic: 8 points
- Weighted estimate: ~5 points

### Sprint Planning
- Estimate capacity with three scenarios
- Plan for most likely
- Understand risk with pessimistic

### Release Planning
- Project completion dates
- Account for velocity variance
- Communicate uncertainty to stakeholders

## Tools and Techniques

### Planning Poker Variant
1. Team estimates optimistic
2. Team estimates most likely
3. Team estimates pessimistic
4. Calculate using PERT formula

### Monte Carlo Simulation
- Run thousands of simulations
- Use three-point estimates as inputs
- Generate probability distributions
- More sophisticated analysis

## When to Use

**Good For**:
- Complex, uncertain projects
- High-stakes deliverables
- Projects with significant unknowns
- First-time initiatives
- Communicating risk to stakeholders

**Less Useful For**:
- Routine, well-understood tasks
- Very short tasks (overhead not worth it)
- When single estimate is accurate enough

## Ideal For

- Project managers
- Agile teams doing estimation
- Anyone planning complex work
- Organizations needing realistic timelines
- Teams learning to estimate better