# TalkBrief Website

Official static website for TalkBrief, deployed to Cloudflare Pages.

Production: https://www.talkbrief.app

TalkBrief Web (separate application): https://web.talkbrief.app

- Homepage: `index.html`
- Support: `support/index.html`
- Terms: `terms/index.html`
- Privacy: `privacy/index.html`

## Deploy

The Pages project is `talkbrief-site`, production branch `main`.
Python 3 stages an explicit allowlist of public assets:

```sh
python scripts/stage.py
npx wrangler pages deploy dist --project-name talkbrief-site --branch main
```

Deploy `dist`, never the repository root. Docs, Git data, local scripts and
configuration are not part of the website. This project uses direct uploads;
pushing to GitHub alone does not publish a new version.

Cloudflare custom domain `www.talkbrief.app` must be associated with this Pages
project, and its proxied DNS CNAME targets `talkbrief-site.pages.dev`.
The existing `talkbrief-web` project and `web.talkbrief.app` are separate.

After publishing, verify all four routes, the Web and App Store links, desktop
and mobile layouts, and the local/live public-file SHA-256 hashes.

## Brand and product assets

The website logo is the current iOS `AppIcon-1024.png`; favicon and Apple touch
icon use the app's existing 80px and 180px assets. The Capture screenshot is from
the 2.7.1 UI verification run. The Web image contains synthetic demonstration
content. No customer recordings or account credentials are included.

Design and deployment evidence are under `docs/`.

