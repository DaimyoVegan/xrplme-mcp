# XRPLME Country Intelligence MCP

30-country economic, policy, and trade data for AI agents. Free discovery tier + x402 pay-per-call on XRPL and Solana.

## Quick Install

Add to your MCP client config:

```json
{
  "mcpServers": {
    "xrplme-country-data": {
      "url": "https://api.xrplme.online/mcp"
    }
  }
}
```

## Pricing

| Tool | Free | Country Brief (x402) | Deep Concierge (x402) | Custom Bounded (x402) |
|------|------|---------------------|----------------------|-----------------------|
| `xrplme_list_countries` | free | — | — | — |
| `xrplme_get_country_data_summary` | free | — | — | — |
| `xrplme_get_country_data` | — | 1 XRP / 1.00 USDC | 5 XRP / 7.00 USDC | 15 XRP / 15.00 USDC |
| `get_country_schema` | — | 1 XRP / 1.00 USDC | — | — |
| `get_country_data_health` | free | — | — | — |
| `get_country_data_pricing` | free | — | — | — |

Pay via XRPL (XRP) or Solana (USDC). The MCP server returns a 402 with both payment options. Three tiers: country_brief (1 XRP / 1.00 USDC), deep_concierge (5 XRP / 7.00 USDC), custom_bounded (15 XRP / 15.00 USDC).

## Available Tools

### Free
- `xrplme_list_countries` — List all 30 supported countries
- `xrplme_get_country_data_summary` — Summary data for a country
- `get_country_data_health` — Health check for a country data route
- `get_country_data_pricing` — Get current pricing for all tools

### Paid (x402)
- `xrplme_get_country_data` — Full economic/policy dataset for a country (slug + optional AI analysis)
- `get_country_schema` — JSON schema for a country's data structure

## Supported Countries

All 30 countries: australia, brazil, brunei, canada, france, germany, hong_kong, india, indonesia, italy, japan, korea, laos, macau, malaysia, mexico, myanmar, netherlands, newzealand, papua-new-guinea, philippines, singapore, switzerland, taiwan, thailand, timor-leste, uae, uk, usa, vietnam

## Links

- **Website:** https://xrplme.online
- **MCP Endpoint:** https://api.xrplme.online/mcp
- **x402 Solana routes:** https://xrplme.online/wc/v1/{country}/bot-solana[ /ai /custom ]
- **x402 XRPL routes:** https://xrplme.online/wc/v1/{country}/bot[/ai]
- **Registry entry:** io.github.DaimyoVegan/xrplme
