---
name: Logo and Brand Identity
slug: logo-and-brand-identity
version: 1.1.0
category: image
description: Explore logos, wordmarks, symbols, and compact brand identity directions from approved brand inputs, with legibility and trademark-review gates.
status: ready
muapi_capabilities:
  - media.generate_image
  - media.edit_image
  - media.upload_file
  - media.upscale
  - media.check_result
  - media.search_models
required_connections:
  - muapi
permissions:
  - draft-only
  - workspace-write
---

# Logo and Brand Identity

## Mission

Turn a confirmed brand brief into several logo and identity directions: symbol,
wordmark, lockup, app icon, color system, and presentation board. Use the model
for exploration and visual direction, then make the limitations of generated
lettering, originality, and vector quality explicit.

This skill produces design drafts. It does not establish trademark clearance,
ownership, originality, or final legal approval.

## Required inputs

- Brand or product name and exact spelling.
- Business, audience, positioning, and intended applications.
- Desired personality, visual tone, color preferences, and motifs to avoid.
- Required deliverables: symbol, wordmark, lockup, favicon/app icon, palette,
  typography direction, usage board, or social avatar.
- Authorized sketches, moodboards, existing marks, and reference assets with
  their roles and rights status.

Collect when relevant:

- required language/script and localization;
- one-color, black-and-white, dark-background, embroidery, print, and small-size
  constraints;
- existing brand rules that must be preserved;
- competitor categories to avoid, review owner, budget, and vector/export needs.

## Brand-system modes

Choose the smallest mode that matches the request:

| Mode | Deliverables | Important caveat |
|---|---|---|
| Logo exploration | symbol, wordmark, lockup, icon, monochrome variants | Generated lettering and originality require review. |
| Brand kit | logo directions, proposed palette, typography pairing, pattern, and usage notes | Color values and font names are proposals until verified. |
| Design guide | palette/type cards, component previews, application mockups, and do/don't rules | A rendered board is not a production design system. |
| Application mockups | business card, packaging, social avatar, app icon, or signage | Mockups must not imply that unapproved marks or copy are final. |

## Workflow

1. Establish a brand brief with `fixed`, `explore`, `avoid`, and `applications`
   sections. Treat the brand name, approved colors, prohibited motifs, and
   existing marks as fixed facts.
2. Confirm rights for sketches, moodboards, fonts, logos, and third-party
   artwork. Upload local references once through `media.upload_file` and record
   whether each is a style, layout, or mark reference.
3. Select a text-capable or reference-capable model from the live schema. Use
   [MODELS.md](../../MODELS.md) and
   [the MuAPI tool reference](../../references/muapi-image-tools.md); do not
   assume that a model's attractive scene output makes it suitable for exact
   wordmarks.
4. Generate a bounded set of concept families, varying one meaningful axis at
   a time: geometric versus organic, typographic versus emblematic, restrained
   versus expressive, or monochrome versus color.
5. If the user requests a brand kit or design guide, add parallel deliverables
   for proposed color swatches, typography pairings, pattern/texture, UI
   components, and one real-world application. Keep the same brand brief in
   every branch and label all generated values as proposals.
6. For sketch-to-logo work, use `media.edit_image` and identify what the model
   may reinterpret. Keep exact text and approved marks in a separate
   compositing/layout step whenever possible.
7. Poll and record every output, including model, prompt, reference roles,
   request ID, status, billing, and provider error.
8. Review each concept at favicon, mobile, document, and large-display sizes.
   Check spelling, letterforms, spacing, silhouette, contrast, one-color use,
   embroidery/print plausibility, accidental symbols, and similarity risk.
9. Review brand-kit/design-guide boards for palette consistency, typography
   legibility, spacing rhythm, component reuse, contrast, and application
   consistency. Do not treat model-generated hex labels as measured color values.
10. Select a direction, then request a restrained refinement or upscale. Do not
   claim that a generated raster is an editable vector; hand off vectorization,
   font licensing, and trademark review as explicit next steps.

## Decision rules

- Exact brand names, legal copy, dates, product claims, and registered marks
  should be placed with approved layout assets, not trusted to regeneration.
- A logo concept is not a trademark search or an originality opinion. Recommend
  human design review and clearance before public adoption.
- Do not copy a competitor's mark, living artist's signature style, or a
  supplied logo beyond the authorized transformation.
- Keep the concept board and final production files distinct. A polished mockup
  can hide an unusable mark.
- Keep proposed palettes, font pairings, spacing tokens, and UI components
  editable and human-verifiable; generated labels are not authoritative design
  tokens.

## Output format

Return:

- the brand brief and fixed/explorable fields;
- concept family, prompt, model/tool, reference roles, and parameters;
- preview URLs, asset IDs, request status, and receipt links;
- legibility, exact-text, color, contrast, and similarity observations;
- vectorization, font, layout, trademark, and production requirements; and
- proposed palette roles, typography pairings, design tokens, application
  mockup notes, and what must be verified manually when a kit or guide was
  requested; and
- the recommended concept plus the smallest next iteration.

## Failure and missing-data behavior

If the brand name, language, rights, or applications are unclear, ask before a
paid call. If generated lettering is incorrect or a mark is too close to a
known design, label it exploratory and return a corrected layout or manual
design path rather than presenting it as a finished logo.
