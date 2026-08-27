---
name: Social Pack
slug: social-pack
version: 1.0.0
category: image
description: Reframe one approved hero image into platform-specific social formats while preserving the subject, palette, and visual identity.
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

# Social Pack

## Mission

Turn a selected source image into a bounded set of channel crops or reframes.
Use this skill when the user wants one visual adapted for multiple platforms,
not a new concept for each platform.

## Required inputs

- Approved source image URL or local file.
- Requested formats or platforms.
- Elements that must remain visible and any safe area for copy or UI overlays.
- Optional short caption/overlay direction and channel brand rules.

Common starting formats are `1:1`, `9:16`, `4:5`, and `16:9`; confirm current
platform requirements before delivery rather than treating this list as policy.

## Model selection

Use the editing/reframe entries in [MODELS.md](../../MODELS.md) and the current
schema in [the MuAPI tool reference](../../references/muapi-image-tools.md).
Do not use text-to-image for a simple crop unless the user asks for a creative
recomposition and accepts subject drift.

## Workflow

1. Read the source asset manifest and confirm that it is the approved parent
   image. If local, upload it once and reuse the hosted URL for all formats.
2. Normalize each requested format to a platform label, dimensions, focal
   subject, crop-safe region, text-safe region, and delivery filename.
3. Skip a generation/edit call when the source already matches a requested
   format; return the original asset ID for that format.
4. For each remaining format, call `media.edit_image` with a reframe prompt:
   keep the subject uncropped, match the original lighting/palette, preserve
   identity/product details, and leave the requested safe area.
5. Run independent format branches in parallel when the host supports it.
   State the number of calls and cost signal before execution.
6. Poll and preserve each result. Review subject visibility, hands/faces,
   product geometry, text-safe space, edge artifacts, aspect ratio, and
   platform dimensions.
7. Return the complete pack with the parent-child relationship and any format
   that still needs manual typography or layout work.

## Decision rules

- Reframing is not permission to invent missing sides of a product or crop out
  a required disclosure.
- Keep generated text minimal; add exact copy in post-production when possible.
- Preserve the selected source as the canonical parent. Do not overwrite it.
- A social crop that changes the subject materially should be reported as a new
  creative direction, not as a faithful adaptation.

## Output format

Return one row per format: platform label, ratio/dimensions, asset ID, parent
asset, model/tool, output URL, status, crop/text-safe notes, and receipt link.

## Failure and missing-data behavior

If a format is unsupported or a crop loses a required element, preserve the
source, mark that branch failed or unsuitable, and recommend a supported ratio
or manual layout. Do not silently replace it with a fresh unrelated image.
