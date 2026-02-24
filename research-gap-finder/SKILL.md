---
name: research-gap-finder
description: Identify research gaps and generate novel research ideas from literature analysis. Use when the user wants to find unexplored research opportunities, generate hypotheses, brainstorm new approaches, or validate research ideas. Triggers: "find research gaps", "generate research ideas", "what's missing", "new research direction", "hypothesis generation", "research opportunities", "novel ideas".
---

# Research Gap Finder & Idea Generator

A systematic framework for identifying research gaps and generating novel research ideas.

## Gap Identification Framework

### 1. Explicit Gaps (Authors state)

Look for these signals in papers:

```markdown
## Explicit Limitations Section
[Direct quotes from papers' limitations/future work sections]

### Paper 1: [Title]
**Stated limitations**:
- "We did not address..."
- "Future work should explore..."
- "Our approach is limited by..."

**Gap identified**: [Clear statement of gap]

### Paper 2: [Title]
...
```

### 2. Implicit Gaps (Analysis reveals)

#### Methodological Gaps

```markdown
## Methodological Gaps

### Gap 1: Limited Evaluation Scope
**Observation**: Most papers test on [specific datasets]
**Missing**: Evaluation on [other types of data]
**Impact**: Generalizability unknown
**Opportunity**: Systematic evaluation across diverse domains

### Gap 2: Simplified Assumptions
**Observation**: Papers assume [specific condition]
**Reality**: Real-world scenarios involve [complex condition]
**Gap**: Methods may fail in realistic settings
**Opportunity**: Develop robust methods for complex scenarios

### Gap 3: Missing Baselines
**Observation**: Papers don't compare against [relevant method]
**Gap**: Unclear if new method is truly better
**Opportunity**: Comprehensive benchmarking study
```

#### Theoretical Gaps

```markdown
## Theoretical Gaps

### Gap 1: Lack of Theoretical Understanding
**Observation**: Methods work empirically but theoretical foundation unclear
**Gap**: No theory explaining when/why methods succeed/fail
**Opportunity**: Develop theoretical framework

### Gap 2: Disjointed Theory
**Observation**: Multiple theoretical frameworks don't connect
**Gap**: No unified theory
**Opportunity**: Unifying theoretical framework

### Gap 3: Unexplored Phenomena
**Observation**: Empirical phenomena observed but not explained
**Gap**: Mechanism behind phenomenon unknown
**Opportunity**: Investigation and explanation
```

#### Empirical Gaps

```markdown
## Empirical Gaps

### Gap 1: Limited Scale
**Observation**: Studies conducted at small scale
**Gap**: Behavior at scale unknown
**Opportunity**: Large-scale empirical study

### Gap 2: Missing Contexts
**Observation**: Research in [context A] but not [context B]
**Gap**: Unknown if findings generalize
**Opportunity**: Cross-context validation

### Gap 3: Long-term Effects
**Observation**: Short-term evaluations only
**Gap**: Long-term effects unknown
**Opportunity**: Longitudinal study
```

### 3. Cross-Paper Gap Analysis

```markdown
## Cross-Paper Analysis

### Contradictory Findings
**Paper A** claims: [Finding X]
**Paper B** claims: [Finding Y, opposite of X]
**Gap**: Resolution of contradiction needed
**Opportunity**: Systematic study to reconcile findings

### Complementary Findings
**Paper A** addresses: [Aspect 1]
**Paper B** addresses: [Aspect 2]
**Gap**: No work combines both aspects
**Opportunity**: Unified approach

### Incremental vs Revolutionary
**Pattern**: Recent papers show incremental improvements
**Gap**: No breakthrough approaches
**Opportunity**: Paradigm shift
```

## Research Idea Generation

### 1. Combination Approach

```markdown
## Idea: Combine [Method A] + [Method B]

**Source 1**: [Paper with Method A]
**Source 2**: [Paper with Method B]

**Core Idea**: Combine strengths of both approaches
- Method A strength: [What it does well]
- Method B strength: [What it does well]
- Combined potential: [Synergy]

**Hypothesis**: [Testable prediction]

**Approach**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Novelty**: [Why this hasn't been done]
**Feasibility**: [Assessment of difficulty]
**Impact**: [Potential significance]
```

### 2. Extension Approach

```markdown
## Idea: Extend [Existing Work] to [New Context]

**Base Work**: [Paper/approach]
**New Context**: [Different domain/problem]

**Motivation**: [Why this extension matters]

**Challenges**:
- [Challenge 1] → [Solution approach]
- [Challenge 2] → [Solution approach]

**Expected Contribution**: [What would be new]
```

### 3. Opposition Approach

```markdown
## Idea: Challenge [Common Assumption]

**Prevailing View**: [What most papers assume]
**My Hypothesis**: [Alternative view]

**Evidence for Challenge**:
- [Observation 1]
- [Observation 2]

**Proposed Investigation**:
[How to test the alternative]

**Potential Impact**: [If assumption is wrong]
```

### 4. Transfer Approach

```markdown
## Idea: Apply [Technique from Field A] to [Field B]

**Source Field**: [Field A with technique]
**Target Field**: [Field B with problem]

**Why It Might Work**:
- [Analogy between problems]
- [Similar structure]

**Adaptation Required**:
- [Modification 1]
- [Modification 2]

**Validation Strategy**: [How to test]
```

## Research Idea Evaluation

### ICE Framework

Score each idea on:

```markdown
## Idea Evaluation: [Idea Name]

**Impact** (1-10): [Score]
- Potential to advance field: [Justification]
- Practical significance: [Justification]

**Confidence** (1-10): [Score]
- Theoretical grounding: [Justification]
- Preliminary evidence: [Justification]

**Ease** (1-10): [Score]
- Resource requirements: [Justification]
- Technical feasibility: [Justification]
- Time to results: [Justification]

**Total ICE Score**: [Impact + Confidence + Ease] / 3 = [Average]

**Decision**: [Pursue/Explore more/Discard]
```

### Risk-Return Matrix

```markdown
## Portfolio Analysis

| Idea | Risk | Return | Category |
|------|------|--------|----------|
| Idea 1 | Low | High | Quick win |
| Idea 2 | High | High | Moonshot |
| Idea 3 | Low | Low | Incremental |
| Idea 4 | High | Low | Avoid |

**Recommended Mix**: [Which to pursue]
```

## Idea Development Process

### Stage 1: Idea Collection
- Collect all potential gaps and ideas
- No filtering at this stage
- Document source of inspiration

### Stage 2: Initial Screening
- Quick ICE scoring
- Eliminate obviously poor fits
- Group related ideas

### Stage 3: Deep Dive
- Top ideas get detailed analysis
- Literature search for related work
- Feasibility assessment

### Stage 4: Refinement
- Clarify research questions
- Define methodology
- Identify needed resources

### Stage 5: Validation
- Discuss with peers
- Preliminary experiments if possible
- Revise based on feedback

## Output Templates

### Research Opportunities Report

```markdown
# Research Opportunities in [Field]

## Executive Summary
- **Gaps identified**: [N]
- **High-priority ideas**: [N]
- **Quick wins**: [N]
- **Long-term opportunities**: [N]

## Top 5 Research Gaps

### 1. [Gap Name] ⭐ HIGH PRIORITY
**Description**: [Clear statement]
**Evidence**: [From papers]
**Why It Matters**: [Significance]
**Feasibility**: [Assessment]
**Potential Impact**: [High/Medium/Low]

### 2. [Gap Name]
...

## Top 5 Research Ideas

### Idea 1: [Title] ⭐ RECOMMENDED
**Concept**: [Brief description]
**Novelty**: [What's new]
**Approach**: [High-level method]
**Expected Outcome**: [What success looks like]
**Resources Needed**: [Equipment/data/expertise]
**Timeline**: [Estimate]
**Risk Level**: [Low/Medium/High]

### Idea 2: [Title]
...

## Gap Categorization

### By Type
- Theoretical: [N]
- Methodological: [N]
- Empirical: [N]
- Practical: [N]

### By Difficulty
- Easy (6 months): [N]
- Medium (1-2 years): [N]
- Hard (2+ years): [N]

### By Impact Potential
- Transformative: [N]
- Significant: [N]
- Incremental: [N]

## Research Roadmap

### Immediate Actions (Next 3 months)
1. [Specific action]
2. [Specific action]

### Short-term Goals (6-12 months)
1. [Goal]
2. [Goal]

### Long-term Vision (1-2 years)
1. [Vision]
2. [Vision]

## Recommended Next Steps

### For Quick Win
[Idea name + specific first steps]

### For High Impact
[Idea name + resource needs]

### For Building Skills
[Idea name + learning path]

## Risk Assessment

### Technical Risks
- [Risk and mitigation]

### Resource Risks
- [Risk and mitigation]

### Competition Risks
- [Who else might work on this]
```

### Single Idea Proposal

```markdown
# Research Proposal: [Title]

## Problem & Motivation
[Clear problem statement with evidence]

## Research Question
[Specific, answerable question]

## Hypothesis
[Testable prediction]

## Related Work
[How this differs from existing work]

## Methodology
[Approach to answering the question]

## Expected Contributions
1. [Theoretical contribution]
2. [Methodological contribution]
3. [Empirical contribution]

## Success Criteria
[How to know if it worked]

## Timeline & Milestones
| Month | Milestone |
|-------|-----------|
| 1 | |
| 3 | |
| 6 | |

## Resource Requirements
- Data: [What data needed]
- Compute: [Computational requirements]
- Collaboration: [Expertise needed]

## Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| | | | |
```

## Techniques for Creative Ideation

### 1. Constraint Removal
"What if [current limitation] wasn't a problem?"

### 2. Analogy Thinking
"How does [different field] solve similar problems?"

### 3. First Principles
"What are the fundamental truths in this area?"

### 4. Inversion
"What would definitely NOT work?" → Avoid those

### 5. Exaggeration
"What if we made [aspect] 10x bigger/smaller/faster?"

### 6. Cross-Pollination
"What if we applied [concept from unrelated field]?"

### 7. Question Assumptions
"What does everyone believe that might be wrong?"

### 8. Edge Case Focus
"What happens at the extreme boundaries?"

## Validation Checklist

Before pursuing an idea, verify:

- [ ] **Novelty**: Literature search confirms gap exists
- [ ] **Significance**: Problem is worth solving
- [ ] **Feasibility**: Can be addressed with available resources
- [ ] **Interest**: You personally find it engaging
- [ ] **Timeline**: Achievable in reasonable timeframe
- [ ] **Skills**: You have or can acquire needed expertise
- [ ] **Collaboration**: Potential advisors/collaborators available
- [ ] **Publishing**: Suitable venues exist for results
