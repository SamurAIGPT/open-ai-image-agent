---
name: Image Project Setup
slug: image-project-setup
version: 1.0.0
category: image
description: Establish reusable brand, asset, platform, rights, and delivery context for repeatable image-production work.
status: ready
muapi_capabilities: []
required_connections: []
permissions:
  - workspace-write
---

# Image Project Setup

## Mission

Turn an unstructured creative request into a small, explicit project brief that
the other image skills can reuse. This is context setup, not a generation run.

## Use this skill when

- a brand or campaign is being analyzed for the first time;
- the same product, person, style, or channel formats recur;
- the user wants consistent outputs across several sessions;
- previous runs contain conflicting style, product, or rights assumptions.

## Required inputs

- Project or brand name.
- Main creative objective.
- Subject/product/person and intended audience.
- Target channels, markets, languages, and delivery formats.

Collect when relevant:

- exact product/SKU facts, dimensions, variants, and approved claims;
- palette, typography treatment, logo rules, mood, lighting, and banned motifs;
- reference asset inventory and whether each item may be uploaded externally;
- identity/style pack names and consent boundaries;
- platform/category rules and post-production requirements;
- owners, reviewers, approval gates, budget, and retention expectations.

## Workflow

1. Read `.image/project.md` and recent run/asset manifests if present. Show
   existing context and identify contradictions instead of silently replacing
   it.
2. Normalize the project into these sections: objective, audience, products or
   subjects, brand system, channels/formats, references, fixed facts, approved
   claims, rights state, review path, budget, and known limitations.
3. Mark every unknown as `unknown`. Propose inferences separately and ask for
   confirmation before treating them as project facts.
4. Inventory local references by role: product front/side/back, packaging,
   logo, style board, identity reference, source hero, or mask. Do not upload
   anything during setup unless the user explicitly asks for a generation run.
5. Confirm the smallest initial deliverable and a review checkpoint. Prefer a
   representative pilot before a broad campaign batch.
6. With confirmation, write `.image/project.md` using the layout in
   [reports and receipts](../../references/reports-and-receipts.md). Record the
   date created, last reviewed, and unresolved limitations.

## Decision rules

- A style description is not permission to use a private image or identity.
- A product name is not enough to establish color, material, dimensions,
  included quantity, label, or performance claims.
- Platform dimensions and policies are volatile; store the source and date
  checked, not just a remembered number.
- Keep brand reference, identity reference, and product reference roles
  distinct so a later workflow cannot confuse them.
- Do not create recurring schedules or publish assets inside this skill.

## Output format

Return:

1. Confirmed project context.
2. Missing decisions and their impact.
3. Reference/asset inventory with rights state.
4. Proposed `.image/project.md` contents.
5. Recommended first skill and smallest useful run.

## Failure and missing-data behavior

If the project is too underspecified, save nothing and return the minimum
questions needed. If a previous context file is stale or contradictory, keep
the old value visible, label the conflict, and ask which value is authoritative.
