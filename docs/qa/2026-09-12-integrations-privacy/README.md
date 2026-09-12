# Planned integration privacy disclosure — September 12, 2026

Published both Notion and Obsidian planned data flows at https://www.talkbrief.app/privacy/.
Deployment: https://eb40282d.talkbrief-site.pages.dev (source commit 3bc9899).

The policy explicitly states that both integrations are planned and not yet available. It describes voluntary authorization/export, content selection, server-held Notion tokens and association records, local Obsidian Markdown export and possible clipboard transfer, external sync, and independent exported copies. No unimplemented retention deadline or automatic deletion guarantee is asserted.

Before enabling real authorization/export: finalize retention, temporary payload/log handling, disconnect and deletion behavior; update website and in-app disclosures to the implemented behavior. Update the iOS privacy URL from GitHub Pages to https://www.talkbrief.app/privacy/ and review App Store privacy disclosures. App code, App Store metadata, and integration services were not changed in this website-only update.

Verification: all 13 public files returned HTTP 200 and matched staged hashes (Cloudflare email obfuscation normalized for affected HTML). The immutable deployment privacy HTML matched source bytes. Local and live checks at 390 and 1440 pixels found no horizontal overflow, missing images, or broken section anchors; 15 legal sections were present. Screenshots and JSON results are in this directory.

Sources checked:
- https://developers.notion.com/guides/get-started/authorization
- https://help.obsidian.md/uri
- https://developer.apple.com/app-store/review/guidelines/#privacy
