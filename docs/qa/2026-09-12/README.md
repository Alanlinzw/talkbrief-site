# Official website production verification — 2026-09-12

Published at https://www.talkbrief.app with `/`, `/support/`, `/terms/`, and
`/privacy/`. All four return HTTP 200 over verified HTTPS; a nonexistent route
returns the custom 404 with HTTP 404.

Production deployment: `ae66ecf6-58bc-4802-bdff-cd5a480aeb2d`.
Deployed source: `fca7680b7c9aa25fc3fd7aaf90b8d6428739dd92`.
Cloudflare Pages project: `talkbrief-site`, production branch: `main`.
Custom domain, validation and verification all report `active`.

## Checks

- Four pages at 390px and 1440px: no horizontal document overflow, broken images,
  broken local anchors or duplicate IDs. One H1 per page.
- Support native disclosure opens with click and closes with Enter. Keyboard
  navigation reaches the skip link. No page errors or failed site requests.
- Header Web CTA was clicked and opened `https://web.talkbrief.app/login/` with
  title `Sign in - TalkBrief Web`.
- App Store link was verified using Apple's lookup API for the app bundle ID:
  https://apps.apple.com/us/app/talkbrief/id6772943796.
- All 13 served files verified. Ten match local SHA-256 directly. The three
  email-containing pages match the immutable Pages deployment byte-for-byte and
  the custom-domain response after reversing only Cloudflare email obfuscation.
  Raw and normalized results are recorded separately in `production.json`.
- Public logo bytes exactly match the current iOS `AppIcon-1024.png` SHA-256:
  `1ae2d3ac1d8a5db5de71882698cfc4863084d34cbb877dce1e219bf5cf103273`.
  Favicon and Apple touch icon use existing iOS 80px/180px assets.
- Existing `talkbrief-web` production deployment remains
  `d4c3c0dd-a494-4610-adab-d9c2c95e3de4`. Its configuration and application were not
  deployed or modified as part of this website work.

See `browser.json`, `production.json`, `homepage-desktop.png` and
`homepage-mobile.png`. Browser tests cover the public website and Web entry;
they do not claim a new authenticated CloudKit or iPhone device test.
