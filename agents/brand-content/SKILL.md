---
name: Brand Content
slug: brand-content
version: 1.1.0
category: image
description: Generate on-brand social or advertising image candidates from a confirmed brand system and asset library, with explicit compliance checks.
status: ready
muapi_capabilities:
  - media.generate_image
  - media.edit_image
  - media.upload_file
  - media.check_result
  - media.search_models
required_connections:
  - muapi
permissions:
  - draft-only
  - workspace-write
---

# Brand Content

## Mission

Generate a repeatable set of social, ad, or campaign visuals that follows a
confirmed brand system rather than a generic aesthetic. Exact pixel-level
compliance is not guaranteed by a prompt; the workflow must surface deviations.

## Required inputs

- Brand style guide or confirmed style descriptor.
- Specific content brief and intended channel/placement.
- Approved palette, tone, typography treatment, logo rules, and prohibited
  motifs.
- Reference asset library and rights state.

Collect when relevant:

- audience, campaign goal, message, and approved copy/claims;
- product/SKU facts and identity/mascot constraints;
- dimensions, safe areas, localization, variant count, and budget;
- reviewer, approval gate, and post-production layout plan.

If no style guide, palette, tone, or references are supplied, use
[Image Project Setup](../image-project-setup/SKILL.md) first. Do not guess a
brand identity.

## Model selection

Use [MODELS.md](../../MODELS.md) and the live tool contract in
[references/muapi-image-tools.md](../../references/muapi-image-tools.md). Use an
editing/reference-capable model when a real logo, product, mascot, or recurring
person must remain stable.

## Workflow

1. Read `.image/project.md` and prior selected assets. Build a reusable style
   descriptor containing palette, contrast, lighting, composition, texture,
   typography treatment, tone, and exclusions. Keep it stable across the batch.
2. Separate brand invariants from the per-asset brief. Record exact logo,
   product, copy, claims, and identity details that may not change.
3. Confirm rights for local style boards, logos, product assets, and likenesses.
   Upload each local reference once through `media.upload_file`, recording its
   role and order.
4. Choose the model per task: text-to-image for a new scene, editing for an
   existing brand/product asset, and a consistency-capable model for a
   recurring identity when the live schema supports it.
5. State the planned calls, formats, variant count, cost signal, and review gate
   before a batch. Generate independent assets in parallel when possible.
6. Poll and preserve each result with model, prompt, parameters, request ID,
   status, URL, billing, and source roles.
7. Check each candidate against the style descriptor and fixed facts: palette,
   contrast, logo treatment, typography space, product/identity fidelity,
   message, artifacts, crop, and platform format.
8. Flag deviations explicitly. Iterate the smallest offending variable or send
   the selected candidate to an editing/enhancement workflow; do not silently
   label a visually inconsistent output “on brand.”

## Decision rules

- A style descriptor is a consistency aid, not proof of brand compliance.
- Keep exact text, logos, legal copy, prices, and claims in approved layout or
  post-production whenever possible.
- Do not invent social proof, ratings, badges, product features, or claims.
- Reuse one descriptor and the same reference roles across a batch so the
  outputs can be compared meaningfully.

## Output format

Return the style descriptor used, per-asset brief, reference roles, model/tool,
parameters, output URL/status, brand-compliance checklist, deviations,
post-production requirements, rights/claims limitations, and receipt links.

## Failure and missing-data behavior

If required brand facts or rights are missing, pause before paid generation and
ask for them. If one asset fails or deviates, preserve that result and explain
the smallest retry or manual correction instead of silently returning a smaller
or supposedly compliant set.
