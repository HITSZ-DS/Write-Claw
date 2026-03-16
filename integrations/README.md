# Integrations

This folder contains host-specific reusable packages for Write-Claw.

## Included

- `claude-plugin-bundle`
  Claude-oriented plugin package based on a `.claude-plugin` structure.
- `codex-skill-bundle`
  Codex-oriented skill package based on `AGENTS.md` and `.codex/skills`.

## MCP note

These packages do not require MCP.

Use MCP only when you need a shared tool-calling layer for operations such as:

- runtime control
- memory access
- chapter synchronization
- external process integration
