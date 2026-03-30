# Mermaid Custom Integration — Reference

Detailed templates and diagnostics for bypassing Material for MkDocs' Mermaid CSS override. Read this file when implementing the custom Mermaid integration described in SKILL.md §2.3.

## Why Material Overrides Mermaid Themes

Material for MkDocs wraps Mermaid in **shadow DOM** and injects its own CSS that targets `.mermaid` elements. This CSS unconditionally overrides all Mermaid color settings.

| What you try | Works? | Why not |
|---|---|---|
| `%%{init: {'themeVariables': {...}}}%%` in markdown | No | Material CSS overrides after render |
| Custom CSS in `extra.css` targeting `.mermaid` | No | Cannot penetrate shadow DOM |
| `!important` in extra CSS | No | Shadow DOM encapsulation blocks it |
| Mermaid `classDef` inline styles | Partially | Works for nodes but not subgraph backgrounds |

**Confirmed by** squidfunk (Material author) in [#5681](https://github.com/squidfunk/mkdocs-material/issues/5681) and [#4582](https://github.com/squidfunk/mkdocs-material/discussions/4582).

## Full `mermaid.mjs` Template

Create this file at `docs/javascripts/mermaid.mjs`. Adjust colors to match your site palette.

```javascript
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";

mermaid.initialize({
  startOnLoad: false,
  securityLevel: "loose",
  theme: "base",
  themeVariables: {
    // --- Adjust these to your palette ---
    // Node colors
    primaryColor: "#eef0fb",        // node background
    primaryTextColor: "#303680",     // node text
    primaryBorderColor: "#9ba3d6",   // node border
    // Lines
    lineColor: "#9ba3d6",           // edge/arrow color
    // Alternate nodes
    secondaryColor: "#f8f8fc",
    secondaryBorderColor: "#d8dbe8",
    secondaryTextColor: "#303680",
    // Subgraph / cluster backgrounds (the gray-background fix)
    tertiaryColor: "#ffffff",
    tertiaryBorderColor: "#d8dbe8",
    tertiaryTextColor: "#303680",
    clusterBkg: "#ffffff",           // KEY: subgraph fill
    clusterBorder: "#d8dbe8",        // KEY: subgraph border
    // Edge labels
    edgeLabelBackground: "#ffffff",
    // Notes (sequence diagrams)
    noteBkgColor: "#f8f8fc",
    noteTextColor: "#303680",
    noteBorderColor: "#9ba3d6",
    // Typography
    fontFamily: "Noto Sans SC, -apple-system, BlinkMacSystemFont, sans-serif",
    fontSize: "13px",
    // --- End palette section ---
  },
});

// Render .mermaid-custom elements (bypasses Material's .mermaid handling)
async function renderMermaidCustom() {
  const elements = document.querySelectorAll(".mermaid-custom");
  if (elements.length === 0) return;

  for (const el of elements) {
    if (el.dataset.processed) continue;
    el.dataset.processed = "true";

    const code = el.textContent.trim();
    const id = `mermaid-${Math.random().toString(36).slice(2, 10)}`;

    try {
      const { svg } = await mermaid.render(id, code);
      el.innerHTML = svg;
      el.style.textAlign = "center";
    } catch (err) {
      console.error("Mermaid render error:", err);
    }
  }
}

// Support Material's instant loading (SPA navigation)
if (typeof document$ !== "undefined") {
  document$.subscribe(() => renderMermaidCustom());
} else {
  document.addEventListener("DOMContentLoaded", renderMermaidCustom);
}
```

## Preset Palettes

Replace the palette section in the template above with one of these:

### Indigo (matches Material indigo primary)

```javascript
primaryColor: "#eef0fb",
primaryTextColor: "#303680",
primaryBorderColor: "#9ba3d6",
lineColor: "#9ba3d6",
secondaryColor: "#f8f8fc",
secondaryBorderColor: "#d8dbe8",
clusterBkg: "#ffffff",
clusterBorder: "#d8dbe8",
```

### Teal (matches Material teal primary)

```javascript
primaryColor: "#e0f2f1",
primaryTextColor: "#004d40",
primaryBorderColor: "#80cbc4",
lineColor: "#80cbc4",
secondaryColor: "#f1f8f7",
secondaryBorderColor: "#b2dfdb",
clusterBkg: "#ffffff",
clusterBorder: "#b2dfdb",
```

### Neutral (minimal, works with any theme)

```javascript
primaryColor: "#f5f5f5",
primaryTextColor: "#333333",
primaryBorderColor: "#bdbdbd",
lineColor: "#9e9e9e",
secondaryColor: "#fafafa",
secondaryBorderColor: "#e0e0e0",
clusterBkg: "#ffffff",
clusterBorder: "#e0e0e0",
```

## Required CSS (`extra.css`)

```css
.md-typeset .mermaid-custom {
  margin: 1.2rem auto;
  text-align: center;
}

.md-typeset .mermaid-custom svg {
  max-width: 100%;
  height: auto;
}
```

## `mkdocs.yml` Changes

```yaml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid-custom          # NOT "mermaid"
          format: !!python/name:pymdownx.superfences.fence_code_format

extra_javascript:
  - javascripts/mermaid.mjs              # must be listed
```

## Post-Migration Cleanup

After switching to custom integration, remove all `%%{init}%%` directives from markdown files — they are no longer needed (theme is controlled globally by `mermaid.mjs`):

```bash
# Find files with %%{init directives
grep -rl '%%{init:' docs/
# Remove the lines (verify manually first)
```

Markdown ```` ```mermaid ```` blocks themselves need no changes — they still use the same syntax.
