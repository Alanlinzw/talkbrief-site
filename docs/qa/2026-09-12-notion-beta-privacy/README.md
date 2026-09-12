# Notion TestFlight privacy disclosure

Source `a0145bd`, published at `https://b78a6c89.talkbrief-site.pages.dev` and `https://www.talkbrief.app/privacy/`.

The Notion section now describes the implemented test service: explicit export, optional transcript/no audio, device-only credential, encrypted tokens, 10-minute pending authorization, 180-day inactivity expiry, immediate export-association removal, token revocation retries, and a hashed retry record retained for at most 24 hours after successful revocation. Availability is described as selected TestFlight builds plus an enabled test service. Obsidian remains planned and unavailable.

Only privacy/index.html changed. Existing styling and other public files were retained. Local and public browser checks at 390px and 1440px passed: no horizontal overflow, broken anchors or missing images. The immutable privacy HTML exactly matched source. Public Notion/optional integration/Obsidian sections matched source text, and all four official routes returned 200. See production.json, browser JSON records and screenshots.

This describes TalkBrief's implementation; it is not evidence of real Notion OAuth, token revocation or iPhone behavior. Those require the TestFlight acceptance run.
