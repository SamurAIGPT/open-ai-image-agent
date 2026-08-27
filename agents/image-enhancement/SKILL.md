---
name: Image Enhancement
slug: image-enhancement
version: 1.0.0
category: image
description: Apply a bounded image-enhancement operation such as upscaling, background removal, extension, or cleanup while preserving the intended subject.
status: ready
muapi_capabilities:
  - media.enhance_image
  - media.upscale
  - media.upload_file
  - media.check_result
required_connections:
  - muapi
permissions:
  - draft-only
  - workspace-write
---

# Image Enhancement

## Mission

Improve or prepare an existing image for delivery without confusing an
enhancement with a creative re-generation. Route the request to the narrowest
MuAPI operation that can perform it.

## Supported request types

- upscale resolution;
- remove or replace a background;
- extend/outpaint a frame when the provider operation supports it;
- restore, colorize, clean up, or apply a named transformation when the live
  model/tool explicitly supports it;
- prepare a final selected image for a target platform or delivery size.

Use [MODELS.md](../../MODELS.md) and
[the MuAPI tool reference](../../references/muapi-image-tools.md) for current
operations. Do not invent a parameter or assume that every enhancement tool
supports every source format.

## Required inputs

- Source image URL or local file.
- One explicit operation and the desired output size or condition.
- Details that must remain unchanged.
- Target channel or delivery format when relevant.

## Workflow

1. Confirm the source, operation, target, preservation constraints, and whether
   the user wants a concept or delivery candidate.
2. Check rights and privacy before uploading a local image. Upload it with
   `media.upload_file` when the chosen operation requires a hosted URL.
3. Choose the operation-specific tool/model. Use `media.upscale` only after a
   candidate is selected; it is not a substitute for repairing geometry,
   spelling, or an incorrect product.
4. State the call count, model/operation, estimated cost signal, and retry
   policy before execution when the account or cost is unknown.
5. Submit and poll with `media.check_result`. Preserve request ID, status,
   output URLs, billing, and errors.
6. Review edges, fine detail, noise, halos, transparency, crop, face/product
   identity, text, and dimensions. For background changes, check hair, glass,
   shadows, reflections, and holes.
7. Return the enhanced output with a clear note about what changed and what
   still needs manual post-production.

## Decision rules

- Enhancement should not silently change a person's identity, a product's
  geometry, a label, or a brand mark.
- Use editing for an intentional scene/object change and enhancement for a
  bounded preparation operation.
- Do not upscale every variant in a concept batch; select first unless the
  user requests otherwise.
- Face swap or likeness transformation is a rights-sensitive edit, not a
  routine enhancement. Require explicit consent and record the source roles.

## Output format

Return the source, operation, model/tool, parameters, output URL(s), dimensions,
status, QA observations, receipt link, and any unresolved rights or delivery
limitations.

## Failure and missing-data behavior

If the operation is unsupported or the result is partial, report the exact
boundary and preserve the failed call. Do not label a failed upscale or
background removal as completed because a request ID was created.
