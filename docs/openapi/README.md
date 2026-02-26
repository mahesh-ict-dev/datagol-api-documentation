# OpenAPI spec

- **`openapi.yaml`** — Current DataGOL API spec (used by Mintlify/API Reference).
- **`openapi.yaml.backup`** — Backup of the previous spec before the last update.

## API segregation (tags)

Endpoints are grouped by tag for docs and flow:

| Tag | Description |
|-----|-------------|
| **Getting Started** | Authentication, login, and service account management |
| **Workspaces** | Workspace CRUD and user management |
| **AI Extraction** | Schema generation, extraction configs, and run triggers |
| **WorkBook** | Tables (workbooks), columns, rows, and data operations |
| **Knowledge Graph** | File upload, folder listing, and knowledge graph APIs |

## Using the shared full spec (8589 lines)

If you have the full shared spec (e.g. from Untitled-1):

1. Save it as **`openapi_new.yaml`** in this folder (same directory as `openapi.yaml`).
2. Run:
   ```bash
   python3 docs/openapi/apply-openapi-update.py docs/openapi/openapi_new.yaml
   ```
3. This will:
   - Strip line-number prefixes if present (e.g. `     1|openapi: ...` → `openapi: ...`)
   - Add the `tags` section and fix servers (deduplicate, add descriptions)
   - Write the result to **`openapi.yaml`** (overwriting the current file).

Keep **`openapi.yaml.backup`** as your backup before running the script if needed.
