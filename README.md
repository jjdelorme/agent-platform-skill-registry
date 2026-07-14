# Gemini Agent Platform Skill Registry

> [!NOTE]
> This skill is designed for managing and orchestrating skills in the **Gemini Enterprise Agent Platform Skill Registry**.
> For full details, official guides, and architectural designs, refer to the [Gemini Enterprise Agent Platform Skill Registry Source Docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/skill-registry).

An open-standard skill package and command-line utility to discover, register, and manage modular AI agent skills on the **Gemini Enterprise Agent Platform Skill Registry** (built on Vertex AI).

---

## Features

-   **Skill Discovery** – Easily search, list, fetch, and inspect detailed revision histories of registered skills.
-   **Skill Lifecycle Management** – Upload, update, and delete registry skills.
-   **Portability & Genericity** – Fully customizable API endpoint suffixes, version segments, and protocols. Supports parameters passed via CLI flags or environment variables.
-   **Security-First Safe Zipping** – Automatically filters out local development files, environment files, and large builds (`.git`, `.env`, `node_modules`, `__pycache__`) to prevent credential leaks and bloated uploads.

---

## Installation via `npx skills`

This repository strictly implements the **Agent Skills open standard**. You can install and integrate this skill natively into supported AI coding agents (such as Claude Code, Cursor, Windsurf, and more) using the `skills.sh` package manager:

```bash
npx skills add jjdelorme/agent-platform-skill-registry
```

---

## Configuration & Prerequisites

### 1. Google Cloud Authentication
Ensure you have authenticated your local system or runtime environment using Google Cloud's Application Default Credentials (ADC):
```bash
gcloud auth application-default login
```

### 2. Required Parameters
The utilities require a Google Cloud Project ID and Region/Location. They can be set either via OS environment variables or passed explicitly as CLI arguments to commands.

**Environment Fallbacks:**
-   `GCP_PROJECT_ID`: Your Google Cloud Project ID.
-   `GCP_LOCATION`: The targeted Vertex AI region (e.g., `us-central1`).

---

## Basic CLI Usage

### Environment Pre-check
Before invoking operations, you can validate your configuration parameters:
```bash
# Validating using environment variables
python3 scripts/validate_env.py

# Validating using explicit CLI overrides
python3 scripts/validate_env.py --project "my-gcp-project" --location "us-central1"
```

### Uploading a Skill
Upload a local skill folder to the remote Skill Registry:
```bash
python3 scripts/skill_registry_ops.py upload \
  --project "my-gcp-project" \
  --location "us-central1" \
  --skill-id "my-custom-skill" \
  --display-name "My Custom Skill" \
  --description "A helpful tool for performing specific actions." \
  --folder "./path/to/skill/directory"
```

### Searching Skills
Search for skills in the registry by keywords:
```bash
python3 scripts/skill_registry_ops.py search --query "performance tuning"
```

### Customizing API Endpoints (Advanced)
To support sovereign clouds, air-gapped zones, VPC service controls, or staging environments, customize the endpoint resolution using environment parameters:
```bash
# Use a pre-production API version or custom endpoint domain suffix
export SKILL_REGISTRY_API_VERSION="v1"
export GCP_VERTEX_ENDPOINT_SUFFIX="custom-aiplatform.p.googleapis.com"

# Run your registry commands normally
python3 scripts/skill_registry_ops.py list
```

---

## Directory Structure

```text
agent-platform-skill-registry/
├── SKILL.md            # Skill manifest, guidelines, and core prompt instructions
├── package.json        # Unified NPM/editor integration metadata
├── README.md           # Getting started and installation documentation (this file)
├── scripts/            # Executable operations utilities
│   ├── skill_registry_ops.py
│   └── validate_env.py
└── references/         # In-depth operation manuals (query, manage, monitor, scaffolding)
```
