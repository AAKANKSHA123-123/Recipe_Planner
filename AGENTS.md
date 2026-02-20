# Smart Recipe & Meal Planner — Agent Coordination

This project uses Cursor Rules, Hooks, Skills, Commands, and Subagents to demonstrate AI-assisted software engineering.

## Subagents

Use the appropriate agent when working on specific areas:

| Agent | When to Use | Files |
|-------|-------------|-------|
| **@frontagent** | UI, layout, Streamlit components | `app.py` |
| **@backend-agent** | Recipe logic, nutrition, data, shopping list | `src/*.py`, `src/data/*.json` |
| **@deploy-agent** | Deployment, Docker, requirements | `Dockerfile`, `requirements.txt` |
| **@git-agent** | Git commits, branches, CI workflows | `.gitignore`, `.github/workflows/` |
| **@kubernetes-agent** | Deploy to Kubernetes pods | `k8s/`, Deployment, Service manifests |
| **@plan-agent** | Architecture, docs, task breakdown | `README.md`, `AGENTS.md` |

## Commands

Commands live in **.cursor/commands/**. Invoke via slash menu or natural language:

| Command | File | Action |
|---------|------|--------|
| `Generate weekly meal plan` / `/meal-plan` | [commands/generate-meal-plan.md](.cursor/commands/generate-meal-plan.md) | Create 7-day plan |
| `Export shopping list` / `/export-shopping-list` | [commands/export-shopping-list.md](.cursor/commands/export-shopping-list.md) | Export as CSV |

## Rules

- **recipe-calorie.mdc** — If recipe calories > 500, mark as high-calorie
- **streamlit-ui.mdc** — UI conventions for Streamlit components

## Hooks

- **.cursor/hooks/** — Hook scripts
- **afterFileEdit** — When `recipes.json` is edited, runs `.cursor/hooks/after-file-edit.py` → `scripts/validate_recipes.py`

## Skills

- **nutrition-lookup** — Add/use nutrition lookup for ingredients
- **recipe-generation** — Add recipes, apply high-calorie rule
- **shopping-list-creation** — Create shopping list from meal plan
- **generate-meal-plan** — Command: Generate weekly meal plan
- **export-shopping-list** — Command: Export shopping list
