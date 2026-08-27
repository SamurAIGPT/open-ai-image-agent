---
name: Multi-Angle Reshoot
slug: multi-angle-reshoot
version: 1.0.0
category: image
description: Re-render an authorized subject, product, or scene from selected camera angles while preserving the approved parent asset.
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

# Multi-Angle Reshoot

## Mission

Create a controlled set of alternate camera perspectives from an approved
subject, product, or scene: eye-level, three-quarter, low-angle, overhead,
macro, wide, or another requested angle. Preserve identity, geometry, wardrobe,
materials, and lighting continuity as far as the live model allows.

## Required inputs

- Subject, product, or scene description.
- Approved reference image, if one already exists; otherwise permission to make
  one base image for approval first.
- Requested angles and what must remain unchanged.
- Target aspect ratio, resolution, output count, delivery format, and intended
  use.

Collect when relevant:

- product/SKU facts, person consent, brand rules, background, lighting, lens
  feel, category-specific details, budget, and reviewer;
- whether the result is a creative reshoot, catalog view, storyboard frame, or
  fictional concept.

## Angle matrix

Choose only the angles that serve the brief. Common options include:

| Angle | Useful for | Main QA risk |
|---|---|---|
| Eye-level/front | baseline or primary view | symmetry, centering, label/text drift |
| Three-quarter/side | depth and silhouette | product geometry, face profile, seams |
| Low-angle hero | premium or powerful emphasis | distorted proportions, unsupported claims |
| Overhead/top-down | layout, flat lay, or spatial context | hidden surfaces, scale, shadows |
| Macro/detail | material or feature detail | invented texture, label and logo errors |
| Wide/bird's-eye | environment and composition | missing edges, perspective, continuity |

## Workflow

1. Inspect the supplied source and write `preserve`, `angle`, `change`, and
   `avoid` blocks. If no source exists, generate one neutral base image in the
   requested ratio and get user approval before reshooting.
2. Confirm product/likeness rights. Label identity, product, environment,
   wardrobe, lighting, and layout references separately.
3. Upload a local parent once through `media.upload_file`. Record the parent
   asset ID, hosted URL, and reference role/order.
4. Select a reference-capable edit model for the angle branches. Check the
   current schema in [MODELS.md](../../MODELS.md) and
   [the MuAPI tool reference](../../references/muapi-image-tools.md).
5. Announce the selected angles, branch count, model, cost signal, and review
   gate. Generate the independent angle branches in parallel when possible.
6. Use `media.edit_image` with one angle directive per branch. Keep the
   approved parent unchanged and do not chain a drifted angle into later ones.
7. Poll with `media.check_result`; preserve request IDs, status, outputs,
   billing, errors, and parent/child relationships.
8. Review subject/product identity, geometry, proportions, perspective,
   reflections, hands/face, label/logo, shadows, crop, and lighting continuity.
9. Upscale only selected angles and return a gallery ordered by camera view.

## Decision rules

- For exact products, prefer source-based editing and label any invented hidden
  side as a concept rather than a verified view.
- For people, require permission and do not use an angle reshoot to create
  deceptive evidence, official-document imagery, or non-consensual edits.
- Keep lens distortion explicit; fish-eye, Dutch-angle, and macro branches are
  creative effects, not neutral product documentation.
- Do not generate all angles by default when the user needs only one or two;
  each branch may incur a separate call.

## Output format

Return the approved parent, angle matrix, model/tool and parameters, one row per
angle with asset ID/status/output URL, continuity observations, selected angles,
and receipt links.

## Failure and missing-data behavior

If no parent can be established, the source is unauthorized, or an angle cannot
preserve the subject, stop that branch and explain the supported alternative.
Never silently present a new subject as a faithful reshoot.
