# Deployment and distribution

[Documentation home](../README.md) · [Complete master plan](../architecture/master-plan.md)

> Design specification — proposed capabilities unless explicitly marked verified.

### 65. Installation

```bash
pip install databridge
uv tool install databridge
git clone <official-repository-url>
cd databridge
uv sync
docker compose up -d
```

Intended commands only; name, repository and container not verified or published.

### 66. Deployment models

Local workstation, self-hosted Linux/Windows server, reproducible Docker container or external orchestration via CLI/SDK.

### 67. Optional dependencies

```bash
pip install "databridge[postgresql]"
pip install "databridge[mysql]"
pip install "databridge[clickhouse]"
pip install "databridge[excel]"
pip install "databridge[s3]"
pip install "databridge[dashboard]"
```

Install only needed drivers and SDKs to reduce conflicts, size and exposure.

### 68. System requirements

| Resource | Minimum | Recommended |
| --- | --- | --- |
| CPU | 2 cores | 4–8 cores |
| RAM | 4 GB | 8–16 GB |
| Disk | 2 GB plus data | SSD, workload-specific |
| Python | 3.12 | Supported 3.12 release |
| OS | Linux, Windows, macOS | Linux for persistent service |
| Network | Source-dependent | Reliable |

Proposed development requirements; actual needs depend on data, operations and concurrency.
