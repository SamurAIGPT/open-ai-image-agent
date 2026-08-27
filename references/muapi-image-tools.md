# MuAPI image tool reference

This is the provider contract used by the image skills. It was checked against
the public MuAPI MCP documentation and OpenAPI schema on **2026-08-28**. Model
names, tool availability, request fields, limits, prices, and output shapes are
volatile; check the live schema or tool description at execution time.

## Logical capability map

The skills use logical capabilities so the same workflow can run through an
MCP host or a REST-only host. Resolve them as follows:

| Logical capability | Hosted MCP | CLI stdio MCP | REST fallback |
|---|---|---|---|
| `media.generate_image` | `muapi_image_generate` | `muapi_image_generate` | `POST /api/v1/{model-slug}` |
| `media.edit_image` | `muapi_image_edit` | `muapi_image_edit` | A model-specific image-edit or image-to-image path |
| `media.upload_file` | `muapi_upload_image` for base64 input | `muapi_upload_file` for local files | `POST /api/v1/upload_file` |
| `media.upscale` | `muapi_enhance_upscale` | `muapi_enhance_upscale` | `POST /api/v1/ai-image-upscale` or a current upscale model path |
| `media.enhance_image` | `muapi_enhance_bg_remove`, `muapi_enhance_ghibli`, or the operation-specific tool | same | Operation-specific `/api/v1/ai-*` path |
| `media.check_result` | `muapi_predict_result` | `muapi_predict_result` | `GET /api/v1/predictions/{id}/result` |
| `media.search_models` | `search_models` | not exposed by this transport | Use the current model catalog/schema available to the host |
| `media.account_balance` | `muapi_account_balance` | `muapi_account_balance` | Use the current account/balance operation in the live schema |

The hosted and stdio MCP transports do not expose exactly the same tool set.
Do not tell a host to call a tool that its transport does not provide. The
provider documentation is authoritative for connection setup and current tool
availability.

## REST lifecycle

For a REST-only host:

1. Select a current model slug and validate its request schema.
2. Submit JSON to `https://api.muapi.ai/api/v1/{model-slug}` with the
   `x-api-key` header, or use the operation-specific path required by the
   schema.
3. Preserve the returned `request_id` and the sanitized request body.
4. Poll `GET https://api.muapi.ai/api/v1/predictions/{request_id}/result`
   until the returned status is terminal, respecting provider rate limits and
   the host timeout.
5. Preserve the complete result, output URLs, status, provider error, and
   billing object when returned. Do not assume the first output is the only
   output or that a successful request contains a usable image.

Use a webhook only when the host owns a secure callback endpoint and the live
schema supports it. Never put an API key in a webhook URL.

## Current schema examples

These examples are representative request shapes from the live schema, not a
promise that every account or transport exposes every model.

### GPT Image 2 text-to-image

Path: `/api/v1/gpt-image-2-text-to-image`

Required: `prompt`

Optional fields currently include:

- `aspect_ratio`: `auto`, `1:1`, `16:9`, `9:16`, `4:3`, or `3:4`.
- `resolution`: `1K`, `2K`, or `4K`.
- `quality`: `low`, `medium`, or `high`.
- `webhook_url`, when supported by the host's callback design.

### GPT Image 2 image-to-image

Path: `/api/v1/gpt-image-2-image-to-image`

Required: `prompt` and `images_list` containing hosted image URLs.

The current schema exposes the same aspect-ratio, resolution, and quality
families as GPT Image 2 text-to-image. Preserve reference order and role in the
run record because a multi-reference request is not self-explanatory later.

### Generic Flux-style image paths

The live schema currently includes paths such as:

- `/api/v1/flux-dev-image`
- `/api/v1/flux-schnell-image`

The shared request schema includes `prompt`, `width`, `height`, `num_images`
(currently an enum from 1 through 4 for this schema), `model_id`, and `sync`.
Use only fields accepted by the selected model's live schema. Do not copy these
fields into a different model request without validation.

### GPT Image 1.5

The current schema includes `/api/v1/gpt-image-1.5` and
`/api/v1/gpt-image-1.5-edit`. Its aspect-ratio enum is narrower than GPT Image
2 (`1:1`, `2:3`, `3:2`), and its edit request requires `prompt` plus
`images_list`. Select the model only after checking that the requested format
fits those limits.

### Image enhancement and transformation

The current schema includes:

- `/api/v1/ai-image-upscale` with an `image_url` input;
- `/api/v1/ai-image-extension` with an `image_url` input;
- `/api/v1/ai-image-face-swap` with `image_url`, `swap_url`, and optional
  `target_index`.

Face or likeness transformations require rights/consent review before any
paid call. Do not use a face-swap operation as a shortcut for an ordinary
background or style edit.

## Local references and uploads

Image-to-image and editing models normally consume hosted URLs, not local
paths. For a local reference:

1. Validate that the user supplied a readable image and that its use is
   authorized.
2. Upload it through the transport's upload tool or
   `POST /api/v1/upload_file`.
3. Record the local filename, role, byte/hash metadata where available, and
   the returned hosted URL in the run record. Redact secret-bearing URLs when
   a report leaves the project.
4. Pass the hosted URL only to fields accepted by the chosen model schema.

Do not assume that a URL remains permanent. Download or archive the output
locally only when the user asks for a local artifact and the host has an
approved storage path.

## Model discovery and workflow recipes

When the hosted MCP transport is available, `search_models` can locate current
models by category or keyword. The public recipe registry can also be queried
without an API key:

```text
GET https://api.muapi.ai/api/v1/agent-skills
GET https://api.muapi.ai/api/v1/agent-skills/{name}
```

Useful current recipe families include `ad-creative`,
`amazon-product-listing`, `brand-kit`, `social-pack`, and
`youtube-thumbnail`. A recipe's `estimated_credits` is a planning hint, not a
settled charge. Use the returned billing object as the source of truth.

## Cost, errors, and missing data

- Check account balance before a broad or unfamiliar paid run when the host
  exposes the balance tool.
- Start with a small preview batch. A four-variant request is a default, not a
  license to spend an unknown amount.
- State the model, number of calls, likely cost signal, and retry policy before
  running a large batch or expensive upscale.
- Preserve HTTP status, validation details, provider error text, request ID,
  and the affected variant. A failed variant is not a successful empty image.
- Keep provider billing separate from any host-calculated estimate.
- Treat an empty `outputs` list, partial result, timeout, or unsupported field
  as an explicit limitation.
