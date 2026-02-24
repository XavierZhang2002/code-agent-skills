---
name: literature-review
description: Generate comprehensive literature reviews from multiple papers. Use when the user needs to synthesize research from multiple sources, identify trends, categorize papers, or write a formal literature review section. Triggers: "write literature review", "synthesize papers", "research overview", "state of the art", "survey the field", "categorize research".
---

# Literature Review Generator

A systematic approach to synthesizing academic literature into coherent reviews.

## Types of Literature Reviews

### 1. Narrative Review
Provide broad overview of a field with critical analysis and synthesis.

### 2. Systematic Review
Follow rigorous methodology with explicit search criteria and inclusion/exclusion rules.

### 3. Scoping Review
Map the extent and nature of research in an area.

### 4. Meta-Analysis
Statistically combine results from multiple studies.

## Review Workflow

### Phase 1: Collection & Organization

```markdown
## Paper Inventory

### Search Strategy
**Databases searched**: [arXiv, Google Scholar, PubMed, etc.]
**Keywords used**: [List of search terms]
**Date range**: [Start - End]
**Inclusion criteria**: [What was included]
**Exclusion criteria**: [What was excluded]

### Papers Identified
| # | Title | Authors | Year | Venue | Category | Priority |
|---|-------|---------|------|-------|----------|----------|
| 1 | | | | | | High/Med/Low |
| 2 | | | | | | |

### Selection Process
- Total identified: [N]
- After screening: [N]
- Final included: [N]
```

### Phase 2: Taxonomy Development

Create classification scheme:

```markdown
## Taxonomy

### By Method/Approach
1. **Category A**: [Description]
   - Subcategory A1
   - Subcategory A2

2. **Category B**: [Description]
   - Subcategory B1
   - Subcategory B2

### By Problem Domain
1. **Problem X**: [Description]
2. **Problem Y**: [Description]

### By Timeline
- **Foundational** (Before 2020)
- **Emerging** (2020-2023)
- **Current** (2024-present)
```

### Phase 3: Analysis & Synthesis

#### Thematic Analysis

```markdown
## Theme 1: [Theme Name]

**Description**: [What this theme encompasses]

**Key Papers**:
- [Author, Year]: [Key contribution]
- [Author, Year]: [Key contribution]

**Evolution**: [How this theme developed over time]

**Current State**: [Where this theme stands now]

**Key Debates**: [Controversies or competing approaches]

**Future Directions**: [Where this theme is heading]
```

#### Comparative Synthesis

```markdown
## Approach Comparison

### Comparison Table
| Criterion | Approach A | Approach B | Approach C |
|-----------|------------|------------|------------|
| Performance | | | |
| Computational cost | | | |
| Data requirements | | | |
| Generalizability | | | |
| Interpretability | | | |

### Trade-off Analysis
- **Performance vs Efficiency**: [Key trade-offs]
- **Accuracy vs Interpretability**: [Key trade-offs]
- **Supervised vs Unsupervised**: [Key trade-offs]
```

### Phase 4: Gap Analysis

```markdown
## Research Gaps

### Gap 1: [Gap Name]
**Description**: [What is missing]
**Evidence**: [Papers that hint at this gap]
**Significance**: [Why filling this gap matters]
**Potential Approaches**: [How it might be addressed]

### Gap 2: [Gap Name]
...

### Gap Categorization
| Gap Type | Count | Examples |
|----------|-------|----------|
| Theoretical | [N] | |
| Methodological | [N] | |
| Empirical | [N] | |
| Practical | [N] | |
```

### Phase 5: Synthesis Writing

#### Structure 1: Chronological

```markdown
## Historical Development

### Foundational Period (Year - Year)
[Early work that established the field]

### Growth Period (Year - Year)
[Expansion and diversification]

### Current Period (Year - Present)
[Recent developments and trends]
```

#### Structure 2: Thematic

```markdown
## Thematic Review

### Theme 1: [Name]
[Detailed synthesis]

### Theme 2: [Name]
[Detailed synthesis]

### Theme 3: [Name]
[Detailed synthesis]

### Cross-cutting Issues
[Themes that span multiple areas]
```

#### Structure 3: Methodological

```markdown
## Methodological Review

### Problem Formulation
[How the problem is defined]

### Solution Approaches
#### Approach 1: [Name]
[Detailed description and examples]

#### Approach 2: [Name]
[Detailed description and examples]

### Evaluation Methodologies
[How progress is measured]
```

## Output Templates

### Full Literature Review

```markdown
# Literature Review: [Topic]

## Abstract
[Brief summary of scope, methodology, and key findings]

## 1. Introduction
### 1.1 Background
[Context and motivation]

### 1.2 Scope
[What is included/excluded]

### 1.3 Research Questions
[Key questions the review addresses]

## 2. Methodology
### 2.1 Search Strategy
[How papers were found]

### 2.2 Selection Criteria
[Inclusion/exclusion rules]

### 2.3 Analysis Method
[How papers were analyzed]

## 3. Overview of the Field
### 3.1 Volume and Growth
[Publication trends]

### 3.2 Key Venues
[Where research is published]

### 3.3 Leading Researchers
[Key contributors]

## 4. Thematic Analysis
[Detailed synthesis by themes]

## 5. Critical Evaluation
### 5.1 Strengths of Current Research
[What is working well]

### 5.2 Limitations
[Common weaknesses]

### 5.3 Methodological Concerns
[Issues with how research is conducted]

## 6. Research Gaps
[Detailed gap analysis]

## 7. Future Directions
[Recommendations for future work]

## 8. Conclusion
[Summary of key findings]

## References
[Full bibliography]
```

### Quick Survey Format

```markdown
# Research Survey: [Topic]

## Executive Summary
- **Papers reviewed**: [N]
- **Time span**: [Years]
- **Key finding**: [One sentence]
- **Main gap**: [One sentence]

## Categorization
[Visual diagram or table]

## Top Papers
1. **[Title]** - [Why it matters]
2. **[Title]** - [Why it matters]
3. **[Title]** - [Why it matters]

## Trends
[Graphical or textual trend analysis]

## Recommendations
1. [Actionable recommendation]
2. [Actionable recommendation]
```

## Quality Checklist

When generating a literature review, ensure:

- [ ] **Coverage**: All major works included
- [ ] **Currency**: Recent papers represented
- [ ] **Diversity**: Multiple perspectives included
- [ ] **Balance**: Positive and negative findings reported
- [ ] **Synthesis**: Not just a list, but integrated analysis
- [ ] **Criticality**: Critical evaluation, not just description
- [ ] **Clarity**: Clear organization and flow
- [ ] **Objectivity**: Balanced presentation of views

## Common Pitfalls to Avoid

1. **Cherry-picking**: Only citing papers that support a position
2. **Citation dumping**: Listing papers without synthesis
3. **Outdated focus**: Over-emphasizing older work
4. **Lack of structure**: Random organization
5. **Missing context**: Not explaining significance
6. **Unclear criteria**: Not stating inclusion/exclusion rules
7. **Shallow analysis**: Describing without analyzing
