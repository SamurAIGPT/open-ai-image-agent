# Installation for existing agents

This repository is a portable image-agent skill pack. It is not an agent
runtime, image editor, or MCP server. The host agent loads the Markdown and
provides the MuAPI connection, tool loop, approvals, and optional local
artifact storage.

## Connect MuAPI

Use the official [MuAPI MCP documentation](https://muapi.ai/docs/mcp) for
current client configuration.

- Hosted Streamable HTTP is intended for clients such as Cursor and Windsurf.
  Configure `https://api.muapi.ai/mcp` with an `Authorization: Bearer` header
  when the client supports custom headers.
- Claude Code and Claude Desktop should use the local stdio bridge supplied by
  the MuAPI CLI:

  ```sh
  claude mcp add muapi -e MUAPI_API_KEY=YOUR_MUAPI_KEY -- muapi mcp serve
  ```

- A REST-only host can use the submit-then-poll contract in
  [muapi-image-tools.md](muapi-image-tools.md).

Keep keys in the host's secret store or environment. Never put a key in a
prompt, committed file, report, receipt, or URL when a header is available.

## Install selected skills

For a directory-based host, keep each `SKILL.md` at its skill root:

```text
<project>/.claude/skills/image-strategist/SKILL.md
<project>/.claude/skills/image-generation/SKILL.md
```

For a broad request, load `AGENTS.md` plus `image-strategist`. For a focused
request, load only the matching skill and the references it names. Avoid
combining every workflow into one prompt when the host supports selective
loading.

## Example request

```text
Create three 16:9 hero-image directions for our launch campaign.
Audience: operations leaders at mid-market companies.
Brand style: dark graphite, warm accent, minimal, no generated text.
Use the attached product screenshot as a reference; preserve the UI exactly.
Budget: keep the first round to three image calls.
Return URLs and receipts; do not publish anything.
```

## Host-agent contract

Before calling MuAPI, the host should:

1. identify the smallest matching skill;
2. read `.image/project.md` and compatible prior runs when present;
3. collect missing brief, platform, reference, rights, and budget decisions;
4. state the planned tools, models, variants, estimated cost signal, and retry
   policy;
5. verify the transport exposes the tool names required by the skill.

After calling MuAPI, it should:

1. preserve structured request/result/billing metadata;
2. separate provider output from QA calculations and creative judgment;
3. report every failed or partial variant;
4. save receipts only when requested or allowed by the host project convention;
5. state unresolved rights, platform, text, product-truth, or URL-retention
   limitations.
