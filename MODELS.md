# Image model selection guide

MuAPI puts many image models behind one connection. This file is a curated
decision guide, not a frozen copy of the provider catalog. The endpoint names
and schema examples below were checked on **2026-08-28**; re-check the live
schema, `search_models` tool, or current provider documentation before a paid
run.

## Select by job

Choose the operation first, then the model. Preserve fixed product, person,
brand, and text facts with an editing or compositing workflow instead of
expecting a text-to-image model to redraw them perfectly.

| Job | Starting point | REST path example | Main trade-off |
|---|---|---|---|
| Highest-quality text-to-image exploration | GPT Image 2 | `/api/v1/gpt-image-2-text-to-image` | Higher quality/cost tier; verify current account access and price |
| Fast, bounded concept batch | Flux Dev or Flux Schnell | `/api/v1/flux-dev-image` or `/api/v1/flux-schnell-image` | Faster/lower-cost exploration may need more iteration |
| Edit a supplied reference | GPT Image 2 image-to-image | `/api/v1/gpt-image-2-image-to-image` | Requires hosted reference URLs and explicit preservation instructions |
| GPT Image 1.5 edit | GPT Image 1.5 Edit | `/api/v1/gpt-image-1.5-edit` | Current aspect-ratio enum is narrower than GPT Image 2 |
| Open-model or style exploration | Qwen, FLUX, HiDream, Seedream, or another live result | model-specific | Licensing, quality, parameters, and availability differ; verify each model |
| Product/background transformation | Live editing or product-photography model | model/recipe-specific | Preserve the actual SKU; do not generate unsupported product facts |
| Final resolution | MuAPI upscale operation | `/api/v1/ai-image-upscale` | Upscale only the selected candidate; it does not repair bad geometry or text |

These are starting points, not universal rankings. A model is suitable only if
its live schema accepts the required references, aspect ratio, resolution,
quality, and output count.

## Current request-shape examples

### GPT Image 2 text-to-image

The current REST request for `/api/v1/gpt-image-2-text-to-image` requires a
`prompt` and exposes these optional fields:

- `aspect_ratio`: `auto`, `1:1`, `16:9`, `9:16`, `4:3`, or `3:4`;
- `resolution`: `1K`, `2K`, or `4K`;
- `quality`: `low`, `medium`, or `high`;
- `webhook_url` when the host has a secure callback endpoint.

### GPT Image 2 image-to-image

`/api/v1/gpt-image-2-image-to-image` requires `prompt` and `images_list`.
Every item in `images_list` must be a hosted URL accepted by the provider. The
current schema exposes the same aspect-ratio, resolution, and quality families
as text-to-image.

### Flux-style generation

The shared schema behind `/api/v1/flux-dev-image` and
`/api/v1/flux-schnell-image` currently includes `prompt`, `width`, `height`,
`num_images` (1–4 in that schema), `model_id`, and `sync`. Only send fields
that the selected endpoint accepts.

### GPT Image 1.5

`/api/v1/gpt-image-1.5` and `/api/v1/gpt-image-1.5-edit` currently use
`1:1`, `2:3`, and `3:2` aspect ratios. The edit request requires `prompt` and
`images_list`.

For the complete logical-to-MCP/REST map and polling contract, see
[references/muapi-image-tools.md](references/muapi-image-tools.md).

## Model choice by constraint

### Reference fidelity

Use image-to-image/edit when the user says “keep this exact,” “preserve the
product,” “same person,” or “change only.” List invariants explicitly in the
prompt and in the QA checklist. If the model cannot accept the needed reference
count or format, stop and choose a supported model or a post-production path.

### Character or identity consistency

Use a dedicated reference-capable model when the same person, mascot, or
character must recur. Keep identity references separate from general style
references, record their order, and require permission before uploading them.
Do not claim identity consistency from one successful image.

### In-image text and logos

Keep generated copy short. For exact headlines, prices, dates, labels, legal
language, logos, badges, and packaging, prefer a layout/compositing step using
approved source art. Always inspect at full size and thumbnail size.

### Aspect ratio and delivery

Prefer a model that natively supports the target ratio. If the source already
exists, use an edit/reframe workflow for a social crop rather than generating a
new subject. Record the requested ratio and the actual output dimensions in the
receipt.

### Cost and iteration

Use a small low-cost concept batch when the brief is uncertain. Move to a
higher-quality or higher-resolution model only after selecting a direction.
Do not treat a provider recipe's estimated credits or this guide's tier labels
as the settled charge; use returned billing metadata.

## Specialist selection

Specialist skills add domain constraints; they do not replace live schema
validation. Search by the task and required input shape, then verify the
returned model accepts the reference count, operation, ratio, resolution, and
quality fields.

### Professional headshots and group portraits

Use a reference-capable image-to-image or edit model when a real likeness must
remain recognizable. Separate identity references from wardrobe, lighting, and
background references, keep their order stable, and prefer a small consistent
set over a large mixed collection. For group portraits, confirm the provider's
current multi-image limit rather than assuming an application-level limit.

Run a low-count preview first. Check face shape, eyes, hair, skin tone,
accessories, hands, occlusion, expression, and identity drift before any
upscale. A portrait model is not an identity-verification tool.

### Logos and brand identity

Search for models with strong text rendering, sketch/image editing, and clean
shape handling. Use text-to-image for concept families and image-to-image for
an authorized sketch or existing brand direction. Keep exact wordmarks,
registered marks, legal text, and final color values in a layout/vector step
whenever possible. Generated raster art is not proof of vector editability,
originality, or trademark clearance.

### Virtual try-on and product placement

Use an edit or compositing model that can distinguish person, garment, product,
styling, and background roles. Put product invariants in a preservation block:
cut, material, pattern, color, closures, labels, logo, and item count. Do not
select a model solely because it creates attractive people; it must preserve
the item and accept the required inputs.

### Photo restoration

Prefer operation-specific enhancement for denoise, scratch repair, color
correction, and upscale. Use generative edit only for an explicitly requested
reconstruction and record which regions may be inferred. Preserve a conservative
version and the untouched original. Never describe model-invented facial or
historical detail as recovered fact.

### Interior redesign and staging

Use image editing for a real room so walls, doors, windows, floors, fixtures,
and perspective remain anchored. Use text-to-image for a moodboard or fictional
scene where the original geometry is not a claim. Prefer models that accept a
room reference and the requested ratio, and review furniture scale, occlusion,
reflections, and structural drift before labeling a result as a visualization.

### Identity-locked portrait packs

For a themed pack from one portrait, keep the identity reference fixed across
all branches and vary only scene, wardrobe, pose, lighting, or category. Analyze
framing and lighting before generation, but do not replace identity with a
demographic description in the prompt. Use a reference-capable edit model when
likeness is important and review every face independently before delivery.

### Storyboards and multi-angle sets

For storyboards, choose a model that can produce the requested ratio and repeat
a continuity sheet for characters, props, locations, palette, lighting, and
screen direction. Generate frames in beat order even when the calls run in
parallel. For multi-angle reshoots, establish or approve one parent image first,
then branch every angle from that parent rather than chaining a drifted angle.

### UI and design mockups

Choose a model with reliable layout and text behavior for the target platform,
then provide a design specification with components, spacing, typography, color
tokens, responsive intent, and accessibility constraints. Prefer editing a
supplied screenshot for a requested visual change. Review hierarchy, alignment,
contrast, overflow, localization, and placeholder-copy risk; a polished raster
does not certify usability or production readiness.

## Live discovery

When the hosted MCP transport is available, use `search_models` by category or
keyword before selecting a model that is not already in the current shortlist.
For REST-only hosts, inspect the model-specific OpenAPI schema or a current
provider catalog. The public MuAPI recipe registry is also useful for workflow
selection:

```text
GET https://api.muapi.ai/api/v1/agent-skills
GET https://api.muapi.ai/api/v1/agent-skills/{name}
```

Use `ad-creative`, `amazon-product-listing`, `brand-kit`, `social-pack`, and
`youtube-thumbnail` as recipe leads when their inputs match the brief. Fetch
the current recipe body rather than assuming an old prompt or model remains
valid.

## Evidence and provenance

For every generated candidate, record:

- model display name and exact model/endpoint identifier;
- schema verification date and transport;
- operation (text-to-image, image-to-image, edit, enhancement, or upscale);
- prompt or prompt hash, parameters, reference asset IDs and order;
- request ID, status, output URLs, settled billing, and QA result;
- selected parent/child relationship when iterating.

Model quality labels and prices are volatile provider facts. If the live source
does not return a field, report it as `unknown` rather than filling it from
memory or a different model.
