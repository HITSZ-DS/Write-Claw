# Write-Claw v0.1.0

This release adds two reusable host-specific package modes for Write-Claw:

- `write-claw-claude-plugin.zip`
  Claude-oriented plugin bundle with `.claude-plugin` layout, agents, prompts, and a story runtime skill.
- `write-claw-codex-skill.zip`
  Codex-oriented skill bundle with `AGENTS.md`, `.codex/skills`, and reusable writing templates.

## Included

- Homepage documentation for `Installation`, `Integrations`, `Plugin Usage`, and `Releases`
- Claude plugin source bundle under `integrations/claude-plugin-bundle`
- Codex skill source bundle under `integrations/codex-skill-bundle`
- Prepacked zip assets under `release/`

## How to use

### Claude

1. Download `write-claw-claude-plugin.zip`
2. Unzip into your target workspace
3. Keep `.claude-plugin` intact
4. Start from `prompts/session-kickoff.md`

### Codex

1. Download `write-claw-codex-skill.zip`
2. Copy `AGENTS.md`, `.codex/skills/write-claw-runtime`, and `templates/` into the target repository
3. Let Codex load the workspace rules and skill

## MCP note

MCP is not required for this release.  
Add MCP later only if you need a shared tool-calling layer for runtime control, memory access, or chapter synchronization.
