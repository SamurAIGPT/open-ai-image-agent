# Image Model Catalog

Muapi exposes 500+ image models behind one API and one API key. No single model wins on every axis — quality, price, uncensored generation, editing, character consistency, and open-weights all trade off differently. Pick the model per job, not by habit. Every sub-agent in this repo references this catalog for its model picks.

## How to call it

```
POST https://api.muapi.ai/api/v1/{model-slug}
Content-Type: application/json
x-api-key: YOUR_API_KEY

{ "prompt": "..." }
```

Poll `GET https://api.muapi.ai/api/v1/predictions/{request_id}/result` until `status` is `completed`, then use the output URL.

```bash
curl -X POST https://api.muapi.ai/api/v1/gpt-image-2-text-to-image \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -d '{"prompt": "a neon-lit night market street in Tokyo, photoreal"}'
```

```python
import requests

response = requests.post(
    "https://api.muapi.ai/api/v1/gpt-image-2-text-to-image",
    headers={"x-api-key": "YOUR_API_KEY"},
    json={"prompt": "a neon-lit night market street in Tokyo, photoreal"},
)
request_id = response.json()["request_id"]

result = requests.get(
    f"https://api.muapi.ai/api/v1/predictions/{request_id}/result",
    headers={"x-api-key": "YOUR_API_KEY"},
)
print(result.json())
```

## Using a local image as input

Image-to-image, editing, and reference-based models take a **URL**, not a local file path or raw bytes. If the reference image is a local file, upload it first to get a hosted URL, then pass that URL as the model input.

```
POST https://api.muapi.ai/api/v1/upload_file
x-api-key: YOUR_API_KEY
Content-Type: multipart/form-data

file=@local-image.jpg
```

Returns `{"url": "https://cdn.muapi.ai/uploads/..."}`. Images are capped at 10MB. The same endpoint also accepts a JSON body `{"url": "https://..."}` to re-host an image that's already at some other URL.

CLI shortcut: `muapi upload file ./local-image.jpg` — prints the hosted URL directly.

## Full comparison table

| Model | Category | Price | Best for |
|---|---|---|---|
| GPT Image 2 | Best Quality #1 | $0.09/image | Artificial Analysis Arena #1 (Elo 1370), clean multilingual text rendering |
| Nano Banana Pro | Best Quality #2 | $0.12/image | Photorealism, coherent local edits, spatial understanding |
| Seedream 5.0 Pro | Best Quality #3 | $0.045/image | Strongest stylized/artistic output |
| Midjourney v8 | Best Quality #4 | $0.10/image | Aesthetic-quality benchmark for pure image generation |
| Imagen 4 Ultra | Best Quality #5 | $0.06/image | Strong prompt adherence |
| Z-Image Turbo | Best Value #1 | $0.007/image | Price/quality sweet spot, not just the cheapest option |
| Flux-2 Klein 4B Turbo | Best Value #2 | $0.0052/image | Half the price of standard Klein 4B, same quality |
| Flux.1 Schnell | Best Value #3 | $0.003/image | Near-instant generation, classic low-cost workhorse |
| SDXL | Best Value #4 | $0.004/image | Lowest possible cost per pixel |
| Wan 2.7 | Best Uncensored #1 | $0.05/image | Near-zero prompt filtering |
| Qwen Image 2.0 | Best Uncensored #2 | $0.04/image | Confirmed NSFW capability, no prompt-rewriting layer |
| Seedream 5.0 | Best Uncensored #3 | $0.0325/image | Open pipeline, no surprise censorship |
| Grok Imagine | Best Uncensored #4 | $0.05/image | Looser content policy than mainstream closed models |
| Nano Banana Pro Edit | Best Editing #1 | $0.12/generation | Coherent object insertion/removal |
| GPT Image 2 (Edit) | Best Editing #2 | $0.09/generation | Arena-verified #3 on Image Editing Arena (Elo 1257) |
| Seedream 5.0 Edit | Best Editing #3 | $0.0325/generation | 1/4 to 1/7 the cost of Nano Banana Pro Edit |
| Flux Kontext Pro | Best Editing #4 | $0.03/generation | One-sentence instruction editing, no fine-tuning |
| Qwen Image Edit 2511 | Best Editing #5 | $0.04/generation | Open-model editing, industry-leading performance for its tier |
| Ideogram Character | Best Character Consistency #2 | $0.15/image | Dedicated Character Reference feature |
| MiniMax Subject Reference | Best Character Consistency #4 | $0.01/generation | Cheapest dedicated subject-consistency endpoint |
| Vidu Q2 Reference-to-Image | Best Character Consistency #5 | $0.032/generation | Reference-driven character generation |
| Qwen Image | Best Open Source #2 | $0.03/generation | Apache 2.0, best-in-class open model for in-image text |
| FLUX.2 [dev] | Best Open Source #3 | $0.015/generation | Current-gen open-weight Flux |
| HiDream i1 (Full) | Best Open Source #4 | $0.04/generation | Open weights, distinct architecture from Flux/Qwen/Z-Image |

## Choosing a model by job, not by vendor

"Best AI image model" is the wrong question — the better question is which model fits the specific job:

- **Raw quality:** GPT Image 2 tops the Text-to-Image Arena.
- **Price/quality sweet spot:** Z-Image Turbo, at $0.007/image.
- **Content-filter too conservative for the use case:** Wan 2.7 or Qwen Image 2.0.
- **Editing an existing image instead of generating from scratch:** Nano Banana Pro Edit or GPT Image 2 (Edit).
- **Locking a character's identity across scenes:** Ideogram Character or MiniMax Subject Reference.
- **Open-weights (licensing/output-rights behave differently than closed models):** Z-Image Turbo or Qwen Image.
- **Legible in-image text/typography:** Qwen Image is best-in-class for this specifically — a common miss is using a cheap/fast model (e.g. Flux.1 Schnell) for a brief that needs readable headline or CTA text baked into the image, which reliably renders garbled.

Because every model sits behind the same API key and request pattern, switching models per request is a one-line change, not a new integration — so pick deliberately per image, not once per project.

Source: [muapi.ai/ai-image-api](https://muapi.ai/ai-image-api) — check that page for current pricing and the latest model additions, since this list reflects a snapshot.
