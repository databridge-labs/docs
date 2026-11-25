# Repository architecture

[Documentation home](../README.md) · [Complete master plan](../architecture/master-plan.md)

> Design specification — proposed capabilities unless explicitly marked verified.

### 57. Target repository structure

```text
databridge/
  .github/
    workflows/ (ci.yml, release.yml, security.yml)
    ISSUE_TEMPLATE/, PULL_REQUEST_TEMPLATE.md, dependabot.yml
  src/databridge/
    __init__.py, __main__.py, cli.py, config.py, exceptions.py, py.typed
    connectors/
      __init__.py, base.py, registry.py
      databases/ (sqlite.py, postgresql.py, mysql.py, clickhouse.py)
      warehouses/ (snowflake.py, bigquery.py, redshift.py)
      files/ (csv.py, excel.py, json.py, parquet.py)
      storage/ (s3.py, azure_blob.py, gcs.py)
      api/ (rest.py)
    engine/
      pipeline.py, executor.py, extractor.py, transformer.py
      validator.py, loader.py, checkpoint.py, scheduler.py
    transformations/
      base.py, registry.py, filter.py, rename.py, cast.py
      join.py, aggregate.py
    quality/ (rules.py, uniqueness.py, completeness.py, schema.py,
              integrity.py)
    destinations/ (base.py, registry.py, csv.py, excel.py, json.py,
                   parquet.py, database.py, object_storage.py)
    metadata/ (models.py, repository.py, database.py, migrations/)
    security/ (secrets.py, masking.py)
    monitoring/ (logger.py, metrics.py, events.py)
    dashboard/ (app.py, pages/, components/)
  tests/ (unit/, integration/, end_to_end/, fixtures/)
  examples/ (pipelines/, queries/, datasets/)
  docs/ (architecture/, getting-started/, connectors/, transformations/,
         destinations/, development/)
  .env.example, .gitignore, .dockerignore, .python-version
  .pre-commit-config.yaml, Dockerfile, compose.yaml
  pyproject.toml, uv.lock, mkdocs.yml, README.md, LICENSE
  CHANGELOG.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md
```

Python package subdirectories include __init__.py where required. Add connector files as implemented.

### 58. Documentation and ADRs

```text
docs/architecture/overview.md, system-design.md, data-engine.md,
                  security.md, decisions/
docs/getting-started/installation.md, quickstart.md, first-pipeline.md
docs/development/setup.md, testing.md, contributing.md, release-process.md
docs/connectors/, transformations/, destinations/
```

| Area | Specification |
| --- | --- |
| ADR-001 | Python |
| ADR-002 | Modular monolith |
| ADR-003 | Arrow interchange |
| ADR-004 | Polars |
| ADR-005 | YAML |
| ADR-006 | Plugin architecture |
| ADR-007 | SQLite metadata |
| ADR-008 | Native Streamlit |

| Area | Specification |
| --- | --- |
| ADR-009 | uv |
| ADR-010 | Secure defaults |
