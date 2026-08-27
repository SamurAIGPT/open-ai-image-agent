---
name: Interior Redesign
slug: interior-redesign
version: 1.0.0
category: image
description: Visualize decluttered, redesigned, or staged interiors while preserving room geometry and separating concepts from property claims.
status: ready
muapi_capabilities:
  - media.edit_image
  - media.generate_image
  - media.upload_file
  - media.check_result
  - media.search_models
required_connections:
  - muapi
permissions:
  - draft-only
  - workspace-write
---

# Interior Redesign

## Mission

Turn an authorized room photograph into a decluttered, redesigned, or staged
interior concept. Preserve the room's real geometry and clearly separate visual
inspiration from a claim about the actual property, furniture, dimensions, or
availability.

## Required inputs

- Room photograph or authorized property reference.
- Room type, intended audience, and use: design exploration, rental staging,
  listing concept, renovation planning, or furniture visualization.
- Desired style, palette, furniture categories, materials, lighting, and items
  to remove, retain, add, or avoid.
- Room facts that must remain stable: walls, windows, doors, ceiling height,
  floor, built-ins, fixtures, outlets, views, and structural boundaries.
- Target aspect ratio, resolution, quantity, and delivery format.

Collect when relevant:

- property-owner or tenant permission;
- furniture dimensions, accessibility needs, budget, region, season, and
  availability constraints;
- whether the output may appear in a listing or is only an inspiration board;
- approved brand/developer style, reviewer, and post-production plan.

Do not infer measurements, structural condition, property ownership, furniture
availability, or renovation feasibility from an image.

## Workflow

1. Inspect the source and map `preserve`, `remove`, `add`, `style`, and
   `delivery` fields. Mark uncertain geometry as unknown instead of guessing.
2. Confirm permission to process the room image and any furniture, artwork, or
   people visible in it. Remove or mask private information where appropriate.
3. Upload the source through `media.upload_file` and use an editing/reference
   workflow for a real room. Use generation only for a clearly labeled
   inspiration concept or when the source does not need to remain recognizable.
4. Select a live model supporting the requested edit, ratio, reference, and
   resolution. Check [MODELS.md](../../MODELS.md) and
   [the MuAPI tool reference](../../references/muapi-image-tools.md).
5. State the planned calls, variants, cost signal, and review gate. Generate a
   small set that varies style or furnishing level while keeping the room
   geometry stable.
6. Poll with `media.check_result` and preserve every output, request ID,
   status, URL, billing object, and provider error.
7. Review walls, windows, doors, floors, fixtures, perspective, shadows,
   furniture scale, occlusions, reflections, textures, and unwanted objects.
   Check that decluttering did not remove safety features or structural facts.
8. Return the selected concept with a clear `visualization only` label when it
   could be mistaken for a real listing photograph. Send measurements,
   furniture sourcing, and final retouching to human review.

## Decision rules

- Preserve property geometry for redesign and staging; use generation for
  moodboards or fictional scenes only.
- Do not invent a view, room size, structural change, appliance, material,
  accessibility feature, energy rating, or furniture availability.
- A staged image must not be presented as an unaltered photograph.
- Keep people, private documents, artwork, and personal belongings unchanged or
  explicitly removed with permission.

## Output format

Return the source/property role, room facts, change/preserve map, model/tool and
parameters, output URLs/status, style and geometry QA, visualization/listing
label, sourcing/measurement limitations, and receipt links.

## Failure and missing-data behavior

If the room geometry, property rights, requested style, or target use is
unclear, ask before a paid call. If the model changes structural features or
produces impossible perspective, mark the result as failed/partial and suggest
manual staging or a better source image.
