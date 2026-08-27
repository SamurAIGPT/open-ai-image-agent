# Image runs, asset manifests, and receipts

The image pack has no hosted database. When a user asks for a plan, report,
repeatable campaign, or history, keep the durable context and run evidence in
the project workspace.

## Suggested layout

```text
.image/
  project.md
  assets/
    <asset-id>.json
  runs/
    YYYY-MM-DD/
      <run-id>/
        plan.md
        receipt.json
        qa.md
        sources/
          <step-id>.json
  snapshots/
    styles/
      <style-id>.md
```

Create these directories only when the user asks for local persistence or the
host's project convention permits it. Do not overwrite an earlier run; a
repeatable comparison needs a new dated run.

## Project context

`project.md` may contain:

- project and brand name;
- products, audiences, markets, languages, and campaign goals;
- channel/platform targets and required dimensions or file formats;
- approved palette, typography treatment, logo rules, tone, and banned visual
  patterns;
- canonical product/SKU facts and approved claims;
- reference asset inventory, identity/style pack names, and rights status;
- owners, reviewers, approval gates, budget, and retention expectations;
- date created, last reviewed, and known limitations.

Mark unknown fields as `unknown`. Do not turn an inferred style, product fact,
or platform rule into a durable project fact without confirmation.

## Asset manifest

For each important input or output, record a small manifest such as:

```json
{
  "schema": "muapi-image-asset.v1",
  "asset_id": "hero-v1",
  "role": "reference|generated|selected|upscaled|restored|visualization|concept",
  "source": "local|muapi|user-url",
  "filename": "refs/product-front.png",
  "sha256": "...",
  "model": "gpt-image-2",
  "request_id": "provider-request-id",
  "url": "https://...",
  "status": "available|failed|expired|unknown",
  "retrieved_at": "2026-08-28T00:00:00Z",
  "rights_status": "confirmed|pending|unknown",
  "reference_roles": ["product-primary"],
  "parent_asset_id": null,
  "approval_status": "draft|selected|approved|rejected|unknown",
  "notes": "Preserve bottle geometry and label art"
}
```

Do not store API keys, authorization headers, OAuth tokens, private connector
secrets, or raw face/reference bytes in a receipt. Redact hosted URLs when they
contain secrets or when the report leaves the project.

## Run receipt

Each distinct provider call used by a report should have a receipt containing:

- the logical capability and concrete provider task/tool;
- run ID, variant ID, model ID, and schema verification date;
- sanitized request parameters, including aspect ratio, resolution, quality,
  seed or other deterministic fields when returned;
- prompt hash and, when the user permits it, the prompt text or a link to a
  local prompt file;
- reference asset IDs and their roles/order;
- specialist domain, preservation block, and approval gate when applicable;
- submission and completion timestamps, request ID, status, output URLs,
  provider error, and billing object;
- calculated QA results, selected variant, iteration relationship, and
  upscaling operation.

A receipt is an audit trail, not a claim that the image is commercially
approved. Human review and platform checks remain separate.

## Report contract

A useful image report contains:

1. Brief, audience, channel, dimensions, and scope.
2. Planned calls, model choices, variant count, and budget assumptions.
3. Generated outputs with IDs, URLs, status, and the model used.
4. QA observations: subject/product/likeness/geometry fidelity as applicable,
   composition, text/brand fidelity, artifacts, and required post-production.
5. Selected direction and the exact change for the next iteration.
6. Rights, claims, platform, accessibility, and approval limitations.
7. Failed/partial calls and the smallest retry needed.
8. Links to local receipts/source records and the next suggested check.

Separate provider facts, calculations, creative judgments, and hypotheses.
