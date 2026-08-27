---
name: Group Photo Compositing
slug: group-photo-compositing
version: 1.0.0
category: image
description: Combine multiple authorized portraits into a coherent group scene while preserving each person's likeness, placement, and consent boundaries.
status: ready
muapi_capabilities:
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

# Group Photo Compositing

## Mission

Create a group portrait from multiple authorized person references: family,
friends, teams, event participants, or fictional characters. Preserve each
subject's recognizable features while composing a requested scene, pose,
camera angle, lighting, and crop.

Use this skill for a group image, not for silently inserting a person into an
unrelated photograph or manufacturing evidence that people were together.

## Required inputs

- One clearly labeled portrait reference per person, within the live model's
  supported reference count.
- Permission to process each recognizable likeness and to combine the people in
  the requested scene.
- Person labels, desired order/placement, relationships, approximate heights
  or pose instructions supplied by the user, and any people who must not be
  placed together.
- Scene, wardrobe, expression, lighting, background, aspect ratio, resolution,
  quantity, and delivery format.

Collect when relevant:

- child/guardian permission and privacy expectations;
- group size, seating/standing arrangement, event or date context, and whether
  the scene is fictional or documentary;
- brand/team rules, approved uniforms, props, accessibility, budget, and
  reviewer.

Do not infer relationships, ages, roles, or consent from the images.

## Reference roles

Assign stable IDs such as `person-01`, `person-02`, and `person-03`. Record for
each:

- source filename or asset ID;
- identity role and order in the request;
- desired placement and pose;
- wardrobe/accessory invariants; and
- rights/consent status.

Keep scene, lighting, and wardrobe references separate from identity sources.

## Model selection

Use a multi-image editing/compositing model that accepts the required number of
references. Check the live schema in
[the MuAPI tool reference](../../references/muapi-image-tools.md) and the
current model guide in [MODELS.md](../../MODELS.md). Do not hard-code a maximum
group size from an old application or recipe.

## Workflow

1. Build a labeled group brief with `preserve`, `arrange`, `change`, and
   `avoid` blocks. State whether the scene is fictional, commemorative, or
   intended to represent a real event.
2. Confirm permission for every recognizable person, including any guardian or
   property permission needed for private references.
3. Upload local portraits once through `media.upload_file`; record the stable
   IDs, order, returned URLs, and roles. Reject an input that is too small,
   ambiguous, or not authorized for the requested use.
4. Choose a live model supporting the reference count, target ratio,
   resolution, quality, and edit operation. Announce the bounded batch, cost
   signal, and review gate.
5. Generate a small set with the group arrangement held stable. Vary only
   scene, lighting, or styling axes that the user asked to compare.
6. Poll with `media.check_result` and preserve every output, request ID, status,
   provider error, and billing object.
7. Review each person independently for face, hair, skin tone, eyewear,
   clothing, hands, limb count, occlusion, scale, and expression. Then review
   group spacing, contact shadows, eye lines, lighting, perspective, and scene
   plausibility.
8. Upscale or reframe only the selected group image. Label a fictional or
   reconstructed scene clearly and do not present it as documentary evidence.

## Safety and quality boundaries

- Do not create non-consensual intimate imagery, deceptive event evidence, or
  identity documents.
- Do not merge identities, swap faces, or alter a subject's age/body without
  explicit direction and a rights review.
- Do not infer family, romantic, employment, political, medical, or other
  sensitive relationships from a group arrangement.
- Generated team uniforms, logos, awards, captions, dates, and claims need
  approved source art and human verification.

## Output format

Return a person-by-person reference map, group arrangement, model/tool and
parameters, output URLs/status, likeness and compositing QA, fictional/event
label, unresolved rights or text issues, and receipt links.

## Failure and missing-data behavior

If the provider rejects the reference count or a subject cannot be preserved,
split the work into supported groups or recommend manual compositing. Preserve
the failed/partial variant and never silently omit a person.
