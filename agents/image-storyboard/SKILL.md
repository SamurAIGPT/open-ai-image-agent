---
name: Image Storyboard
slug: image-storyboard
version: 1.0.0
category: image
description: Turn a story premise into an ordered set of visual keyframes with continuity notes, without generating video or audio.
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

# Image Storyboard

## Mission

Translate a premise, script excerpt, product narrative, or scene idea into an
ordered storyboard of still images. Establish visual continuity for characters,
props, locations, lighting, and screen direction while keeping each frame
independently reviewable.

This skill outputs keyframes only. It does not animate frames, create audio, or
claim that a generated storyboard proves an event occurred.

## Required inputs

- One-line premise or short story/script.
- Number of frames or beats, target aspect ratio, and output format.
- Visual style, audience, tone, and intended use.
- Character, product, prop, location, or brand facts that must stay consistent.

Collect when relevant:

- approved character/product reference images and their rights status;
- scene order, camera movement, dialogue/copy to visualize, safety boundaries,
  language, budget, and reviewer;
- whether frames are for pitching, shot planning, animation handoff, or a
  static comic/presentation.

## Continuity protocol

Before any image call, create a continuity sheet containing:

- stable character/subject descriptors and identity IDs;
- wardrobe, prop, product, and environment invariants;
- time of day, lighting direction, palette, lens language, and visual style;
- screen direction, eyelines, geography, and frame numbering; and
- facts that may change from beat to beat.

Do not silently redesign a character or product between frames. If a real
person's likeness is used, obtain permission and keep identity analysis separate
from demographic assumptions.

## Workflow

1. Read project context and decompose the premise into a clear arc such as
   setup, inciting moment, escalation, climax, and resolution. Use the user's
   scene count unless it is missing; then propose a count before paid work.
2. Write one visual beat per frame with subject/action, setting, composition,
   lighting, continuity fields, and a one-line caption. Avoid keyword soup;
   describe spatial and physical relationships in complete sentences.
3. Upload approved local character, product, or style references once through
   `media.upload_file`. Record their roles and reuse the same order when the
   selected model accepts them.
4. Select a live image model supporting the requested ratio, reference inputs,
   resolution, and output count. Verify [MODELS.md](../../MODELS.md) and
   [the MuAPI tool reference](../../references/muapi-image-tools.md).
5. Announce the frame count, model/call count, cost signal, and review gate.
   Generate the independent keyframes in parallel when possible.
6. Poll with `media.check_result` and preserve every frame's request ID, status,
   output URL, billing, and provider error.
7. Review frame order and continuity: identity, wardrobe, props, product
   geometry, location, light direction, color, camera grammar, eyelines,
   screen direction, text, and artifacts.
8. Return a numbered gallery description and flag frames that need a redraw.
   Do not upscale or hand off to video until the storyboard is approved.

## Decision rules

- Keep all keyframes in one visual system; style variation belongs in a
  separately labeled concept branch.
- Use image editing for a supplied character/product frame when continuity is
  more important than a new composition.
- Keep exact dialogue, titles, labels, logos, and legal copy out of generated
  lettering when a layout step is available.
- A storyboard is a planning artifact, not a final shot list, production proof,
  or factual record.

## Output format

Return an ordered table with frame number, beat/caption, visual description,
continuity constraints, model/tool, parameters, output URL/status, QA notes,
and the next action for any failed or inconsistent frame.

## Failure and missing-data behavior

If the premise, scene count, references, or intended style is too ambiguous,
ask before generating. If a frame fails or breaks continuity, preserve it as
failed/partial and identify the smallest redraw rather than silently changing
the story.
