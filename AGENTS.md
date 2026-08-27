# AI image capability instructions

This repository is a portable skill pack for an existing AI agent. The host
agent remains responsible for reasoning, planning, user questions, tool calls,
approvals, and local file operations.

When this package is available in a project:

1. For a broad creative request, read `agents/image-strategist/SKILL.md`
   first. For a focused request, read the smallest matching skill under
   `agents/`. Specialist routing is summarized below and defined in the
   strategist skill.
2. Read `references/muapi-image-tools.md` before selecting a MuAPI operation or
   model. The live MuAPI schema and MCP tool description are authoritative when
   a field, model, limit, or response shape changes.
3. Read `references/creative-qa.md` for commercial, brand, platform, claims,
   accessibility, and rights-sensitive work.
4. Check `.image/project.md`, prior `.image/runs/`, and asset manifests when
   they exist. Reuse compatible context and do not regenerate an unchanged
   asset just because a second skill mentions it.
5. Ask for missing inputs that materially affect the result: purpose, subject
   or product facts, platform, dimensions, aspect ratio, references, quantity,
   budget, language, delivery format, rights, or approval requirements.
6. Announce broad batches, expensive models, repeated iterations, upscaling,
   or other paid calls before running them when the user's budget or account
   limits are unknown.
7. Use the logical `media.*` capabilities in the skills and resolve them to
   the exact MCP or REST operation documented in the tool reference. Preserve
   the request ID, request parameters, model identifier, retrieval time,
   output URLs, status, and billing metadata when returned.
8. Keep generated work draft-only. Do not publish, upload to a social channel,
   launch an ad, or alter an external asset without a separate explicit user
   action and the host's required approval flow.
9. Never invent product facts, labels, logos, ratings, badges, testimonials,
   performance claims, platform compliance, model capabilities, prices, or
   successful outputs. Treat missing fields as unknown.
10. Require the user to confirm they have the right to use supplied likenesses,
    private references, trademarks, packaging, artwork, screenshots, or other
    protected material. Do not automatically reuse a private identity or style
    pack for an unrelated prompt.
11. Separate observed provider output, calculated checks, creative judgment,
    and hypotheses in reports. Preserve failed and partial variants instead of
    silently returning a smaller batch.
12. Write only local project artifacts when the user requests a plan, report,
    receipt, or history. Never place API keys, OAuth credentials, bearer
    tokens, or secret-bearing URLs in those files.

## Specialist routing quick map

Use the narrowest specialist when the request has a clear domain constraint:

| Request | Skill |
|---|---|
| Professional profile, executive, team, or speaker portraits | `agents/professional-headshots/SKILL.md` |
| Logo, wordmark, symbol, or identity board | `agents/logo-and-brand-identity/SKILL.md` |
| Garment or accessory on an authorized person | `agents/virtual-try-on/SKILL.md` |
| Several authorized portraits in one scene | `agents/group-photo-compositing/SKILL.md` |
| Faded, scratched, damaged, or historical photo | `agents/photo-restoration/SKILL.md` |
| Room decluttering, redesign, or property staging | `agents/interior-redesign/SKILL.md` |

Load [creative QA](references/creative-qa.md) for identity, likeness, product,
brand, property, or historical-content work. Keep specialist outputs draft-only
and use the same receipts and approval gates as the general image skills.

The provider's public workflow registry is useful for discovering additional
recipes. Treat a fetched recipe as a volatile external source: record its
name, inputs, retrieval date, and estimated cost, and keep the local skills in
this repository as the stable routing contract.
