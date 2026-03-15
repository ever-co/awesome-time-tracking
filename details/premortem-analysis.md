## Overview

A premortem is a managerial strategy where a team imagines that a project has failed and then works backward to determine what potentially could have led to the failure. This technique helps combat optimism bias and the planning fallacy in project planning.

## How It Works

### Step 1: Assume Failure
Imagine it's 6-12 months in the future and your project has completely failed.

### Step 2: Write the Story
Individually, team members write down all the reasons why the project failed.

### Step 3: Share and Compile
Go around the room having each person share one reason at a time until all reasons are captured.

### Step 4: Prioritize Risks
Rank the identified risks by likelihood and potential impact.

### Step 5: Mitigate
For the highest-priority risks, develop specific mitigation strategies.

## Benefits for Time Estimation

### Surface Hidden Risks
Team members feel psychologically safe sharing concerns they might otherwise suppress.

### Identify Time Sinks
Many identified failure reasons relate to time: scope creep, technical debt, dependencies, etc.

### Adjust Estimates
Once risks are explicit, can add appropriate buffer time to estimates.

### Prevent Problems
Proactive mitigation prevents delays before they occur.

## Connection to Planning Fallacy

The planning fallacy causes teams to:
- Focus on best-case scenarios
- Ignore potential obstacles
- Underestimate time required

Premortem directly counters this by:
- Explicitly considering worst-case scenarios
- Surfacing specific obstacles
- Informing realistic time estimates

## Example Application

### Project: Launch New Feature

**Premortem Failure Reasons Identified:**
1. API integration took 3x longer than estimated
2. Key developer left mid-project
3. Requirements changed after development started
4. QA found critical bugs late in process
5. Dependency on another team's timeline
6. Underestimated time for documentation
7. Customer feedback required major redesign

**Impact on Time Estimate:**
- Original estimate: 6 weeks
- After premortem: 10 weeks
- Actual time: 9.5 weeks

## Implementation Tips

### Do It Early
Conduct premortem after planning but before execution begins.

### Psychological Safety
Emphasize this is about surfacing risks, not assigning blame.

### Be Specific
Vague concerns ("delays happen") are less useful than specific scenarios ("API vendor has 2-week response time for support tickets").

### Document Everything
Capture all identified risks for reference during the project.

### Revisit Periodically
Update risk assessment as project progresses.

## Comparison to Retrospectives

### Retrospective (Postmortem)
- Happens after project completion
- Identifies what went wrong
- Helps future projects
- Too late to help current project

### Premortem
- Happens before project execution
- Identifies what could go wrong
- Helps current project
- Prevents problems proactively

## Research Basis

Developed by psychologist Gary Klein, based on research into decision-making and prospective hindsight (imagining an event has occurred increases perceived likelihood of causes).

## Integration with Time Tracking

### Track Predicted vs. Actual Risks
Record which premortem risks actually occurred and their time impact.

### Build Better Estimates
Use historical premortem accuracy to refine future risk identification.

### Validate Time Allocation
Check if time budgeted for risk mitigation was sufficient.

## Common Premortem Findings

### Technical Risks
- Underestimated complexity
- Third-party integration issues
- Technical debt slowing development
- Learning curve for new technologies

### Process Risks
- Unclear requirements
- Too many stakeholders
- Approval delays
- Scope creep

### Resource Risks
- Key person unavailable
- Competing priorities
- External dependencies
- Budget constraints affecting timeline

### Communication Risks
- Assumptions not validated
- Feedback loops too slow
- Requirements changes not managed
- Stakeholder expectations misaligned