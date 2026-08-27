---
name: Image Editing
slug: image-editing
version: 1.0.0
category: image
description: Edit or transform a supplied image while preserving the specific people, products, composition, or brand details the user marks as fixed.
status: ready
muapi_capabilities:
  - media.edit_image
  - media.upload_file
  - media.check_result
required_connections:
  - muapi
permissions:
  - draft-only
  - workspace-write
---

# Image Editing

## Mission

Make a controlled change to an existing image. Use this skill when the user
says “edit,” “remove,” “replace,” “reframe,” “keep the same,” or supplies a
source image whose identity, product geometry, or composition matters.

## Required inputs

- Source image URL or local file.
- Exact requested change.
- Details that must remain unchanged.
- Target aspect ratio, dimensions, file format, and quantity when relevant.

Collect when relevant:

- additional reference images and their roles/order;
- mask or region guidance when the selected model supports it;
- identity, product, logo, label, or packaging rights;
- quality, speed, cost, and iteration priorities;
- whether the result is a concept, mockup, or final commercial candidate.

## Model selection

Use the editing/image-to-image entries in [MODELS.md](../../MODELS.md) and the
live schema described in [the MuAPI tool reference](../../references/muapi-image-tools.md).
Do not silently route an edit to text-to-image when the user expects source
fidelity.

## Workflow

1. Inspect the source and create two lists: `change` and `preserve`. Include
   fixed geometry, identity, labels, logos, text, colors, quantity, lighting,
   and camera position when applicable.
2. Confirm rights to upload the source and any additional reference. Do not
   use a saved private identity or brand asset without an explicit match.
3. If the source is local, upload it through `media.upload_file` and record the
   hosted URL, role, order, and source metadata. Pass only hosted URLs accepted
   by the selected endpoint.
4. Build an edit prompt with the requested change first, followed by an
   explicit preservation block and unwanted-change constraints. Keep exact
   copy, labels, logos, and claims out of a regeneration request when
   approved source art can be composited instead.
5. Select the narrowest editing model that supports the source count, target
   ratio, and required operation. State the planned call, estimated cost
   signal, and retry policy before execution when unknown.
6. Generate a bounded preview. Poll with `media.check_result` and preserve the
   request ID, status, output URLs, billing, and provider errors.
7. Compare source and output for unintended changes. Check identity/product
   fidelity, geometry, text, edges, shadows, repeated objects, artifacts,
   crop, and requested region.
8. On feedback, change one relevant variable at a time. If the model cannot
   preserve a fixed detail, recommend compositing or a different supported
   operation rather than claiming success.

## Output format

Return:

- source asset and reference roles;
- requested change and preservation block;
- model/tool, parameters, and output dimensions;
- output URL(s), asset IDs, request status, and receipt link when saved;
- changed details, preserved details, observed drift, and required
  post-production;
- rights, text, claims, and URL-retention limitations.

## Failure and missing-data behavior

If the source cannot be uploaded, the model does not accept the requested
reference, or the output is incomplete, preserve the failure and return the
smallest supported alternative. Do not silently return a fresh image as though
it were an edit. Retry a failed variant at most once without new user input.
