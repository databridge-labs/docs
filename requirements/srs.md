# Software requirements specification

[Documentation home](../README.md) · [Complete master plan](../architecture/master-plan.md)

> Design specification — proposed capabilities unless explicitly marked verified.

### 10. Purpose and scope

Define, execute, monitor and manage pipelines through code, configuration and a graphical console. P0 essential; P1 core; P2 advanced; P3 future.

### 11. Functional requirements

#### 11.1 Source connectivity

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-001 | Connect relational databases | P0 |
| FR-002 | Connect analytical databases | P0 |
| FR-003 | Test connections | P0 |
| FR-004 | Secure credentials | P0 |
| FR-005 | Parameterized SQL | P0 |
| FR-006 | Configurable batches | P0 |
| FR-007 | Discover schemas and tables | P1 |
| FR-008 | Discover column types | P1 |
| FR-009 | Read CSV Excel JSON Parquet | P1 |
| FR-010 | REST APIs | P2 |
| FR-011 | Object storage | P2 |
| FR-012 | Connection timeouts | P0 |
| FR-013 | TLS | P0 |
| FR-014 | External plugins | P2 |

#### 11.2 Pipeline management

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-015 | YAML pipelines | P0 |
| FR-016 | Validate configuration | P0 |
| FR-017 | CLI execution | P0 |
| FR-018 | Python SDK | P1 |
| FR-019 | Named connections | P1 |
| FR-020 | Multiple input datasets | P1 |
| FR-021 | Execution parameters | P1 |
| FR-022 | Dependencies | P2 |
| FR-023 | Scheduling | P2 |

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-024 | Retries | P2 |
| FR-025 | Cancellation | P2 |
| FR-026 | Incremental extraction | P2 |
| FR-027 | Checkpoint recovery | P2 |
| FR-028 | Dry-run validation | P1 |

#### 11.3 Transformations

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-029 | Select/remove columns | P1 |
| FR-030 | Rename | P1 |
| FR-031 | Filter | P1 |
| FR-032 | Cast | P1 |
| FR-033 | Normalize strings | P1 |
| FR-034 | Missing values | P1 |
| FR-035 | Sort | P1 |
| FR-036 | Join | P1 |
| FR-037 | Aggregate/group | P1 |
| FR-038 | Calculated columns | P1 |
| FR-039 | Explicit deduplication | P1 |
| FR-040 | Local SQL | P2 |
| FR-041 | Custom Python | P2 |
| FR-042 | Conditional transformations | P2 |
| FR-043 | Schema mapping | P2 |
| FR-044 | Nested data | P2 |

#### 11.4 Quality

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-045 | Required columns | P0 |
| FR-046 | Expected schemas | P1 |
| FR-047 | Uniqueness | P1 |
| FR-048 | Non-null | P1 |
| FR-049 | Data types | P1 |

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-050 | Allowed values | P1 |
| FR-051 | Ranges | P1 |
| FR-052 | Row counts | P1 |
| FR-053 | Detect duplicates | P1 |
| FR-054 | Detect conflicts | P1 |
| FR-055 | Join cardinality | P1 |
| FR-056 | Quality reports | P1 |
| FR-057 | Warn/fail policies | P1 |
| FR-058 | Quarantine | P2 |
| FR-059 | Schema drift | P2 |
| FR-060 | Thresholds | P2 |

#### 11.5 Destinations

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-061 | CSV | P0 |
| FR-062 | Excel | P0 |
| FR-063 | Parquet | P1 |
| FR-064 | JSON/NDJSON | P1 |
| FR-065 | Database writes | P1 |
| FR-066 | Object storage | P2 |
| FR-067 | Append/overwrite | P1 |
| FR-068 | Upsert | P2 |
| FR-069 | Atomic local publication | P0 |
| FR-070 | Compression | P2 |
| FR-071 | Partitioned datasets | P2 |
| FR-072 | Spreadsheet formula injection prevention | P0 |

#### 11.6 Observability

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-073 | Unique run IDs | P0 |
| FR-074 | Start/end times | P0 |

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-075 | Status | P0 |
| FR-076 | Sanitized structured logs | P0 |
| FR-077 | Extracted/loaded counts | P0 |
| FR-078 | History | P1 |
| FR-079 | Validation results | P1 |
| FR-080 | Stage metrics | P1 |
| FR-081 | Dataset lineage | P2 |
| FR-082 | Export metrics | P2 |
| FR-083 | Log retention | P2 |

#### 11.7 Graphical interface

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-084 | Overview | P2 |
| FR-085 | Connection definitions | P2 |
| FR-086 | Schema browsing | P2 |
| FR-087 | Controlled SQL workspace | P2 |
| FR-088 | Pipeline editing | P2 |
| FR-089 | Execute pipelines | P2 |
| FR-090 | History | P2 |
| FR-091 | Logs | P2 |
| FR-092 | Quality reports | P2 |
| FR-093 | Authorized outputs | P2 |
| FR-094 | Schedules | P2 |
| FR-095 | Settings | P2 |

Conflicting records must never be silently discarded; explicit policies are required.

### 12. Non-functional requirements

| ID | Requirement |
| --- | --- |
| NFR-001 | Windows/Linux/macOS portability |
| NFR-002 | Minimize copying |
| NFR-003 | Configurable batches |
| NFR-004 | Avoid mandatory full loading |

| ID | Requirement |
| --- | --- |
| NFR-005 | No credentials in logs |
| NFR-006 | Encrypted connections |
| NFR-007 | Least privilege |
| NFR-008 | Fail on critical validation |
| NFR-009 | No incomplete local output |
| NFR-010 | Separated responsibilities |
| NFR-011 | Independent connectors |
| NFR-012 | Unit/integration/E2E tests |
| NFR-013 | Actionable errors |
| NFR-014 | Versioned configs |
| NFR-015 | Execution traceability |
| NFR-016 | Supported version matrix |
| NFR-017 | Public interface documentation |
| NFR-018 | Minimal sensitive retention |
| NFR-019 | No mandatory hosted service |
| NFR-020 | Usable CLI and console |

### 13. Performance targets

Proposed, not measured: lightweight CLI startup under 2 seconds; 1 million representative records; bounded-memory demonstration with 10 million; configurable batches; 85% core coverage before v1.0; no silent record loss or plaintext credentials in logs; terminal status for completed/reconciled runs. Record hardware, row width, types, network, versions and complexity in benchmarks.
