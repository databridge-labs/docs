# Documentation website

The canonical Markdown remains in the repository root and its existing folders. The preparation script stages a temporary MkDocs source directory, so GitHub and the website use the same content.

## Local development

```bash
uv venv
uv pip install -r requirements.txt
uv run --no-sync python scripts/prepare_docs.py
uv run --no-sync mkdocs serve
```

Open http://127.0.0.1:8000. Rerun the preparation script after editing canonical Markdown.

## GitHub Pages

In repository Settings → Pages, select GitHub Actions as the build source, if available on the organization plan. Run the Documentation website workflow. The intended URL is https://databridge-labs.github.io/docs/.

**Privacy:** Confirm the intended site audience before enabling Pages. A private source repository does not necessarily mean a private published site. Do not change repository visibility merely to enable hosting.

The workflow builds on pull requests and deploys on main pushes or manual runs. Deployment requires Pages to be enabled.
