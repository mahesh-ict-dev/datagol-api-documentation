#!/usr/bin/env python3
"""
Apply OpenAPI update: strip line-number prefixes (if any), add tags section,
and deduplicate servers. Reads from stdin or first argument, writes to
docs/openapi/openapi.yaml.
"""
import re
import sys
from pathlib import Path

def strip_line_number(line: str) -> str:
    """If line looks like '     1|content', return 'content'."""
    m = re.match(r"^\s*\d+\|(.*)$", line)
    return m.group(1) if m else line

OLD_PREAMBLE = """openapi: 3.0.0
info:
  title: DataGOL APIs
  version: 1.0.0
  description: ''
servers:
  - url: 'https://be.datagol.ai'
  - url: 'https://be.datagol.ai'
  - url: 'https://kg.datagol.ai'
  - url: 'https://ai.datagol.ai'
paths:
"""

NEW_PREAMBLE = """openapi: 3.0.0
info:
  title: DataGOL APIs
  version: 1.0.0
  description: ''
tags:
  - name: Getting Started
    description: Authentication, login, and service account management
  - name: Workspaces
    description: Workspace CRUD and user management
  - name: AI Extraction
    description: Schema generation, extraction configs, and run triggers
  - name: WorkBook
    description: Tables (workbooks), columns, rows, and data operations
  - name: Knowledge Graph
    description: File upload, folder listing, and knowledge graph APIs
servers:
  - url: 'https://be.datagol.ai'
    description: DataGOL backend API
  - url: 'https://kg.datagol.ai'
    description: Knowledge graph service
  - url: 'https://ai.datagol.ai'
    description: AI services
paths:
"""

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            raw = f.read()
    else:
        raw = sys.stdin.read()

    lines = raw.split("\n")
    cleaned = [strip_line_number(L) for L in lines]
    text = "\n".join(cleaned)

    if OLD_PREAMBLE in text:
        text = text.replace(OLD_PREAMBLE, NEW_PREAMBLE, 1)
    elif "servers:" in text and "tags:" not in text.split("paths:")[0]:
        # Insert tags before servers
        text = text.replace(
            "description: ''\nservers:",
            "description: ''\ntags:\n  - name: Getting Started\n    description: Authentication, login, and service account management\n  - name: Workspaces\n    description: Workspace CRUD and user management\n  - name: AI Extraction\n    description: Schema generation, extraction configs, and run triggers\n  - name: WorkBook\n    description: Tables (workbooks), columns, rows, and data operations\n  - name: Knowledge Graph\n    description: File upload, folder listing, and knowledge graph APIs\nservers:",
            1,
        )
        # Deduplicate servers
        text = re.sub(
            r"  - url: 'https://be\.datagol\.ai'\n  - url: 'https://be\.datagol\.ai'",
            "  - url: 'https://be.datagol.ai'\n    description: DataGOL backend API",
            text,
            count=1,
        )

    out_path = Path(__file__).resolve().parent / "openapi.yaml"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Written {out_path}", file=sys.stderr)

if __name__ == "__main__":
    main()
