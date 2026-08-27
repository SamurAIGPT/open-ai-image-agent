---
name: Virtual Try-On
slug: virtual-try-on
version: 1.0.0
category: image
description: Create clearly labeled garment-on-person visualization drafts while preserving authorized person and garment details.
status: ready
muapi_capabilities:
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

# Virtual Try-On

## Mission

Visualize an authorized garment, accessory, or styling item on an authorized
person reference for fashion planning, catalog concepts, merchandising, or
customer previews. Preserve the garment's material, cut, print, color, logo,
and construction as far as the live model allows.

The output is a simulation, not proof of fit, size, comfort, fabric behavior,
or a product's appearance on every body.

## Required inputs

- Person image and permission to process the likeness.
- Garment/accessory image and permission to use the product asset.
- Which image is the person, which is the item, and whether either is only a
  pose, lighting, or background reference.
- Desired pose, styling, scene, crop, aspect ratio, resolution, and quantity.
- Product facts that must remain stable: color, pattern, material, closures,
  sleeves, neckline, silhouette, logo, and item count.

Collect when relevant:

- size/fit intent supplied by the user rather than inferred by the model;
- background, lighting, season, target market, language, and catalog rules;
- whether the result is a private concept, marketplace image, or ad draft;
- rights, consent, reviewer, budget, and post-production plan.

## Reference roles

Label inputs explicitly:

- `person`: likeness, pose, body context, and face;
- `garment`: the item to place or preserve;
- `styling`: optional shoes, accessories, hair, or palette;
- `background`: scene or lighting only; and
- `layout`: crop or catalog composition only.

Do not pass unrelated identity references as styling images. Do not infer a
person's size, health, age, ethnicity, or attractiveness from the source.

## Model selection

Use a live image-to-image or virtual-try-on-capable model from
[MODELS.md](../../MODELS.md) and verify its current input shape in
[the MuAPI tool reference](../../references/muapi-image-tools.md). Upload local
files through `media.upload_file` and preserve reference order.

## Workflow

1. Inspect the person and item sources. Write separate `person-preserve`,
   `garment-preserve`, `change`, and `avoid` blocks.
2. Confirm likeness/product rights and whether every recognizable person has
   authorized the processing. Require guardian/owner permission for minors or
   private subjects.
3. Upload each source once, record its role and hosted URL, and choose a model
   that supports the required number of inputs, target ratio, and output size.
4. State the planned calls, variant count, cost signal, and simulation label
   before execution. Start with one pose and a small number of variants.
5. Use `media.edit_image` with explicit preservation instructions. Do not ask a
   model to invent the product label, price, size, material certification, or
   performance claim.
6. Poll with `media.check_result`. Preserve output URLs, request IDs, status,
   errors, billing, and partial results.
7. Compare the output to both source assets. Check face/hand anatomy, pose,
   garment boundaries, seams, patterns, closures, logos, skin/hair occlusion,
   shadows, reflections, and background edges.
8. Return the selected simulation with a prominent fit/product disclaimer and
   send exact labels, claims, and final catalog layout to post-production.

## Safety and quality boundaries

- Do not create sexualized imagery of minors or non-consensual intimate edits.
- Do not claim actual size, fit, color accuracy, material performance, or body
  measurements from a generated preview.
- Do not alter a person's identity or body beyond the requested garment
  visualization without explicitly disclosing the change.
- Treat logos, labels, badges, prices, and claims as approved source art, not
  generated facts.
- Keep a commercial listing image separate from an aspirational campaign
  concept.

## Output format

Return a table with person and garment asset roles, model/tool, parameters,
simulation label, output URL/status, product and likeness observations, fit and
claim limitations, QA notes, and receipt links.

## Failure and missing-data behavior

If either source is missing, unauthorized, incompatible, or too ambiguous to
preserve, pause before a paid call. If the garment changes materially or the
person drifts, mark the result as failed/partial and recommend a better source,
supported model, or manual compositing path.
