# Git Commit & Push

**Slash:** `/git-commit-push`  
**Natural language:** "Commit and push", "Push to remote"

## Purpose
Commit staged changes and push to remote.

## Subagent
Use [@git-commit-push](.cursor/agents/git-commit-push.md).

## Execute
1. Ensure files are staged (use @git-status-add first if needed)
2. Run `git commit -m "message"` (conventional: feat:, fix:, docs:, chore:)
3. Run `git push origin main`
