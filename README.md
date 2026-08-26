# AI Image Agent

An AI agent for image generation and creative/design production — image generation, thumbnails, and on-brand visual content — backed by real generative-image APIs.

Part of [Agency Agents OS](https://github.com/Anil-matcha/agency-agents-os), an open ecosystem of specialized AI agents for real business work.

## What this covers

This repo is the umbrella for anything an agency or in-house team would call "the AI image agent": producing finished, on-brief images at scale without a designer generating each one manually.

## Sub-agents

| Agent | Does | Status |
|---|---|---|
| [Image Generation](agents/image-generation/SKILL.md) | Text-to-image and image-to-image generation from a creative brief | Blueprint |
| [Thumbnail Generation](agents/thumbnail-generation/SKILL.md) | Video/blog thumbnail variants optimized for click-through | Blueprint |
| [Brand Content](agents/brand-content/SKILL.md) | On-brand social/ad images using a defined style and asset library | Blueprint |

## Required Muapi APIs

- `media.generate_image` — text-to-image and image-to-image generation across Muapi's model catalog.
- `media.upscale` — resolution upscaling for final delivery.

See each sub-agent's `SKILL.md` for the specific capabilities it uses.

## Setup

1. Create a Muapi account and API key at [muapi.ai](https://muapi.ai).
2. Review the [Muapi API quickstart](https://muapi.ai) and [OpenAPI schema](https://api.muapi.ai/openapi.json) for the image-generation endpoints.
3. Load the `SKILL.md` for the sub-agent you need into your agent runtime (hosted agent, MCP client, or custom LLM app), or follow it manually.

## Read-only vs. write actions

Image generation is `draft-only` — output is a file/URL, not a publish. Publishing to a channel, storefront, or ad platform is out of scope for this repo.

## Status and limitations

Image generation is a live, tested Muapi capability. Brand-content consistency (matching a defined style guide precisely across many generations) depends on how well the brief is specified; it is not guaranteed pixel-perfect brand compliance.

## Contributing

See [Agency Agents OS CONTRIBUTING.md](https://github.com/Anil-matcha/agency-agents-os/blob/main/CONTRIBUTING.md).

## License

[MIT](LICENSE)
