# Risks and project boundaries

[Documentation home](../README.md) · [Complete master plan](../architecture/master-plan.md)

> Design specification — proposed capabilities unless explicitly marked verified.

### 77. Risks

| Area | Specification |
| --- | --- |
| Excessive scope (high) | Incremental milestones |
| Type incompatibility (high) | Explicit mapping and tests |
| Memory exhaustion (high) | Batch and disk-backed processing |
| Silent corruption (critical) | Integrity validation |
| Credential exposure (critical) | Secure resolution |
| Duplicate writes (high) | Checkpoints and idempotency |
| Connector maintenance (high) | Contracts and integration tests |
| Dependency conflicts (medium) | Optional extras and locks |
| Config changes (medium) | Schema versioning |
| Scheduler overlap (high) | Locking |
| Untrusted plugins (high) | Trusted installation and docs |
| Insufficient testing (high) | CI gates |
| Name/license conflict (high) | Verify before publishing |
| Limited capacity (high) | Prioritize and onboard contributors |

### 78. Excluded initially

Spark, Kafka, Kubernetes, microservices, custom database or Rust/C++ engine, React/Angular, distributed worker clusters, full CDC, machine learning platform, BI visualization platform and commercial managed services. Existing engines and native Streamlit meet initial needs.

### 79. Definition of done

Typed, documented, tested and reviewed against requirements; supported environments; no known critical security or integrity defects. Release requires passing tests, successful builds, verified installation, updated docs and explicit limitations.
