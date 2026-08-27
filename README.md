# AI Image Agent

> A free, open-source image-production playbook for the AI assistant you
> already use.

Give Claude, Claude Code, Codex, Cursor, Windsurf, Claude.ai, or another
Markdown-capable assistant a complete creative-production workflow. Add this
repository to the assistant you already use and ask it to plan, generate, edit,
adapt, review, and organize professional image work.

The repository is a portable skill pack, not a hosted application or an image
editor. The assistant provides the reasoning and tool loop; the connected image
provider supplies generation, editing, enhancement, uploads, and result
delivery.

## Why use it?

- Use the AI assistant you already know instead of learning another creative
  dashboard.
- Start with a complete image plan or run one focused workflow at a time.
- Route each job by its real constraint: identity, product fidelity, text,
  geometry, platform, or delivery format.
- Keep plans, prompts, asset roles, QA observations, and receipts in your
  project folder.
- Use a small draft batch, review it, and iterate only the selected direction.
- Read, adapt, and extend the workflows for your own production process.

## What you can ask it to do

Use plain language. For example:

- “Create a product launch image set and tell me which shots to make first.”
- “Create three professional headshot directions from my authorized photos.”
- “Turn one portrait into a themed photo pack while preserving the exact face.”
- “Put this garment on the supplied person photo and label the result as a
  visualization, not a fit guarantee.”
- “Combine these authorized portraits into a coherent team photo.”
- “Restore this old photograph conservatively and identify reconstructed detail.”
- “Create a logo, palette, typography direction, and application mockups for
  this brand.”
- “Turn this room photo into three realistic interior-staging directions.”
- “Create a storyboard of still frames for this short film premise.”
- “Create a mobile dashboard mockup using these design tokens and screenshots.”
- “Reshoot this approved product from front, three-quarter, macro, and overhead
  angles.”

The assistant chooses the smallest matching workflow and returns a clear
handoff with assumptions, model/tool choices, outputs, failures, QA findings,
and next steps.

## Use it with your AI assistant

This repository works with the assistant you already use:

| Assistant | How to add the image playbook |
|---|---|
| Claude Code | Keep `AGENTS.md` in the project and add selected skill folders to `.claude/skills/`. |
| Codex | Keep `AGENTS.md` in the project and load the relevant `SKILL.md` with the task. |
| Cursor or Windsurf | Add `AGENTS.md` and the relevant skill as project instructions. |
| Claude.ai | Add the files to Project knowledge or the conversation, then connect the available image tools. |
| Other AI assistants | Load `AGENTS.md` and the relevant skill through the assistant's project-instruction or file-upload feature. |

See [installation for existing agents](references/agent-installation.md) for
setup patterns. The host must provide the tool loop, approvals, image viewer or
editor when needed, and secure provider credentials.

## Quick start

1. Choose Claude, Claude Code, Codex, Cursor, Windsurf, Claude.ai, or another
   assistant that can read project files and use tools.
2. Add `AGENTS.md` and the skill you need from `agents/`.
3. Connect an image-generation provider through the assistant's MCP or REST
   integration. The bundled adapter supports MuAPI; its setup and current
   operation map are in [the image-tools guide](references/muapi-image-tools.md).
4. Ask for a task using the subject, audience, platform, format, references,
   rights, quantity, and budget.
5. Start with a bounded draft batch and approve any larger or expensive run.

Run the dependency-free package check before sharing or installing changes:

```sh
python3 scripts/validate_package.py
```

The assistant should never put API keys in prompts, reports, receipts,
committed files, or image metadata.

## Image workflows

Start with **Image Strategist** when a request spans several steps. For a
focused task, use the matching workflow directly.

| Workflow | What it helps with |
|---|---|
| [Image Strategist](agents/image-strategist/SKILL.md) | Build a complete image plan, route specialist work, and manage dependencies. |
| [Image Project Setup](agents/image-project-setup/SKILL.md) | Set up project, brand, subject, asset, platform, rights, and approval context. |
| [Image Generation](agents/image-generation/SKILL.md) | Create new images from a structured creative brief. |
| [Image Editing](agents/image-editing/SKILL.md) | Change an existing image while preserving selected details. |
| [Image Enhancement](agents/image-enhancement/SKILL.md) | Upscale, clean up, extend, remove a background, or prepare a selected image. |
| [Product Imagery](agents/product-imagery/SKILL.md) | Build truthful marketplace, catalog, reseller, lifestyle, and multi-angle product sets. |
| [Professional Headshots](agents/professional-headshots/SKILL.md) | Create consent-based LinkedIn, executive, team, speaker, and profile portraits. |
| [Portrait Photo Pack](agents/portrait-photo-pack/SKILL.md) | Generate themed portrait collections from one authorized identity source. |
| [Group Photo Compositing](agents/group-photo-compositing/SKILL.md) | Combine several authorized portraits into one coherent scene. |
| [Virtual Try-On](agents/virtual-try-on/SKILL.md) | Visualize a garment or accessory on an authorized person. |
| [Photo Restoration](agents/photo-restoration/SKILL.md) | Repair, colorize, clean, or upscale old and damaged photographs. |
| [Interior Redesign](agents/interior-redesign/SKILL.md) | Declutter, redesign, stage, or render an authorized room or floor plan. |
| [Multi-Angle Reshoot](agents/multi-angle-reshoot/SKILL.md) | Create controlled alternate camera views from an approved parent image. |
| [Logo and Brand Identity](agents/logo-and-brand-identity/SKILL.md) | Explore logos, wordmarks, brand kits, design guides, and application mockups. |
| [UI Mockups](agents/ui-mockups/SKILL.md) | Create mobile, web, SaaS, ecommerce, and design-system visual mockups. |
| [Image Storyboard](agents/image-storyboard/SKILL.md) | Turn a premise or script into ordered still keyframes. |
| [Ad Creative](agents/ad-creative/SKILL.md) | Develop ad concepts, visual hooks, and platform-ready image variants. |
| [Social Pack](agents/social-pack/SKILL.md) | Reframe an approved visual for multiple social placements. |
| [Thumbnail Generation](agents/thumbnail-generation/SKILL.md) | Create truthful video, blog, podcast, or editorial thumbnail directions. |
| [Brand Content](agents/brand-content/SKILL.md) | Produce repeatable social and campaign visuals from a confirmed brand system. |

Workflows can be combined. For example, a product launch may use project setup,
product imagery, multi-angle reshoot, ad creative, social pack, and image
enhancement in that order.

## Connect image tools

The skills use stable logical capabilities so the workflow remains portable
across assistants and provider transports:

| Logical capability | Purpose |
|---|---|
| `media.generate_image` | Create a new image from a structured prompt. |
| `media.edit_image` | Transform or recompose an existing image. |
| `media.upload_file` | Make a local reference available to a model that requires a hosted URL. |
| `media.upscale` | Increase resolution for a selected candidate. |
| `media.enhance_image` | Apply an operation such as cleanup or background removal. |
| `media.check_result` | Poll asynchronous work and retrieve outputs. |
| `media.search_models` | Discover current models and supported input shapes. |
| `media.account_balance` | Check available balance when the host exposes it. |

Resolve these capabilities to the exact tools and fields exposed by the host.
The live provider schema is authoritative for model availability, parameters,
limits, prices, and output URLs. Do not assume that a tool exposed over one
transport is available over another.

## Model and workflow selection

[MODELS.md](MODELS.md) is a curated decision guide, not a frozen provider
catalog. Choose the operation first, then verify that the live model accepts the
required references, aspect ratio, resolution, quality, and output count.

Use these general rules:

- text-to-image for a new concept;
- image-to-image/edit for a source whose identity, product, or geometry matters;
- enhancement for bounded cleanup or resolution changes;
- a reference-capable model for likeness, garment, product, or group continuity;
- a text-capable model plus post-production for exact lettering and logos; and
- a staged plan when a request includes generation, selection, editing,
  reframing, and final preparation.

When the host exposes a workflow catalog, inspect the selected workflow's
required inputs and dependencies before running it. If workflow tools are not
available, execute the local plan graph through the individual operations the
host does expose.

## Costs and approvals

The repository is free and open source. The connected provider may charge for
generation, editing, enhancement, uploads, or high-resolution outputs.

Before a paid call, the assistant should:

- identify the operation and model;
- state the expected call and output count;
- check balance when available;
- explain any estimate as a planning signal, not a quote;
- confirm a draft, exploration, or production-candidate budget; and
- stop for approval when the requested spend is ambiguous or exceeds the limit.

Start with a small, diverse batch. Bound retries, preserve failed/partial
variants, and never present a request ID without a usable output as success.
Publishing to an ad account, storefront, social channel, CMS, or profile is
outside this pack and requires a separate explicit action.

## Image coverage

The current workflows cover:

- text-to-image concepts and reference-guided editing;
- professional headshots and themed identity-locked portrait packs;
- group portraits and controlled camera-angle reshoots;
- garment/accessory try-on and product placement;
- product listings, catalog sets, reseller refreshes, lifestyle scenes, and
  multi-angle product views;
- logo exploration, brand kits, design guides, UI mockups, and application
  concepts;
- photo restoration, colorization, cleanup, extension, and upscaling;
- room redesign, property staging, floor-plan concepts, and architectural
  visualizations;
- storyboards, thumbnails, blog/social/ad visuals, and brand campaigns; and
- local receipts, parent/child assets, QA findings, and approval handoffs.

Actual model support, input limits, output retention, and tool availability
depend on the connected image provider and the assistant transport.

## Reports and saved work

When you ask the assistant to save its work, it can keep project context, asset
manifests, plans, receipts, and QA notes in a `.image/` folder:

```text
.image/
  project.md
  assets/<asset-id>.json
  runs/YYYY-MM-DD/<run-id>/plan.md
  runs/YYYY-MM-DD/<run-id>/receipt.json
  runs/YYYY-MM-DD/<run-id>/qa.md
  snapshots/styles/<style-id>.md
```

Receipts should preserve the logical operation, concrete tool/model, sanitized
request, input roles/order, request ID, status, output URLs, billing, parent
asset, QA, and approval state. Never save API keys, OAuth credentials, secret
URLs, or raw private image bytes. See [reports and receipts](references/reports-and-receipts.md)
for the suggested project, asset, and run formats.

## Quality, privacy, and rights

Before commercial, public, or high-stakes use, follow
[the creative QA checklist](references/creative-qa.md):

- verify product shape, packaging, labels, dimensions, text, logos, faces,
  hands, anatomy, geometry, reflections, and model artifacts;
- separate observed output, calculated checks, creative judgment, and
  hypotheses;
- verify claims, regulated categories, platform rules, accessibility, crop,
  dimensions, format, and safe areas;
- confirm permission for likenesses, private photos, property, trademarks,
  artwork, packaging, screenshots, uniforms, and other supplied assets;
- label try-on, staging, restoration, reconstruction, and fictional scenes
  clearly; and
- require human approval for exact copy, brand marks, legal text, product
  truth, fit claims, historical authenticity, and final publication.

Treat uploaded assets as sensitive. Use only assets the user is authorized to
process, minimize retention, and do not assume provider URLs are permanent or
private.

## Limitations

Your assistant must be able to read project files, connect image tools, and
review outputs. Quality and consistency vary by model and source quality. A
prompt cannot guarantee exact identity, product geometry, text, logo fidelity,
fit, historical recovery, architectural accuracy, or brand compliance. Some
hosts expose hosted tools but not local upload, while others expose local tools
with different schemas.

## Contributing

Improvements are welcome. Keep workflows focused, reusable, rights-aware, and
usable by more than one assistant. For a new skill:

1. Give it its own `agents/<name>/SKILL.md` with complete frontmatter.
2. Define inputs, routing keywords, tool mapping, prompt/plan protocol, cost
   gate, output contract, QA, rights, and failure behavior.
3. Update `AGENTS.md`, `MODELS.md`, this README, and the validator.
4. Keep provider details in the connection guide and verify live schemas before
   hard-coding fields.
5. Run:

```sh
python3 scripts/validate_package.py
git diff --check
```

Do not commit API keys, private image bytes, unreviewed generated assets, or
provider responses containing sensitive account data.

## License

[MIT](LICENSE)
