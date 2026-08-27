---
name: Photo Restoration
slug: photo-restoration
version: 1.0.0
category: image
description: Restore damaged, faded, noisy, or low-resolution photographs while distinguishing recovered detail from model reconstruction.
status: ready
muapi_capabilities:
  - media.enhance_image
  - media.upscale
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

# Photo Restoration

## Mission

Improve an old or damaged photograph while preserving its historical content,
people, objects, composition, and visible evidence. Route bounded defects to
enhancement or repair operations, and clearly label any region that has been
reconstructed rather than recovered.

## Required inputs

- Original scan or photograph and permission to process it.
- Desired operations: denoise, deblur, scratch/dust repair, color correction,
  colorization, face/detail recovery, crop repair, or upscale.
- Details that must remain unchanged: people, clothing, objects, text, dates,
  architecture, framing, and relative arrangement.
- Target output size, format, color profile, archive/display use, and quantity.

Collect when relevant:

- a higher-quality scan, alternate scan, or back-of-photo notes;
- whether colorization is wanted or the original monochrome must be preserved;
- regions that may be reconstructed versus regions that must remain untouched;
- historical/family sensitivity, privacy, rights, budget, and reviewer.

## Workflow

1. Inspect the source and classify damage: capture noise, fading, dust,
   scratches, folds, missing pixels, blur, compression, or framing loss. Do not
   promise recovery where the source contains no reliable evidence.
2. Write a `preserve` block for identity, faces, clothing, objects, text,
   architecture, dates, and composition. Write a separate `repair` block for
   the requested defects.
3. Confirm rights and privacy before upload. Record whether the source includes
   recognizable private people, sensitive events, or third-party artwork.
4. Upload the source through `media.upload_file` and choose the narrowest live
   enhancement/edit operation. Use [MODELS.md](../../MODELS.md) and
   [the MuAPI tool reference](../../references/muapi-image-tools.md).
5. State whether the workflow will denoise, repair, colorize, edit, or upscale,
   along with calls, cost signal, and retry policy. Preserve the original
   source unchanged.
6. Run a bounded restoration preview. Poll with `media.check_result` and
   record request ID, status, output, billing, and provider errors.
7. Compare original and output side by side and at full size. Check faces,
   hands, text, edges, patterns, repeated objects, skin, lighting, grain,
   color plausibility, halos, and invented detail.
8. Produce separate variants when useful: conservative restoration,
   colorized restoration, and display upscale. Upscale only a selected version.
9. Mark reconstructed regions and retain the original alongside the output.
   Do not make forensic, historical-authenticity, or identity claims from the
   restored image.

## Decision rules

- Prefer enhancement for bounded cleanup and editing only for an intentional
  reconstruction or crop change.
- Colorization is an interpretation unless the original color information is
  available. Keep a monochrome version when historical fidelity matters.
- A face/detail enhancer can hallucinate features. Do not describe invented
  detail as recovered fact.
- Never overwrite the original or discard a failed restoration.

## Output format

Return the source condition, requested operations, model/tool and parameters,
before/after URLs or paths, variant status, preserved versus reconstructed
regions, QA observations, archive/display limitations, and receipt links.

## Failure and missing-data behavior

If the source is unreadable, the requested repair is unsupported, or the model
would need to invent a material historical detail, pause and explain the
boundary. Preserve failed/partial outputs and recommend a better scan or
manual restoration for the affected region.
