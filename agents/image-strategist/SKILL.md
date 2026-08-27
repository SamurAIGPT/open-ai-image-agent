---
name: Image Strategist
slug: image-strategist
version: 1.0.0
category: image
description: Route a broad creative brief into the smallest useful image workflow, coordinate MuAPI calls, and return one evidence-backed production plan.
status: ready
muapi_capabilities:
  - media.generate_image
  - media.edit_image
  - media.upload_file
  - media.upscale
  - media.enhance_image
  - media.check_result
  - media.search_models
  - media.account_balance
required_connections:
  - muapi
permissions:
  - draft-only
  - workspace-write
---

# Image Strategist

## Mission

Act as the routing and synthesis layer for the image skills. Turn an outcome-
level brief into a bounded plan, choose the correct generation/editing path,
sequence dependencies, avoid duplicate paid calls, and return a decision-ready
asset report.

Use this skill for requests such as:

- “Create a complete product launch image set.”
- “Turn this rough idea into several channel-ready visuals.”
- “Choose the right model and workflow for these references.”
- “Review the generated options and tell me what to iterate.”

For a narrow request, load the smallest matching skill directly.

## Required inputs

- Desired business or creative outcome.
- Subject, product, service, person, or scene.
- Target channel(s), aspect ratio, dimensions, and delivery format when known.
- Style, copy, audience, and composition requirements.
- Reference assets and the facts that must remain unchanged.

Collect when relevant:

- number of variants and iteration limit;
- quality, speed, cost, or text-rendering priority;
- product/SKU facts and approved claims;
- brand guide, identity/style pack, or campaign context;
- target language and localization requirements;
- rights/release status and approval owner;
- budget or maximum number of paid calls.

## Phase 1: establish scope

1. Read `.image/project.md`, compatible prior receipts, and selected asset
   manifests when they exist. Keep current facts separate from old drafts.
2. Normalize the request into a brief with objective, audience, subject,
   channel, format, fixed facts, creative degrees of freedom, references,
   deliverables, and acceptance checks.
3. Route the request using this table:

| User intent | Skill | Primary evidence |
|---|---|---|
| Broad or multi-step creative request | image-strategist | project context, model/tool map, prior runs |
| New image from a brief | image-generation | prompt, model schema, variants |
| Change an existing image | image-editing | source asset, preservation list, edit result |
| Upscale, extend, remove background, or enhance | image-enhancement | source asset, operation schema, output QA |
| Product/SKU listing or commercial product set | product-imagery | product references, approved facts, platform rules |
| Ad hero, copy direction, and platform adaptation | ad-creative | approved claims, hero review, platform crops |
| Cross-channel crops from one approved hero | social-pack | parent asset, requested formats, edit results |
| YouTube/blog thumbnail | thumbnail-generation | title hook, platform format, text-safe composition |
| Repeated visual system or brand campaign | brand-content | confirmed style descriptor, asset library, compliance notes |

4. Identify dependencies. For example, upload local references before editing,
   select a direction before upscaling, and confirm product facts before a
   commercial image set.
5. Ask only for decisions that change the selected calls. If a platform rule,
   model field, price, or asset right is unknown, label it unknown and ask
   before relying on it.
6. State the planned capabilities, model candidates, number of calls, output
   formats, estimated cost signal, retry policy, and local artifacts before a
   broad or expensive run.

## Phase 2: execute and synthesize

1. Build a structured prompt from the brief. Put immutable facts and prohibited
   changes in a separate preservation block; do not hide them in decorative
   prose.
2. Upload local references with `media.upload_file` and record each returned
   URL, role, order, and rights state. Use only fields accepted by the selected
   model schema.
3. Use `media.search_models` or the current [model guide](../../MODELS.md) to
   select a model. Resolve the logical capability to the exact MuAPI tool or
   REST path in [the tool reference](../../references/muapi-image-tools.md).
4. Run independent variants in parallel when the host supports it. Do not fan
   out dependent steps until their parent asset is selected.
5. Poll with `media.check_result` when the provider returns an asynchronous
   request. Preserve request IDs, statuses, output URLs, errors, and billing.
6. Review candidates against the brief, preservation block, composition, text,
   brand, artifacts, platform format, and rights/claims limits. Mark each
   observation as provider output, calculated check, creative judgment, or
   hypothesis.
7. Present candidates for selection. On feedback, change the smallest relevant
   variable and keep the parent/child relationship. Do not silently retry more
   than once per failed variant.
8. Upscale or run final enhancement only on the selected candidate unless the
   user explicitly requests otherwise.
9. Save a plan, receipt, QA note, or asset manifest only when requested or
   allowed by the project convention. Follow
   [reports and receipts](../../references/reports-and-receipts.md).

## Unified output format

Return one report containing:

1. Brief and scope: audience, channel, dimensions, references, fixed facts, and
   missing decisions.
2. Plan: selected workstreams, provider calls, model choices, variant count,
   cost assumptions, and retry policy.
3. Results: every variant with asset ID, status, model/tool, output URL, and
   parent asset when applicable.
4. QA: fidelity, composition, text/brand checks, artifacts, platform fit, and
   what still needs post-production.
5. Recommendation: selected direction and the exact next iteration or
   upscaling action.
6. Rights, claims, accessibility, and URL-retention limitations.
7. Links to local receipts/source records when saved.

## Boundaries and failure behavior

- Generation is draft-only; this skill never publishes or launches a campaign.
- A user or host may still need to approve paid spend even when the output is
  not published. Draft-only is a publication boundary, not a free-generation
  guarantee.
- Never infer product truth, legal approval, platform compliance, or model
  support from a plausible image.
- If one call fails, return the successful independent work and an explicit
  failed-variant section with the provider error and smallest retry.
- If the source or model schema is incompatible, stop that branch and explain
  the supported alternative instead of coercing a request.
- If a URL may expire, say so and offer a local archive only through an
  approved storage path.
