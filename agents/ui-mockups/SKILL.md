---
name: UI Mockups
slug: ui-mockups
version: 1.0.0
category: image
description: Create high-fidelity mobile or web interface mockups and lightweight design-system boards from a product brief, with accessibility and implementation handoff notes.
status: ready
muapi_capabilities:
  - media.generate_image
  - media.edit_image
  - media.upload_file
  - media.check_result
  - media.search_models
required_connections:
  - muapi
permissions:
  - draft-only
  - workspace-write
---

# UI Mockups

## Mission

Turn a product or feature brief into visual UI/UX mockups for mobile, web,
SaaS, ecommerce, portfolios, or internal tools. Express layout hierarchy,
components, design tokens, and responsive intent while making clear that a
rendered mockup is not working software or a usability certification.

## Required inputs

- Product, feature, user, and task to visualize.
- Platform: mobile, web, tablet, desktop, or a named viewport.
- Screens or states required: landing, dashboard, onboarding, checkout,
  settings, empty/error/loading, or another flow.
- Brand style, palette, typography direction, content hierarchy, and desired
  visual tone.

Collect when relevant:

- existing screenshots, logos, design tokens, component library, or brand guide;
- target viewport dimensions, localization, accessibility requirements,
  interaction states, copy, reviewer, and implementation stack;
- whether the output is a wireframe, high-fidelity mockup, presentation board,
  or design-system reference.

## Design specification

Before generation, translate the brief into:

- page hierarchy and the primary user action;
- atomic components: buttons, inputs, cards, navigation, tables, alerts, and
  content modules;
- spacing rhythm, typography scale, color tokens, elevation, and icon style;
- responsive behavior and safe regions for content;
- realistic placeholder copy with known text limitations; and
- accessibility checks for contrast, focus, labels, hierarchy, and density.

Use complete descriptions of how components relate. Avoid keyword soup and do
not ask the model to render a photograph of a screen, hands holding a phone, or
an invented device frame unless that mockup context is explicitly requested.

## Workflow

1. Read `.image/project.md` and supplied brand/screenshot references. Separate
   approved UI facts from visual inspiration and confirm rights to upload them.
2. Build a screen matrix with screen purpose, viewport, components, content
   hierarchy, state, interaction cue, and design tokens.
3. Upload local screenshots, logos, or style references once through
   `media.upload_file`; label them as layout, brand, content, or inspiration.
4. Select a live model suited to UI text, layout, and reference editing. Check
   [MODELS.md](../../MODELS.md) and
   [the MuAPI tool reference](../../references/muapi-image-tools.md).
5. Announce the screen count, model/call count, cost signal, and review gate.
   Generate independent screens in parallel only when they share the same
   design specification.
6. Poll with `media.check_result` and preserve model, request ID, status,
   outputs, billing, references, and provider errors.
7. Review hierarchy, alignment, spacing, component consistency, contrast,
   overflow, text legibility, localization risk, responsive assumptions, and
   whether the image accidentally implies a functional interaction.
8. Return the mockups with a written token/component handoff. Put exact copy,
   SVG icons, and production layouts into the implementation/design tool rather
   than trusting a generated raster.

## Decision rules

- Use a consistent design specification across screens; do not let each image
  invent a separate component system.
- Prefer editing a supplied screenshot for a requested visual change and label
  any regenerated UI as a concept.
- Generated copy, prices, metrics, logos, testimonials, and product claims are
  placeholders until verified.
- Accessibility and usability are review requirements, not guarantees from a
  visually polished mockup.

## Output format

Return a screen table with purpose, viewport, state, model/tool, parameters,
output URL/status, design-token notes, component consistency, accessibility and
text observations, implementation handoff, and receipt links.

## Failure and missing-data behavior

If the target platform, screen purpose, brand system, copy, or reference rights
are unclear, ask before a paid call. If a screen contains unreadable text,
broken hierarchy, or inconsistent components, mark it as a draft and recommend
layout/post-production work rather than presenting it as implementation-ready.
