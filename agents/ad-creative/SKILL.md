---
name: Ad Creative
slug: ad-creative
version: 1.0.0
category: image
description: Plan and generate a conversion-oriented image-ad set in two phases: approve a hero concept and copy direction, then fan it out into platform formats.
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

# Ad Creative

## Mission

Turn a product or service brief into a reviewable ad-creative set. Separate
concept development from platform adaptation so the user can approve the
message and hero direction before more paid variants are generated.

## Required inputs

- Product/service and the actual benefit the ad may communicate.
- Target audience, campaign goal, and intended platforms/placements.
- Brand style, approved copy/claims, and optional product/reference image.
- Required formats, variant count, budget, and review owner.

Collect when relevant:

- landing-page or offer facts, CTA, price, date, and disclosure requirements;
- product/SKU preservation rules and source asset rights;
- audience language/localization and platform safe areas;
- performance data only when it is supplied by an authorized source.

## Model selection

Use [MODELS.md](../../MODELS.md) and the live MuAPI contract in
[references/muapi-image-tools.md](../../references/muapi-image-tools.md). Use
editing when a supplied product or source image must remain recognizable. A
public MuAPI `ad-creative` recipe is a useful reference, but the current model,
fields, cost, and platform constraints must be verified before execution.

## Workflow

### Phase A: hero and message

1. Read `.image/project.md` and confirm product facts, audience, brand style,
   approved claims, and rights for all references.
2. Extract one honest audience problem or opportunity and propose two or three
   visual directions. Each direction should change one major creative variable:
   hook, setting, subject treatment, or composition.
3. Draft a small copy set: headline (short), supporting line, and CTA. Mark
   every factual or performance claim as approved, unsupported, or requiring
   review. Never invent social proof, ratings, savings, endorsements, or
   urgency.
4. Choose a square or other universal starting format, state model/calls/cost
   signal, and generate one hero candidate per approved direction.
5. Poll and record every result. Review product/brand fidelity, content truth,
   visual hierarchy, crop safety, text, and artifacts.
6. Present the hero candidates and copy options. Stop and obtain the user's
   direction before Phase B.

### Phase B: platform adaptation

1. Use the selected hero as the parent asset. Confirm the chosen copy and each
   platform's current placement requirements.
2. For each requested format, use `media.edit_image` to reframe the parent;
   preserve the product/subject, palette, and lighting and leave space for
   exact copy to be added in post-production.
3. Run independent format branches in parallel when the host supports it.
4. Poll and preserve parent/child relationships, parameters, statuses, URLs,
   errors, billing, and QA notes.
5. Return the platform set with recommended overlay placement, remaining
   manual layout, claims/disclosure review, and approval status. Do not launch
   or publish the ads.

## Decision rules

- Conversion intent does not justify unsupported claims or manipulative
  imagery. Product truth and substantiation outrank visual impact.
- Change one major variable per first-round concept so the user can compare
  the result meaningfully.
- Do not regenerate the parent for a simple crop. If reframing materially
  changes the subject, report it as a new concept.
- Keep exact copy, price, dates, logos, legal disclosures, and badges in an
  approved post-production layout whenever possible.
- Performance data can inform a variation only when the source, date range,
  metric, and significance are known; do not infer an underperformer from a
  creative impression.

## Output format

Return:

- campaign scope and approved facts/claims;
- Phase A direction, copy options, model/tool, prompt, output URL/status, and
  QA notes;
- the user's selected hero/copy checkpoint;
- Phase B format table with platform, dimensions, parent asset, output URL,
  status, overlay guidance, disclosure/claims notes, and receipt links;
- failed branches, post-production work, and approval limitations.

## Failure and missing-data behavior

If product facts, approved claims, source rights, or platform scope are missing,
pause before paid generation and ask for the minimum required decisions. If a
branch fails, preserve it with the provider error and continue only with
independent branches. Never auto-confirm Phase B or auto-publish.
