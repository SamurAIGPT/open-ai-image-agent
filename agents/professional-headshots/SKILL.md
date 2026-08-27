---
name: Professional Headshots
slug: professional-headshots
version: 1.0.0
category: image
description: Produce consent-based professional portrait and headshot sets from authorized identity references, with controlled styling and identity QA.
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

# Professional Headshots

## Mission

Create a coherent set of professional portraits for LinkedIn, team pages,
speaker profiles, resumes, creator profiles, or personal branding. Preserve the
person's recognizable identity while allowing controlled changes to wardrobe,
lighting, pose, crop, and background.

This is a portrait-production workflow, not an identity-verification or
document-photo workflow. The result is a draft until the subject approves it.

## Required inputs

- Intended use: LinkedIn, company profile, speaker bio, resume, portfolio, or
  another placement.
- Authorized identity references and the subject's permission to process them.
- Identity details that must remain stable: face shape, skin tone, hairline,
  distinctive features, eyewear, facial hair, and any required accessories.
- Desired wardrobe, expression, pose, lighting, background, crop, aspect ratio,
  resolution, quantity, and delivery format.

Collect when relevant:

- age range and representation preferences;
- employer or brand rules, approved logo use, and prohibited alterations;
- whether the subject wants a natural photograph, studio portrait, or stylized
  professional look;
- localization, retouching boundaries, reviewer, budget, and iteration limit.

Do not infer age, ethnicity, job title, credentials, employer, or identity from
an image. Ask for those facts when they materially affect the brief.

## Reference roles

Use a small, consistent identity set accepted by the live model schema. Label
each asset as one of:

- `identity-primary`: the clearest face and overall likeness reference;
- `identity-support`: additional angles or expressions for likeness;
- `wardrobe`: clothing or styling reference, not a replacement identity;
- `background`: location or lighting reference; or
- `brand`: an authorized color, logo, or visual-system reference.

Do not mix multiple people's identity references without explicit group-photo
intent. Do not use a private face pack for an unrelated request.

## Model selection

Use the portrait and reference-capable entries in
[MODELS.md](../../MODELS.md) and the live contract in
[the MuAPI tool reference](../../references/muapi-image-tools.md). Prefer
image-to-image/edit when likeness must remain stable. Use text-to-image only
for a clearly labeled concept or when the provider supports the required
identity references.

## Workflow

1. Read `.image/project.md` and prior selected portraits when available. Keep
   current subject facts separate from old drafts.
2. Confirm the subject's permission and the permitted use of every likeness,
   wardrobe, logo, and location reference before uploading anything.
3. Build a portrait brief with `preserve`, `change`, `avoid`, and `delivery`
   blocks. State whether retouching may change skin texture, hair, teeth,
   facial hair, body shape, or age presentation.
4. Upload local inputs once through `media.upload_file`, record their roles and
   order, and pass only hosted URLs accepted by the selected model.
5. Select a live model that supports the required reference count, aspect
   ratio, resolution, and quality. State the planned calls, variant count,
   cost signal, and approval gate before execution.
6. Generate a small set of distinct directions: for example, studio neutral,
   warm editorial, and industry-specific. Keep identity instructions stable so
   the variants can be compared.
7. Poll with `media.check_result` and record every request ID, status, output,
   billing object, and provider error.
8. Review each output against likeness, anatomy, eyes, teeth, hands, hair,
   wardrobe, accessories, lighting, background, crop, and requested
   retouching boundaries. Mark subjective style judgments separately from
   observed drift.
9. Upscale or reframe only the selected candidate. Return it to the subject for
   approval before treating it as a public profile asset.

## Safety and quality boundaries

- Do not create deceptive impersonation, non-consensual intimate imagery, or
  official identity, passport, visa, license, or employment-document photos.
- Do not promise that a portrait proves a person's identity, credentials, job,
  age, health, or real-world appearance.
- Do not materially alter a person's age, body, skin, or features without
  explicit direction and a clear note in the handoff.
- Flag celebrity/public-figure likeness requests and any request involving a
  person who has not authorized processing.
- Treat generated text, logos, employer marks, and credentials as unverified;
  use approved layout assets for exact copy.

## Output format

Return a table containing:

- portrait direction and intended placement;
- identity/reference roles and rights status;
- model/tool, parameters, and output dimensions;
- output URL, asset ID, request status, and receipt link;
- observed likeness preservation and unintended drift;
- retouching, text, brand, accessibility, and post-production notes; and
- subject-approval status and the next smallest iteration.

## Failure and missing-data behavior

If the reference set is unclear, rights are missing, or the selected model
cannot support the requested likeness workflow, pause before a paid call. If a
variant drifts or fails, preserve it as failed/partial and return the smallest
supported alternative; never silently substitute a generic person's face.
