---
name: Thumbnail Generation
slug: thumbnail-generation
version: 1.1.0
category: image
description: Produce a small set of truthful, high-contrast video or article thumbnail directions with platform-aware composition and text-safe space.
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

# Thumbnail Generation

## Mission

Create thumbnail directions that communicate the actual content quickly at
small size. Optimize the visual hook and hierarchy, not a misleading promise
or an image full of model-generated copy.

## Required inputs

- Video/article title or core topic.
- Platform and target dimensions; use the platform's current requirements.
- Channel/brand style and audience.
- Optional source frame, face, product, logo, or other reference image.

Collect when relevant:

- the actual content promise and approved claims;
- subject emotion/pose and what must remain recognizable;
- language, overlay copy, safe areas, and number of variants;
- budget and whether typography will be added in post-production.

## Model selection

Use [MODELS.md](../../MODELS.md) and the live provider contract in
[references/muapi-image-tools.md](../../references/muapi-image-tools.md). Use
text-to-image for a new concept and image editing when incorporating a real
source frame or face. A public MuAPI `youtube-thumbnail` recipe is a useful
starting workflow, but its current model and fields must be rechecked.

## Workflow

1. Extract the content hook and write one honest visual promise. Do not invent
   results, guests, products, or events that do not appear in the content.
2. Propose two or three distinct concepts, such as emotion-first, single-object
   contrast, before/after only when factual, or a clean curiosity gap.
3. Define the subject, focal point, rule-of-thirds placement, background
   contrast, safe text region, and no-go elements for each concept.
4. If a local source image is supplied, confirm rights and upload it with
   `media.upload_file`. Use `media.edit_image` to incorporate or reframe it.
5. Generate one candidate per approved concept in the target aspect ratio. Keep
   the first batch bounded and state the call count/cost signal first.
6. Poll and preserve each result. Review the thumbnail at small size for
   immediate subject recognition, contrast, crop, facial/subject drift,
   artifacting, and truthful content representation.
7. Return suggested overlay copy of three to five words, placement, and
   post-production typography guidance. Prefer adding exact text outside the
   image model; if text is generated, verify spelling and legibility.
8. Offer A/B variants only when the user asks or has approved the additional
   calls.

## Decision rules

- One clear focal point beats a crowded collage.
- Do not use a fake reaction, badge, celebrity, result, or screenshot to imply
  content the video/article does not contain.
- Keep overlay copy short and high-contrast; text-rendering in generated images
  is not a substitute for final typography.
- Preserve a real source subject rather than regenerating it when identity or
  product continuity matters.

## Output format

Return one row per concept with title/hook, concept label, model/tool, prompt or
prompt hash, output URL, status, dimensions, suggested overlay, text placement,
QA notes, and receipt link when saved.

## Failure and missing-data behavior

If the topic is too abstract to create an honest visual, ask for a more
specific angle or source image. If a source or generation branch fails, report
it explicitly and do not silently replace it with a generic thumbnail.
