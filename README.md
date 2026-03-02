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

## GitHub Pages (live API docs)

This repo deploys the **API reference** (OpenAPI spec) to GitHub Pages via the **Deploy to GitHub Pages** workflow. After you enable it once, every push to `main` updates the site.

**Live URL (after first deploy):**  
**https://mahesh-ict-dev.github.io/datagol-api-documentation/**

### One-time setup to enable GitHub Pages

1. In your repo on GitHub go to **Settings** → **Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Push the `deploy-gh-pages.yml` workflow (or re-run the workflow). The first run will deploy the site; the link above will work once the run succeeds.

The deployed site is a Redoc-based API reference built from `docs/openapi/openapi.yaml`. For the full Mintlify site (tabs, intro, etc.) use `npm run dev` locally or connect the repo to [Mintlify](https://mintlify.com).

## Deploy

- **GitHub Pages**: Automatic on push to `main` (see above). Free, no account needed.
- **Mintlify**: Connect this repo at [Mintlify](https://mintlify.com) for their full hosted docs experience.
