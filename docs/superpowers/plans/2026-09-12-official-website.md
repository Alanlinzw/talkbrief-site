# TalkBrief Website Implementation Plan

**Goal:** Publish the approved four-page website at https://www.talkbrief.app.

**Architecture:** Static HTML pages share assets/styles.css. Native HTML navigation and disclosures keep the site usable without JavaScript. Cloudflare Pages serves a public-file-only staged directory.

**Tech Stack:** HTML, CSS, Python authoring/verification helpers, Playwright browser checks, Cloudflare Pages.

1. Record baseline repository revision, inspect current Pages projects and DNS.
2. Implement the shared stylesheet and page navigation; rewrite homepage and support; update factual privacy content and add legal section navigation.
3. Stage only index.html, support/, terms/, privacy/, assets/, 404.html, robots.txt, sitemap.xml and headers. Never upload Git, docs or local scripts.
4. Serve locally; check every route, anchor, asset and 390/1440px layout. Visually inspect saved homepage and legal screenshots; validate disclosures and keyboard focus.
5. Commit scoped website changes, push to the requested repository, deploy to the website Pages project and associate www.talkbrief.app with matching DNS.
6. Verify production deployment/custom domain TLS and HTTP status, compare public-file hashes, record evidence and deployment instructions.

User approval already covers execution and deployment; proceed without a repeated implementation or publication approval.
