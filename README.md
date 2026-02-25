# DataGOL API Docs

Mintlify documentation site for the DataGOL API, generated from the OpenAPI specification.

## Quick start

```bash
npm install
npm run dev
```

Open **http://localhost:3000**. Use the **API Reference** tab to browse and try all endpoints.

## Commands

| Command | Description |
|---------|-------------|
| `npm run dev` | Start local preview (port 3000) |
| `npm run validate` | Validate `docs.json` and content |
| `npm run build` | Build for production |

## Structure

- **`docs/docs.json`** — Site config: navigation, theme, OpenAPI reference.
- **`docs/introduction.mdx`** — Getting started (Documentation tab).
- **`docs/api-reference.mdx`** — API overview (Documentation tab).
- **`docs/openapi/openapi.yaml`** — OpenAPI 3.0 spec; the **API Reference** tab is auto-generated from this file.

## Adding Postman

You can add a Postman collection link or embed in the docs (e.g. in `introduction.mdx` or a new “Postman” page) using a [Card](https://mintlify.com/docs/components/card) or [Link](https://mintlify.com/docs/components/link). Export the collection from Postman and either host the JSON or link to a public collection URL.

## Deploy

Connect this repo to [Mintlify](https://mintlify.com); deployments run on push. Or build with `npm run build` and deploy the output to any static host.
