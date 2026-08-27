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
