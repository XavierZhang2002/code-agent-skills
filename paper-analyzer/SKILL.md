---
name: paper-analyzer
description: Deep analysis of academic papers to extract key insights, methodology, contributions, and limitations. Use when the user wants to understand a paper in depth, critique research methodology, compare approaches, or extract actionable insights. Triggers: "analyze this paper", "deep dive into", "critique", "methodology analysis", "what are the limitations", "compare approaches", "key insights".
---

# Paper Deep Analyzer

A systematic framework for comprehensive analysis of academic papers.

## Analysis Framework

### Phase 1: Structural Overview

First, understand the paper's architecture:

1. **Paper Metadata**
   - Title, authors, affiliations
   - Publication venue and date
   - Citations (if available)
   - Paper type: theoretical, empirical, survey, position paper

2. **Core Structure**
   - Abstract summary
   - Research questions/hypotheses
   - Key claims and contributions
   - Organization of sections

### Phase 2: Content Analysis

#### 2.1 Problem & Motivation

Analyze the research problem:

```markdown
## Problem Analysis

**Stated Problem**: [What problem does the paper address?]

**Problem Significance**: [Why is this problem important?]

**Target Domain**: [Where does this problem manifest?]

**Current Limitations**: [What existing approaches fail to address?]

**User Pain Points**: [Who benefits from solving this?]
```

#### 2.2 Methodology Analysis

Deep dive into the approach:

```markdown
## Methodology Analysis

**Approach Category**: 
- [ ] Theoretical/Analytical
- [ ] Experimental
- [ ] Empirical/observational
- [ ] System implementation
- [ ] Survey/Review
- [ ] Position/Argumentative

**Core Methods**:
1. [Method 1 with technical details]
2. [Method 2 with technical details]
3. [Method 3 with technical details]

**Technical Innovations**:
- Novel techniques introduced
- Modifications to existing methods
- New theoretical frameworks

**Experimental Design** (if applicable):
- Datasets used
- Evaluation metrics
- Baselines compared
- Experimental setup
- Statistical methods

**Reproducibility Assessment**:
- Code availability: [Yes/No/Partial]
- Data availability: [Yes/No/Partial]
- Hyperparameters specified: [Yes/No]
- Random seeds reported: [Yes/No]
```

#### 2.3 Results & Findings

Analyze outcomes:

```markdown
## Results Analysis

**Main Findings**:
1. [Primary result with quantitative evidence]
2. [Secondary finding]
3. [Unexpected or negative results]

**Performance Claims**:
- Claimed improvement: [X% over baseline Y]
- Significance: [Statistical significance if reported]
- Effect size: [Practical significance]

**Scope of Evaluation**:
- Number of datasets/experiments
- Diversity of test cases
- Generalizability evidence
```

#### 2.4 Critical Analysis

Identify strengths and weaknesses:

```markdown
## Critical Assessment

### Strengths
1. [Methodological strength]
2. [Novel contribution]
3. [Rigorous evaluation]
4. [Clear presentation]

### Weaknesses & Limitations
1. **Limitation**: [Description]
   - **Severity**: [Critical/Major/Minor]
   - **Impact**: [How it affects conclusions]
   - **Evidence**: [Specific location in paper]

2. **Limitation**: [Description]
   ...

### Methodological Concerns
- [Potential biases]
- [Threats to validity]
- [Confounding factors]
- [Sample size issues]

### Alternative Interpretations
- [Different ways to interpret the results]
- [Missing control conditions]
- [Alternative explanations not considered]
```

### Phase 3: Contextual Analysis

#### 3.1 Literature Positioning

```markdown
## Position in Literature

**Related Work Coverage**:
- Key prior works cited
- Gaps in literature review
- Positioning relative to existing work

**Novelty Assessment**:
- Incremental improvement vs breakthrough
- Theoretical vs practical contribution
- Scope of innovation

**Citation Analysis** (if data available):
- Key papers this work builds on
- Potential influence on future work
```

#### 3.2 Impact Assessment

```markdown
## Impact & Significance

**Academic Impact**:
- Contribution to theory
- Methodological advancement
- Opens new research directions

**Practical Impact**:
- Real-world applicability
- Industry relevance
- Implementation feasibility

**Time Sensitivity**:
- Urgency of the problem
- Competition in research area
- Window of relevance
```

### Phase 4: Synthesis & Insights

#### 4.1 Key Takeaways

```markdown
## Executive Summary

**For Researchers**:
- Core insight: [Key theoretical/practical insight]
- Method to adopt: [Promising technique]
- Caution about: [Potential pitfalls]

**For Practitioners**:
- When to use: [Applicable scenarios]
- Expected outcomes: [Realistic expectations]
- Implementation notes: [Practical considerations]

**For Reviewers**:
- Quality score: [Accept/Minor/Major/Reject]
- Key concerns: [Main issues to address]
- Strengths to highlight: [Notable contributions]
```

#### 4.2 Future Work Identification

```markdown
## Extensions & Future Work

**Immediate Extensions**:
1. [Short-term follow-up work]
2. [Natural next steps]

**Long-term Directions**:
1. [Major research program]
2. [ paradigm shifts suggested]

**Open Questions**:
1. [Unanswered questions]
2. [Promising but unexplored directions]
```

## Special Analysis Modes

### Comparative Analysis (Multiple Papers)

When analyzing multiple papers:

```markdown
## Comparative Analysis

### Comparison Matrix
| Aspect | Paper A | Paper B | Paper C |
|--------|---------|---------|---------|
| Method | | | |
| Dataset | | | |
| Performance | | | |
| Strength | | | |
| Weakness | | | |

### Evolution Analysis
[How approaches evolved over time]

### Consensus & Controversy
[Areas of agreement and disagreement]

### Best Practice Identification
[Emerging standards from the literature]
```

### Gap Analysis Mode

```markdown
## Research Gap Analysis

### Explicit Gaps (Authors acknowledge)
1. [Limitation 1]
2. [Limitation 2]

### Implicit Gaps (Analysis reveals)
1. [Unaddressed aspect]
2. [Weak experimental design]
3. [Missing comparison]

### Opportunity Identification
1. [High-value research opportunity]
2. [Underserved problem variant]
3. [Methodological improvement potential]
```

## Output Format

Always provide analysis in this structure:

```markdown
# Paper Analysis: [Title]

## Quick Reference
- **Authors**: 
- **Venue**: 
- **Year**: 
- **Type**: 
- **Quality Score**: [A/B/C/D]
- **Recommendation**: [Must-read/Worth-reading/Skip]

## 1-Minute Summary
[3-5 sentence executive summary]

## Key Contributions
[Numbered list of main contributions]

## Critical Insights
[Most important takeaways]

## Limitations & Concerns
[Key weaknesses]

## Practical Takeaways
[Actionable insights]

## Related Papers
[Papers to read next]
```

## Quality Rubric

When evaluating papers, consider:

| Dimension | Excellent (A) | Good (B) | Fair (C) | Poor (D) |
|-----------|---------------|----------|----------|----------|
| **Novelty** | Breakthrough idea | Significant innovation | Incremental improvement | Trivial or rehashed |
| **Rigor** | Flawless methodology | Minor issues | Significant concerns | Fatal flaws |
| **Clarity** | Exceptionally clear | Well written | Confusing sections | Incomprehensible |
| **Impact** | Field-changing | Influential | Niche interest | Insignificant |
| **Reproducibility** | Fully reproducible | Mostly reproducible | Missing key details | Not reproducible |

## Guidelines

1. **Be objective**: Separate personal preference from objective quality assessment
2. **Be specific**: Cite specific sections/evidence for claims
3. **Be constructive**: Frame weaknesses as improvement opportunities
4. **Be comprehensive**: Cover all aspects, not just results
5. **Be contextual**: Consider venue standards and field norms
