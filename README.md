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

## Git (user: mahesh-ict-dev)

This repo is configured with Git user **mahesh-ict-dev**. To push to a remote:

1. **Create a new repository** on GitHub (or your Git host) — do not initialize with a README.

2. **Add the remote and push** (replace `mahesh-ict-dev` and `newDGDoc` with your org/user and repo name):

   ```bash
   git remote add origin https://github.com/mahesh-ict-dev/newDGDoc.git
   git branch -M main
   git push -u origin main
   ```

3. **Using SSH** (if you use SSH keys):

   ```bash
   git remote add origin git@github.com:mahesh-ict-dev/newDGDoc.git
   git push -u origin main
   ```

To change the Git user for this repo only:

```bash
git config user.name "mahesh-ict-dev"
git config user.email "your-email@example.com"
```

## CI/CD

- **GitHub Actions** (`.github/workflows/ci.yml`): on every push and pull request to `main`/`master`, the workflow runs `npm ci` and `npm run validate` to ensure the Mintlify docs and OpenAPI spec are valid.

- **Mintlify deploy**: Connect this repository to [Mintlify](https://mintlify.com). Mintlify will build and publish the docs on each push to the connected branch (no extra CI step needed for deploy).

- To add deploy via GitHub Actions (e.g. to GitHub Pages or another host), add a job that runs `npm run build` and uploads the `docs/out` (or Mintlify output) artifact.

## Deploy

Connect this repo to [Mintlify](https://mintlify.com); deployments run on push. You can also run `npm run build` and deploy the generated output to any static host.
# datagol-api-documentation
