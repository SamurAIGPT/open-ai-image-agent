---
name: Image Generation
slug: image-generation
version: 1.1.0
category: image
description: Turn a creative brief into a bounded set of text-to-image or reference-guided image candidates, selecting the MuAPI model and parameters for the actual job.
status: ready
muapi_capabilities:
  - media.generate_image
  - media.upload_file
  - media.check_result
  - media.search_models
  - media.account_balance
required_connections:
  - muapi
permissions:
  - draft-only
  - workspace-write
---

# Image Generation

## Mission

Turn a concrete creative brief into a small set of reviewable image
candidates. Choose the operation and model for the brief instead of treating a
single default model as a complete image strategy.

## Use this skill when

- a user needs one or more images from a text brief;
- a user wants reference-guided variations or a style/character direction;
- a user needs a first visual direction before editing or a larger campaign.

If the user asks to change an existing image while preserving it, use
[Image Editing](../image-editing/SKILL.md) instead.

## Required inputs

- Purpose and audience.
- Subject, scene, style, composition, lighting, mood, and copy direction.
- Target platform, aspect ratio, dimensions, resolution, and file format when
  known.
- Quantity of candidates or an explicit budget.

Collect when relevant:

- reference images and the role of each reference;
- fixed facts, prohibited changes, identity/product/brand constraints;
- quality, speed, price, text-rendering, or consistency priority;
- target language and localization requirements;
- rights/consent state and review owner;
- maximum iterations and whether the output is a concept, mockup, or final
  candidate.

## Model selection

Use [MODELS.md](../../MODELS.md) and the live schema in
[references/muapi-image-tools.md](../../references/muapi-image-tools.md). Use
`media.search_models` when the host exposes it. Check that the model supports
the required aspect ratio, resolution, reference count, output count, and
quality controls before sending the request.

## Workflow

1. Read `.image/project.md` and compatible prior runs when available. Reuse a
   confirmed style descriptor or asset manifest rather than rebuilding it from
   memory.
2. Normalize the brief into subject, action/state, setting, composition,
   camera/lighting, style, palette, text direction, negative constraints,
   format, and acceptance checks.
3. Separate immutable facts from creative choices. For products, record exact
   SKU/shape/color/quantity facts. For people, record identity/consent and
   requested likeness boundaries. For brands, record approved style rules.
4. If a local reference is supplied, confirm upload rights and use
   `media.upload_file` once per source. Record the hosted URL, role, order, and
   source metadata; never pass a local path to a model that requires a URL.
5. Select a model and state the proposed calls, variant count, parameters,
   estimated cost signal, and retry policy. Default to up to four first-round
   candidates only when that fits the user's budget; otherwise use fewer.
6. Submit independent candidates in parallel when the host supports it. Poll
   each asynchronous request with `media.check_result`.
7. Preserve request IDs, exact model/endpoint, sanitized parameters, status,
   output URLs, billing, and provider errors for every candidate.
8. Review candidates against the brief, fixed facts, composition, text,
   artifacts, dimensions, rights, and intended use. Present all successful and
   failed variants for selection.
9. Iterate by changing the smallest relevant variable. Keep parent/child asset
   relationships and do not retry a failed candidate silently more than once.
10. Send only the selected candidate to [Image Enhancement](../image-enhancement/SKILL.md)
    for upscaling or final preparation.

## Decision rules

- Prefer text-to-image for a new concept; prefer image-to-image/edit when
  source fidelity is part of the requirement.
- A generated image containing plausible text, packaging, or a logo still
  requires full-size verification and often post-production.
- Do not describe a model as best without a dated criterion. Use quality,
  price, speed, reference fidelity, text, or consistency as the explicit axis.
- Do not generate a broad batch when the brief, rights, platform, or budget is
  materially ambiguous.
- Treat a hosted output URL as temporary until the host archives it through an
  approved path.

## Output format

Return:

1. Brief and assumptions.
2. Model/tool, operation, parameters, and cost/budget note.
3. Every variant with asset ID, URL, status, and request ID when available.
4. Prompt or prompt hash, reference roles/order, and parent asset when
   iterating.
5. QA observations, selected direction, and exact next step.
6. Rights, claims, platform, accessibility, and URL-retention limitations.

## Failure and missing-data behavior

If generation fails, report the affected variant and provider error. If the
result is partial or has no usable output, preserve that state. Do not silently
return fewer images than requested or replace a failed reference-guided run
with an unrelated text-only image.

## Example interaction

**User:** “Create three 16:9 launch hero directions for a workflow product,
dark graphite palette, no generated text, using this UI screenshot without
changing the UI.”

**Agent:** confirms the screenshot rights and preservation boundary, proposes a
three-call plan with a model that accepts the format/reference, generates the
directions, checks the UI for drift, and returns the variants plus the exact
prompt/receipt metadata without publishing them.
