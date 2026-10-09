# MCP Registry Publish Package

This directory contains everything needed to publish the XRPLME Country Intelligence MCP server to the official MCP Registry.

## Files

- `server.json` — registry metadata (namespace: io.github.DaimyoVegan/xrplme)
- `README.md` — server documentation with tool descriptions and pricing
- `slugs.py` — exact 30 country slugs from the live server

## Publish Steps

```bash
# 1. Install mcp-publisher CLI (binary download, no npm needed for remote-only)
curl -L "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher

# 2. Login with GitHub (device flow)
./mcp-publisher login github
# → Visit https://github.com/login/device, enter code

# 3. Validate before publishing
./mcp-publisher validate

# 4. Publish
./mcp-publisher publish

# 5. Verify
curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.DaimyoVegan/xrplme"
```

## Notes

- Namespace must be `io.github.DaimyoVegan/...` (matches GitHub user)
- Only 100 char description limit — current description is 96 chars (OK)
- Remote-only: no npm package needed, just server.json + remote URL
- The `/.well-known/server-card.json` is already live on both apex and api.xrplme.online
