---
name: Product Imagery
slug: product-imagery
version: 1.0.0
category: image
description: Plan and produce truthful ecommerce or commercial product-image sets from approved SKU references, with channel-specific QA and provenance.
status: ready
muapi_capabilities:
  - media.generate_image
  - media.edit_image
  - media.upload_file
  - media.upscale
  - media.check_result
required_connections:
  - muapi
permissions:
  - draft-only
  - workspace-write
---

# Product Imagery

## Mission

Create a useful product-image set without allowing visual polish to change what
the customer is buying. This skill is for ecommerce listings, product pages,
catalogs, and commercial campaigns.

## Required inputs

- Product name, SKU/variant, and purchasable quantity.
- Approved product photos, packshots, label/packaging art, or a product sheet.
- Product facts that must remain true: shape, dimensions, material, finish,
  color, logo, controls, included components, and packaging.
- Target channel/category, audience, deliverables, and required formats.

Collect when relevant:

- approved claims and prohibited claims;
- primary-image versus secondary/lifestyle/infographic requirements;
- brand guide, art direction, and background preferences;
- model/property release and asset-license state;
- dimensions, scale references, accessibility/alt-text needs, budget, and
  approval owner.

## Model selection

Use [MODELS.md](../../MODELS.md) and [the MuAPI tool reference](../../references/muapi-image-tools.md).
If a public MuAPI recipe such as `amazon-product-listing` matches the brief,
use it as a workflow lead but re-check its current inputs, model, cost, and
platform rules before execution.

## Workflow

1. Read `.image/project.md` and prior product manifests. Confirm the exact SKU
   and separate observed product facts from creative choices.
2. Split the deliverable into channel-specific roles: clean primary, lifestyle
   context, scale/dimensions, feature/detail, packaging, or approved
   comparison. Do not assume a single image can satisfy all roles.
3. Inspect source coverage. Ask for missing views or mark the result as a
   concept/mockup when the supplied reference cannot establish the product's
   hidden sides, material, color, or scale.
4. For a source-based visual, upload the reference via `media.upload_file` and
   prefer editing/product-photography paths that preserve the actual item. Use
   text-to-image for a scene only when it will not be presented as a verified
   product fact.
5. Use approved label, logo, packaging, price, certification, and copy assets
   through compositing or post-production where possible. Do not ask the model
   to invent them.
6. State the planned images, calls, model choices, cost signal, and review gate
   before a parallel batch. Run independent roles in parallel only after the
   product facts and channel scope are confirmed.
7. Poll and record every variant. Compare product geometry, color, label,
   included quantity, scale, shadows, reflections, and text against the source.
8. Upscale only selected candidates. Return an approval checklist and flag
   anything requiring platform or compliance review.

## Decision rules

- Product truth outranks aesthetics. If the output changes the SKU, label,
  material, quantity, dimensions, or included accessories, it is not a final
  product image.
- Health, beauty, wellness, environmental, safety, comparative, discount,
  certification, rating, and endorsement claims require approved wording and
  review. Visual implication counts as a claim risk.
- Platform requirements are volatile. Check the current official rules for the
  target category, locale, and placement before delivery.
- Keep actual product imagery separate from conceptual campaign imagery.

## Output format

Return a channel/role table with asset ID, source references, model/tool,
dimensions, output URL, status, product-fidelity observations, claims/platform
limitations, alt-text guidance, and receipt links.

## Failure and missing-data behavior

If product facts or references are incomplete, ask only the questions needed to
protect product truth and label any concept output clearly. If one role fails,
return the independent roles and an explicit failed section; never fill a
missing product view with an invented variant.
