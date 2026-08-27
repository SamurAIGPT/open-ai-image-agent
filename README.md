# AI Image Agent

> A portable, MuAPI-backed creative production agent for image generation,
> editing, portraits, product imagery, try-on, restoration, thumbnails, and
> on-brand visual systems.

This repository turns image-production workflows into selective agent skills.
It is designed for Claude Code, Codex, Cursor, Windsurf, Claude.ai, or any
agent host that can load Markdown and connect tools. It is not a hosted app and
does not run an agent runtime of its own.

## Why use it?

The pack adds the operating layer around an image API:

- turns an unstructured brief into a concrete image plan;
- collects platform, asset, rights, budget, and product-fact inputs before a
  paid call;
- selects a model using the live MuAPI schema instead of a permanent default;
- uploads local references, records their roles, and preserves iteration
  relationships;
- creates independent variants in parallel when the host supports it;
- checks fidelity, composition, text, brand constraints, and delivery specs;
- returns failed or partial variants explicitly instead of silently dropping
  them; and
- records receipts so a result can be reviewed or reproduced later.

The host assistant supplies the reasoning and tool loop. These Markdown skills
provide the routing rules, input contracts, quality gates, and handoff format.

## What you can ask it to do

- “Create four hero-image directions for this product launch. Keep the first
  round under my budget and return the prompts and model choices.”
- “Use this product photo to create a clean primary image, two lifestyle shots,
  and a dimensions graphic. Do not change the product or invent claims.”
- “Edit this image to remove the background but preserve the person, clothing,
  logo, and lighting.”
- “Turn this approved hero into square, portrait, vertical, and wide social
  versions without regenerating the subject.”
- “Make three thumbnail concepts for this title and leave safe space for the
  final text overlay.”
- “Create an on-brand campaign set from our style guide and reference assets;
  flag anything that deviates from the palette.”
- “Compare two image models for this brief, run a small draft batch, and show
  me the tradeoffs before any larger spend.”
- “Create three professional headshot directions from my authorized photos.
  Preserve my identity and give me LinkedIn and speaker-profile crops.”
- “Use this garment and person photo to make a try-on preview. Preserve the
  pattern and label it clearly as a visualization, not a fit guarantee.”
- “Restore this family photograph conservatively, keep the original, and mark
  any reconstructed detail.”

## Use it with your AI assistant

The repository is a Markdown skill pack. Keep `AGENTS.md` available to the
host and load only the skill needed for the current task, unless the request
spans several stages.

| Host | Recommended setup |
|---|---|
| Claude Code | Keep `AGENTS.md`, install selected folders under `.claude/skills/`, and connect the MuAPI MCP server over stdio. |
| Codex | Open the repository context, load `AGENTS.md` plus the selected `SKILL.md`, and use the host's MuAPI connection. |
| Cursor or Windsurf | Add the selected skill directory to the project context and configure MuAPI as an MCP integration. |
| Claude.ai | Upload `AGENTS.md` and the relevant skill or use a connected hosted MCP server. |
| Another Markdown-capable host | Preserve each skill's directory and `SKILL.md`, then map the logical operations in the MuAPI guide to the host's tools. |

The assistant should always report the concrete model, operation, request ID,
outputs, and any failed variants. It should ask for missing high-impact
inputs rather than guessing product facts, legal status, or brand rules.

## Quick start

### 1. Install the pack

Clone or download this repository, or install all skills with a compatible
skills installer:

```sh
npx skills add SamurAIGPT/open-ai-image-agent --all
```

For a focused setup, install a single skill instead:

```sh
npx skills add SamurAIGPT/open-ai-image-agent --skill image-generation
```

If the host does not support that installer, copy `AGENTS.md` and the desired
`agents/<skill-name>/` directory into the host project.

### 2. Connect MuAPI

Configure the MuAPI MCP server or use the REST fallback. Hosted MCP and local
stdio MCP expose different upload shapes, so follow
[the MuAPI setup guide](https://muapi.ai/docs/mcp) and the local
[installation guide](references/agent-installation.md).

Do not place API keys in prompts, receipts, committed files, or image metadata.

### 3. Load the right skill

For a broad brief, load `AGENTS.md`,
[Image Strategist](agents/image-strategist/SKILL.md), and the guides it names.
For a narrow request, load only the matching skill from the table below.

### 4. Give the assistant a usable brief

Include the goal, audience, subject, required format, dimensions or platform,
reference assets and their intended roles, brand constraints, rights status,
quantity, deadline, and spend limit. Say whether the output is a draft or an
approved production asset.

### 5. Validate the package

Run the dependency-free check before sharing or installing changes:

```sh
python3 scripts/validate_package.py
```

### Example first request

```text
Create three draft hero directions for our insulated travel mug.
Audience: commuters. Use the attached product photo as a fidelity reference.
Output: 16:9 web hero, plus a square crop-safe direction. Preserve the exact
logo and lid shape, avoid unsupported performance claims, and keep the first
round within 12 credits. Return the selected model, prompts, request IDs,
output URLs, failed variants, and a recommendation for the next round.
```

## Image workflows

| Workflow | Use it for | Expected handoff |
|---|---|---|
| [Image Strategist](agents/image-strategist/SKILL.md) | Route a broad brief across multiple image stages. | Plan, assumptions, budget gate, skill sequence, and acceptance criteria. |
| [Image Project Setup](agents/image-project-setup/SKILL.md) | Establish brand, asset, platform, rights, and approval context. | Project context and asset manifest. |
| [Image Generation](agents/image-generation/SKILL.md) | Create new images from a prompt or structured brief. | Model choice, prompt, parameters, outputs, and QA notes. |
| [Image Editing](agents/image-editing/SKILL.md) | Modify an existing image while preserving selected details. | Input roles, edit instruction, fidelity checks, and variants. |
| [Image Enhancement](agents/image-enhancement/SKILL.md) | Upscale, remove a background, extend a canvas, or improve a source. | Enhancement operation, before/after details, and delivery checks. |
| [Product Imagery](agents/product-imagery/SKILL.md) | Build a SKU, catalog, marketplace, or lifestyle image set. | Shot list, product invariants, claims checks, and asset matrix. |
| [Professional Headshots](agents/professional-headshots/SKILL.md) | Create consent-based LinkedIn, executive, team, speaker, or personal-brand portraits. | Identity roles, style directions, likeness QA, and subject approval. |
| [Logo and Brand Identity](agents/logo-and-brand-identity/SKILL.md) | Explore logos, wordmarks, symbols, and compact identity boards. | Concept families, legibility review, vector handoff, and trademark caveat. |
| [Virtual Try-On](agents/virtual-try-on/SKILL.md) | Visualize an authorized garment or accessory on a person. | Person/item roles, product fidelity, simulation label, and fit limitations. |
| [Group Photo Compositing](agents/group-photo-compositing/SKILL.md) | Combine several authorized portraits into one scene. | Person map, arrangement, consent, likeness QA, and fictional/event label. |
| [Photo Restoration](agents/photo-restoration/SKILL.md) | Repair, colorize, clean, or upscale old and damaged photographs. | Damage map, conservative version, reconstructed regions, and archive notes. |
| [Interior Redesign](agents/interior-redesign/SKILL.md) | Declutter, redesign, or stage an authorized room photograph. | Room geometry map, style variants, visualization label, and property QA. |
| [Ad Creative](agents/ad-creative/SKILL.md) | Develop ad concepts, visual hooks, and platform-ready variants. | Concept directions, copy-safe layout notes, and test matrix. |
| [Social Pack](agents/social-pack/SKILL.md) | Reframe one approved visual for several social placements. | Shared-source variants with platform dimensions and crop checks. |
| [Thumbnail Generation](agents/thumbnail-generation/SKILL.md) | Create YouTube, blog, podcast, or editorial thumbnail concepts. | Attention hook, safe area, text plan, and variant comparison. |
| [Brand Content](agents/brand-content/SKILL.md) | Produce a repeatable set from an approved visual identity. | Brand inputs, reusable prompt system, outputs, and deviation flags. |

## Connect MuAPI

The skills use logical `media.*` capabilities so the planning layer remains
stable when the provider catalog changes. The current mapping is documented in
[the MuAPI image-tools guide](references/muapi-image-tools.md).

| Logical capability | MCP operation | REST fallback |
|---|---|---|
| `media.generate_image` | `muapi_image_generate` | Submit to the selected image model endpoint. |
| `media.edit_image` | `muapi_image_edit` | Submit to the model's image-to-image or edit endpoint. |
| `media.upload_file` | `muapi_upload_file` over stdio, or `muapi_upload_image` for hosted base64 input | `POST /api/v1/upload_file` |
| `media.upscale` | `muapi_enhance_upscale` | `POST /api/v1/ai-image-upscale` or the live upscale endpoint. |
| `media.enhance_image` | `muapi_enhance_bg_remove` and related enhancement tools | Use the selected enhancement endpoint. |
| `media.check_result` | `muapi_predict_result` | `GET /api/v1/predictions/{request_id}/result` |
| `media.search_models` | `search_models` | Read the provider's current model/schema catalog. |
| `media.account_balance` | `muapi_account_balance` | Use the provider account endpoint available to the host. |

The REST fallback submits to a model-specific `/api/v1/{model-slug}` path,
uploads local files through `/api/v1/upload_file`, and polls the prediction
result endpoint. The live schema is authoritative; model availability,
fields, prices, limits, and output URLs can change.

The image skills should use the narrowest operation that matches the brief:

- text-to-image for a new scene or concept;
- image-to-image or edit for a source that must remain recognizable;
- enhancement for quality or canvas changes that should not redesign the
  subject; and
- a multi-step plan when generation, cleanup, reframing, and delivery are all
  required.

## Model selection and workflow recipes

[MODELS.md](MODELS.md) is a curated selection guide, not a frozen copy of the
provider catalog. The assistant should use live model search or schema data
when available and record the model identifier actually used.

Selection should consider:

- whether the task is text-to-image, editing, enhancement, or compositing;
- reference-image support and the required level of subject fidelity;
- aspect ratio, resolution, quality, and output-count requirements;
- typography, logo, and fine-detail sensitivity;
- latency, retry tolerance, and the user's spend limit; and
- whether the result is a draft exploration or a final candidate.

MuAPI's workflow recipes can be useful planning hints for common deliverables,
including ads, product listings, brand kits, social packs, and thumbnails.
Their estimated credits are not a quote: settled provider billing is the
source of truth.

## Costs, batching, and approvals

Image generation and enhancement may incur provider charges. Before a paid
call, the assistant should:

- identify the operation and model;
- state the expected number of outputs and any estimated credit range;
- check the available balance when the host exposes it;
- confirm whether the user wants exploration, a constrained draft batch, or a
  production candidate; and
- stop for approval when the requested spend is ambiguous or exceeds the
  stated limit.

The default strategy is a small, diverse draft batch followed by selection and
targeted iteration. Independent variants may run in parallel, but retries must
be bounded and reported. A failed or partial result is part of the receipt;
it must not be presented as a successful output.

Publishing to an ad account, storefront, social channel, or CMS is outside the
scope of this pack and always requires a separate explicit action.

## External image coverage

The pack covers the planning and handoff layer for these common image tasks:

- prompt-based text-to-image exploration;
- reference-guided generation and image-to-image editing;
- targeted edits that preserve a product, person, logo, or composition;
- professional headshots, team portraits, and speaker/profile imagery;
- multi-person portrait compositing with consent and identity checks;
- garment and accessory try-on visualizations;
- logo, wordmark, and compact brand-identity exploration;
- conservative photo restoration and historical-image cleanup;
- room decluttering, interior redesign, and property-staging concepts;
- upscaling and quality enhancement;
- background removal, canvas extension, and other cleanup operations;
- product listing, catalog, and lifestyle image sets;
- advertising concepts and platform variants;
- social-format reframing from an approved source;
- YouTube, blog, podcast, and editorial thumbnails; and
- repeatable brand-content production with deviation checks.

Actual model support, input limits, output retention, and tool availability
depend on the connected MuAPI transport and live provider catalog.

## Reports and saved work

For repeatable work, the host may keep local context and receipts under
`.image/`. The format is documented in
[reports and receipts](references/reports-and-receipts.md):

```text
.image/
  project.md
  assets/<asset-id>.json
  runs/YYYY-MM-DD/<run-id>/plan.md
  runs/YYYY-MM-DD/<run-id>/receipt.json
  runs/YYYY-MM-DD/<run-id>/qa.md
```

A receipt should preserve the logical capability, concrete provider operation,
model, sanitized request, reference roles, request ID, status, output URLs,
billing, and QA or iteration notes. It should never contain API keys or raw
reference bytes.

The assistant should return a compact handoff containing:

1. what was requested and what assumptions were made;
2. the model, parameters, and input roles;
3. successful outputs with URLs or local paths;
4. failed, skipped, or partial variants with the reason;
5. QA findings and recommended next action; and
6. the receipt location or equivalent audit record.

## Quality, privacy, and rights

Before final commercial or public use, follow
[the creative QA checklist](references/creative-qa.md). At minimum, verify:

- product shape, color, packaging, dimensions, labels, and other factual
  details;
- logos, names, faces, hands, text, and model artifacts;
- claims, regulated categories, disclosures, and platform requirements;
- consent, licenses, model releases, and the permitted use of references;
- accessibility, legibility, safe areas, dimensions, file format, and crop
  behavior; and
- approval state and the person responsible for final sign-off.

Treat uploaded assets as sensitive by default. Use only assets the user is
authorized to process, minimize retained copies, avoid secrets in prompts and
logs, and do not assume that a provider output is private or permanently
available.

A plausible image is not proof that every visible fact is correct. Human review
and post-production are required for claims, logos, labels, legal copy, and
high-stakes or public-facing use.

## Example workflows

### New campaign hero

1. Load Image Strategist and Image Project Setup.
2. Capture the audience, channel, dimensions, product facts, brand rules,
   rights, and budget.
3. Generate a small set of distinct directions with Image Generation.
4. Evaluate composition, fidelity, text risk, and crop safety.
5. Iterate only the selected direction and save the receipt.

### Product listing set

1. Upload the product source and label it as a fidelity reference.
2. Build a shot list with Product Imagery: primary, detail, lifestyle, scale,
   and dimensions where needed.
3. Keep product invariants explicit in every edit or generation step.
4. Run QA for packaging, claims, dimensions, background, and marketplace
   requirements.
5. Return an asset matrix with successful and incomplete shots clearly marked.

### Ad concept test

1. Use Ad Creative to define several visual hooks and a copy-safe layout.
2. Generate only enough variants to compare the hooks.
3. Reuse the strongest source with Social Pack for placement variants.
4. Record the model, prompt family, spend, output URLs, and test labels.
5. Keep publishing and performance decisions outside the image-generation run.

### Professional headshot set

1. Confirm the subject's permission, intended placement, identity invariants,
   wardrobe preferences, and retouching boundaries.
2. Upload a small labeled identity set and choose a reference-capable model.
3. Generate a bounded set of studio, editorial, or industry-specific directions.
4. Review likeness, anatomy, clothing, crop, background, and unintended age or
   body changes.
5. Get subject approval before delivery and upscale only the selected portrait.

### Logo or identity exploration

1. Capture exact brand spelling, applications, audience, tone, colors, and
   prohibited motifs.
2. Generate several concept families, keeping wordmark text separate from
   decorative exploration.
3. Review concepts at favicon, mobile, print, monochrome, and large sizes.
4. Select a direction for vectorization, font review, and trademark clearance.

### Restoration or interior visualization

1. Preserve the untouched source and classify the requested repair or room
   changes.
2. Choose enhancement for bounded cleanup, or editing for a clearly labeled
   redesign/reconstruction.
3. Compare every output against the source for invented detail, identity drift,
   geometry changes, perspective, and artifacts.
4. Return conservative and exploratory variants separately with their intended
   use and unresolved review requirements.

## Limitations

- MuAPI availability, model parameters, prices, quotas, and output retention
  are provider-controlled and volatile.
- Exact brand, product, or character consistency is not guaranteed by a prompt
  alone.
- Generated text, labels, logos, badges, dimensions, and claims need human or
  post-production verification.
- Some hosts expose hosted MCP tools but not local file upload, while others
  expose stdio tools with different input schemas.
- This pack provides workflows and contracts; the host supplies the actual
  MCP or REST connection and any local image viewer or editor.

## Contributing

Contributions should improve a reusable workflow rather than add an
undocumented provider-specific shortcut.

When adding or changing a skill:

1. Keep the skill in its own `agents/<name>/` directory with a complete
   `SKILL.md`.
2. Define inputs, routing rules, tool mapping, cost or approval behavior,
   output contract, QA checks, and failure handling.
3. Update `AGENTS.md`, `MODELS.md`, and this README when the capability is
   user-facing.
4. Keep provider details in the MuAPI guide and verify live schemas before
   hard-coding fields.
5. Add or update package validation when the skill inventory changes.
6. Run the checks before opening a change:

```sh
python3 scripts/validate_package.py
git diff --check
```

Do not commit API keys, private image bytes, unreviewed generated assets, or
provider responses that contain sensitive account data.

## License

[MIT](LICENSE)
