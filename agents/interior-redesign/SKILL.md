---
name: Interior Redesign
slug: interior-redesign
version: 1.1.0
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
- Optional 2D floor plan or a written layout description when a plan-to-render
  workflow is requested.
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

## Interior modes

| Mode | Inputs | Handoff |
|---|---|---|
| Declutter | room photograph, items to remove, items to preserve | Before/after concept with removed-object notes. |
| Redesign | room photograph, style and furnishing brief | Geometry-anchored style variants. |
| Property staging | empty or furnished room, listing context, target audience | Clearly labeled staged visualization, not an unmodified listing photo. |
| Floor-plan rendering | approved 2D plan or layout description | Plan review followed by a labeled 3D/isometric visualization. |

For a floor-plan workflow, dimensions, room names, windows, doors, stairs, and
fixed fixtures are facts supplied by the user. A generated plan or rendering
must not be treated as an architectural or construction document.

## Workflow

1. Inspect the source and map `preserve`, `remove`, `add`, `style`, and
   `delivery` fields. Mark uncertain geometry as unknown instead of guessing.
2. If no floor plan exists but one is requested, draft a clearly labeled 2D
   concept from the supplied layout description and get approval before using
   it as the parent of a 3D render. If a plan exists, preserve the original and
   verify its labels and dimensions with the user.
3. Confirm permission to process the room image and any furniture, artwork, or
   people visible in it. Remove or mask private information where appropriate.
4. Upload the source through `media.upload_file` and use an editing/reference
   workflow for a real room. Use generation only for a clearly labeled
   inspiration concept or when the source does not need to remain recognizable.
5. Select a live model supporting the requested edit, ratio, reference, and
   resolution. Check [MODELS.md](../../MODELS.md) and
   [the MuAPI tool reference](../../references/muapi-image-tools.md).
6. State the planned calls, variants, cost signal, and review gate. Generate a
   small set that varies style or furnishing level while keeping the room
   geometry stable.
7. Poll with `media.check_result` and preserve every output, request ID,
   status, URL, billing object, and provider error.
8. Review walls, windows, doors, floors, fixtures, perspective, shadows,
   furniture scale, occlusions, reflections, textures, and unwanted objects.
   Check that decluttering did not remove safety features or structural facts.
9. Return the selected concept with a clear `visualization only` label when it
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
- For floor-plan rendering, preserve the approved plan as a separate parent and
  label the 3D image as illustrative. Do not infer a construction-ready result
  from a visually plausible render.

## Output format

Return the source/property role, room facts, change/preserve map, model/tool and
parameters, output URLs/status, style and geometry QA, visualization/listing
label, sourcing/measurement limitations, and receipt links.

## Failure and missing-data behavior

If the room geometry, property rights, requested style, or target use is
unclear, ask before a paid call. If the model changes structural features or
produces impossible perspective, mark the result as failed/partial and suggest
manual staging or a better source image.
