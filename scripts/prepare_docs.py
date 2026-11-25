"""Stage canonical GitHub Markdown for MkDocs without duplicating source files."""
from pathlib import Path
import re
import shutil

root = Path(__file__).resolve().parents[1]
target = root / "site_docs"
if target.exists():
    shutil.rmtree(target)
target.mkdir()
for folder in ("project", "requirements", "architecture", "development"):
    shutil.copytree(root / folder, target / folder)
shutil.copyfile(root / "README.md", target / "index.md")
for page in target.rglob("*.md"):
    content = page.read_text(encoding="utf-8")
    content = content.replace("](../README.md)", "](../index.md)")
    content = content.replace("](architecture/diagrams/)", "](architecture/system-design.md)")
    page.write_text(content, encoding="utf-8")
