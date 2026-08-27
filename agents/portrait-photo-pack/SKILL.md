---
name: Portrait Photo Pack
slug: portrait-photo-pack
version: 1.0.0
category: image
description: Generate a themed pack of portraits from an authorized identity reference while locking likeness and varying only the requested scene or styling.
status: ready
muapi_capabilities:
  - media.edit_image
  - media.generate_image
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

# Portrait Photo Pack

## Mission

Turn one authorized portrait reference into a coherent set of themed photos:
professional, creator, travel, editorial, seasonal, lifestyle, or another
user-defined category. Keep identity as the primary invariant and vary only the
scene, wardrobe, pose, lighting, and visual treatment that the user requests.

This skill creates a creative portrait pack. It is not an identity-verification,
official-document, or evidence-generation workflow.

## Required inputs

- One clear identity reference and permission to process the likeness.
- Pack category or categories and intended use.
- Number of images, target formats, aspect ratios, resolution, and delivery
  format.
- Requested scene, wardrobe, pose, lighting, mood, and style changes.
- Face, body, clothing, accessories, and retouching details that must remain
  unchanged.

Collect when relevant:

- additional support references and their roles;
- privacy, age, public-figure, model-release, and reviewer requirements;
- brand or platform rules, localization, budget, and iteration limit.

## Identity-lock protocol

Analyze the image for scene attributes only before generation:

- head orientation and camera angle;
- expression and gaze direction;
- framing and visible body region;
- lighting direction, contrast, and background relationship; and
- pose or interaction that needs continuity.

Do not replace the source identity with a demographic description. Keep a fixed
identity block in every prompt:

```text
Use the supplied image as the identity source. Preserve the exact facial
identity, face proportions, eye shape and spacing, nose, jawline, chin,
cheekbones, skin tone, hairline, and distinctive features. Do not create a new
person or beautify the face. Change only the requested scene and styling.
```

Use a negative constraint block when the selected model supports it or include
the constraints in natural language:

```text
different person, altered facial structure, changed eye spacing, generic face,
face distortion, plastic skin, unintended age change, unintended body change
```

## Workflow

1. Confirm the source is readable and the subject has authorized the requested
   use. Do not reuse a private identity pack for an unrelated person or project.
2. Build a category matrix with one row per image: scene, action/pose,
   composition, lighting, wardrobe, requested change, and preservation block.
3. Upload the identity source once through `media.upload_file` and record its
   role/order. Add support references only when the live model schema accepts
   them and their role is unambiguous.
4. Choose a reference-capable edit model when likeness is critical. Use
   generation only when the selected model explicitly supports the identity
   reference. Verify the live schema in [MODELS.md](../../MODELS.md) and
   [the MuAPI tool reference](../../references/muapi-image-tools.md).
5. State the category count, calls, model, cost signal, and review gate. Run a
   small preview across categories before generating a large pack.
6. Submit independent image branches in parallel when supported. Keep the
   identity block and source order unchanged across branches.
7. Poll with `media.check_result`; preserve request IDs, statuses, outputs,
   billing, and provider errors for every image.
8. Review likeness, anatomy, eyes, hands, hair, clothing, accessories,
   lighting, background, crop, and retouching boundaries. Mark any identity
   drift or generated text as a failure/limitation.
9. Upscale only selected images. Return the pack with category labels and a
   subject-approval checkpoint.

## Safety and quality boundaries

- Do not create deceptive impersonation, non-consensual intimate imagery, or
  official identity/passport/license/employment-document photos.
- Do not claim that a generated portrait proves identity, age, credentials,
  occupation, health, or real-world appearance.
- Do not materially change age, body, skin, or facial features without explicit
  direction and disclosure.
- Treat logos, employer marks, names, and copy as unverified unless supplied as
  approved layout assets.

## Output format

Return a pack table with category, scene, identity/reference roles, model/tool,
parameters, output URL/status, asset ID, likeness QA, requested versus
unintended changes, approval state, and receipt links.

## Failure and missing-data behavior

If no authorized source is supplied, rights are unclear, or the model cannot
accept the required reference, pause before a paid call. If one branch drifts
or fails, preserve it and return the other results without silently substituting
a generic face.
