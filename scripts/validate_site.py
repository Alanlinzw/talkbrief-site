"""Validate public routes, legal anchors, and Slack disclosure before deploy."""

from html.parser import HTMLParser
from pathlib import Path


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.anchors = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            self.ids.add(values["id"])
        if tag == "a" and values.get("href", "").startswith("#"):
            self.anchors.append(values["href"][1:])


root = Path(__file__).resolve().parents[1]
for route in ["index.html", "support/index.html", "terms/index.html", "privacy/index.html"]:
    path = root / route
    if not path.is_file():
        raise SystemExit(f"Missing public route: {route}")
    parser = Page()
    parser.feed(path.read_text(encoding="utf-8"))
    missing = sorted(set(parser.anchors) - parser.ids)
    if missing:
        raise SystemExit(f"Broken anchors in {route}: {missing}")

privacy = (root / "privacy/index.html").read_text(encoding="utf-8")
privacy_text = " ".join(privacy.split())
for phrase in [
    'id="slack"',
    "permission to post to one channel you select",
    "for no more than 10 minutes",
    "do not pass through the TalkBrief Slack integration service",
    "stored in this device's iOS Keychain",
    "Audio and transcript are not included",
    "Disconnect asks Slack to revoke the token and webhook",
]:
    if phrase not in privacy_text:
        raise SystemExit(f"Missing Slack privacy disclosure: {phrase}")

support = (root / "support/index.html").read_text(encoding="utf-8")
support_text = " ".join(support.split())
for phrase in ["How do I post a brief to Slack?", "Profile → Integrations → Slack", "does not include audio or the transcript"]:
    if phrase not in support_text:
        raise SystemExit(f"Missing Slack support guidance: {phrase}")

print("PASS four public routes, anchors, Slack privacy disclosure, and Slack support guidance")
