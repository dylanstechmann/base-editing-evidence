# Agent instructions

This is a personal hobby and learning project with substantial AI assistance.
Keep source-reported experiments, computational classifications, synthetic
fixtures and human functional outcomes distinct. No owner source review or
laboratory work is implied.

Run `PYTHONPATH=src python -m unittest discover -s tests -v` before committing.
The CLI has no guide-design or biological-execution interface. Its first release
audits study scope and explicit count denominators; it does not identify a
safe or effective editor. Unknown outcomes stay unknown, not zero. Preserve
coordinate conventions, source links, source-access limits and negative findings.
No doses, self-treatment instructions, private patient genomes or credentials.
Sibling repositories are pattern sources only; see NEIGHBORS.md. Do not import
their protocols, scores or rejuvenation claims as editing outcomes.

## Agent tooling (portable across harnesses)

<!-- agent-toolbox:installed -->

This repo vendors its agent tooling (no secrets inside) so Claude Code,
Cline, Codex, OpenCode, Kilo Code, Kimi Code and Grok share one setup:

- `.mcp.json` — project MCP servers:
  `scholar` (PubMed, OpenAlex, Semantic Scholar, CORE, ORCID, Crossref),
  `web` (Exa, Brave, Jina, Firecrawl), `github` (read-only, token via
  `gh auth token`), `context7` (library docs), `playwright` (browser).
- `opencode.json` — the same servers for OpenCode;
  `AGENT_TOOLS.md` has merge snippets for Codex / Cline / Kilo Code and
  CLI fallbacks for Kimi / Grok.
- `.claude/skills/` — project skills: citation-check, literature-search, web-research, secrets-guard, regen-guardrails, fold-providers.
- Keys: `~/.config/ai-keys.env` via the `agentkeys` loader — never in git,
  MCP config or chat. Run `secrets-guard` (`--staged`) before committing.
