"""Copy an allowlisted static site, including downloadable lab assets."""
from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
dest=root/'_site'
dest.mkdir(exist_ok=True)
dirs={'assets','scenario','days','coursework','practice','coverage','templates','artefacts','infra','queries','notebooks','data','scripts'}
for p in root.iterdir():
    if p.is_file() and (p.suffix in ('.html','.md') or p.name in ('.nojekyll','LICENSE')):shutil.copy2(p,dest/p.name)
    elif p.is_dir() and p.name in dirs:shutil.copytree(p,dest/p.name,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
print('Packaged static pages and allowlisted practical assets in _site.')
