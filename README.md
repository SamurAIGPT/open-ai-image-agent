# AI Image Agent

An AI agent for image generation and creative/design production — image generation, thumbnails, and on-brand visual content — backed by real generative-image APIs.

Part of [Agency Agents OS](https://github.com/Anil-matcha/agency-agents-os), an open ecosystem of specialized AI agents for real business work.

## Related Projects

- [Agency Agents OS](https://github.com/Anil-matcha/agency-agents-os) — the central catalog this repo is part of.
- [ai-youtube-agent](https://github.com/SamurAIGPT/ai-youtube-agent) — uses this repo's thumbnail-generation sub-agent and model picks for YouTube thumbnails.
- [ai-video-agent](https://github.com/SamurAIGPT/ai-video-agent) — uses this repo's generated images as reference/starting frames for video shots.
- [ai-voice-agent](https://github.com/SamurAIGPT/ai-voice-agent) — pairs with generated avatar images for talking-head video narration.
- [ai-social-agent](https://github.com/SamurAIGPT/ai-social-agent) — publishes the thumbnails and brand content this repo generates.
- [MuAPI specialized apps docs](https://muapi.ai/docs/specialized-apps) — image transformation and enhancement workflows behind the model catalog in `MODELS.md`.
- [MuAPI MCP docs](https://muapi.ai/docs/mcp) — connect this repo's `SKILL.md` files via MCP.
- [MuAPI access keys](https://muapi.ai/access-keys) — create the API key this agent needs.

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
- `media.upload_file` — upload a local reference/asset image to get a hosted URL (image-to-image and editing models take a URL, not a local path).
- `media.upscale` — resolution upscaling for final delivery.

See each sub-agent's `SKILL.md` for the specific capabilities it uses, and [MODELS.md](MODELS.md) for the full model catalog (quality, price, editing, character consistency, open-weights) each sub-agent picks from.

## Setup

1. Create a Muapi account and API key at [muapi.ai](https://muapi.ai).
2. Review the [Muapi API quickstart](https://muapi.ai) and [OpenAPI schema](https://api.muapi.ai/openapi.json) for the image-generation endpoints.
3. Load the `SKILL.md` for the sub-agent you need into your agent runtime (hosted agent, MCP client, or custom LLM app), or follow it manually.


## Using with an AI agent

Every sub-agent's `SKILL.md` is model- and runtime-agnostic — it's plain Markdown, so it works with any LLM agent, not just Claude. Two integration paths:

**As an MCP connection (the agent gets live Muapi tools):**

Muapi runs an MCP server at `https://api.muapi.ai/mcp` that any MCP-compatible client can connect to — Cursor, Windsurf, Claude, or your own custom agent.

- **Cursor / Windsurf / other clients with a header field:** connect to `https://api.muapi.ai/mcp` with an `Authorization: Bearer YOUR_MUAPI_KEY` header.
- **claude.ai / Claude Cowork / other connector UIs with no header field:** use the URL-embedded key form instead, `https://api.muapi.ai/mcp/YOUR_MUAPI_KEY`, via Settings → Connectors → Add custom connector.
- **Claude Code / Claude Desktop:** `claude mcp add muapi -e MUAPI_API_KEY=YOUR_MUAPI_KEY -- muapi mcp serve` (uses the muapi CLI's stdio transport — Claude Code's HTTP MCP client doesn't reliably inject tools).

Full setup details for every client: [muapi.ai/docs/mcp](https://muapi.ai/docs/mcp).

**As agent instructions (any LLM follows the workflow directly):**

Drop a sub-agent's `SKILL.md` into a Claude Code project's `.claude/skills/` directory, paste it into a custom-GPT/Project's system instructions, hand it to an autonomous agent framework as a tool spec, or attach it directly in a chat conversation — then ask the agent to follow it.

## Read-only vs. write actions

Image generation is `draft-only` — output is a file/URL, not a publish. Publishing to a channel, storefront, or ad platform is out of scope for this repo.

## Status and limitations

Image generation is a live, tested Muapi capability. Brand-content consistency (matching a defined style guide precisely across many generations) depends on how well the brief is specified; it is not guaranteed pixel-perfect brand compliance.

## Contributing

See [Agency Agents OS CONTRIBUTING.md](https://github.com/Anil-matcha/agency-agents-os/blob/main/CONTRIBUTING.md).

## License

[MIT](LICENSE)
