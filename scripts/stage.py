"""Stage only public website files for Cloudflare Pages; emits a hash manifest."""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
FILES=['index.html','support/index.html','terms/index.html','privacy/index.html','404.html','robots.txt','sitemap.xml','_headers','assets/styles.css','assets/talkbrief-icon.png','assets/talkbrief-icon-192.png','assets/favicon.png','assets/favicon-64.png','assets/favicon-32.png','assets/apple-touch-icon.png','assets/iphone-capture.png','assets/web-workspace.jpg']
OUT.mkdir(exist_ok=True)
existing={p.relative_to(OUT).as_posix() for p in OUT.rglob('*') if p.is_file()}
unexpected=existing-set(FILES)
if unexpected: raise RuntimeError(f'Unexpected staged files; inspect before deployment: {unexpected}')
manifest={}
for name in FILES:
    target=OUT/name
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(ROOT/name,target)
    manifest[name]={'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
print(json.dumps(manifest,indent=2))
