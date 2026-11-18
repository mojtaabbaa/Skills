---
name: figma-mcp
description: Figma's official MCP server: gives AI coding agents design context from Figma frames, variables and Code Connect; remote server can also write to the canvas.
---

# Figma MCP

## Overview
Figma's official MCP server: gives AI coding agents design context from Figma frames, variables and Code Connect; remote server can also write to the canvas.

- **Source Repository**: https://github.com/figma/mcp-server-guide
- **Safety Profile**: Safety: Official hosted server with Figma OAuth; the guide repo has no server code but bundles skills with scripts, and the remote tools can write to your Figma files.

## Workflow & Guidelines
Install the "Figma MCP" MCP server for Google Antigravity.
Follow the steps at https://www.antigravityskills.org/install/figma-mcp.md (source: https://github.com/figma/mcp-server-guide).
If you cannot open that link, read it in the terminal with curl -s https://www.antigravityskills.org/install/figma-mcp.md and run its commands as written; do not write the skill files yourself.
Before running anything, show me what you will download and whether it includes scripts, and wait for my OK.
Ask me for any keys or paths it needs. When done, check that it is listed under Installed MCP Servers.

## Implementation Best Practices
1. Integrate cleanly with UI design systems, token architectures, and theme variables.
2. Adhere to strict WCAG 2.2 contrast ratios and minimum 44x44px touch targets.
3. Preserve responsive layouts across desktop, tablet, and mobile viewports.
4. Support bi-directional layouts (RTL/LTR) gracefully.
