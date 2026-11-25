# Security architecture

[Documentation home](../README.md) · [Complete master plan](../architecture/master-plan.md)

> Design specification — proposed capabilities unless explicitly marked verified.

### 46. Security principles

Least privilege, secure defaults, explicit secrets, restricted logging, dependency security and fail-safe execution.

### 47. Credentials

Initial environment variables and development .env; optional OS keyring; advanced AWS Secrets Manager, Azure Key Vault and Google Secret Manager. Environment variables and .env are not encrypted vaults; enforce OS permissions.

```yaml
connection:
  type: postgresql
  host: ${POSTGRES_HOST}
  username: ${POSTGRES_USER}
  password: ${POSTGRES_PASSWORD}
```

### 48. Security requirements

| Area | Specification |
| --- | --- |
| Credential leakage | Secret references and redaction |
| SQL injection | Parameters and safe identifiers |
| Unauthorized access | Least privilege |
| Interception | TLS and certificate verification |
| Spreadsheet injection | Safe CSV/Excel export |
| Malicious YAML | Safe parsing and validation |
| Plugins | Trusted installation |
| Path traversal | Path validation and boundaries |
| Dependencies | Auditing and updates |
| Sensitive logs | Sanitization and retention |
| Partial output | Staged writes and atomic publication where supported |
| Console access | Localhost default and protected deployment |
| Resource exhaustion | Timeouts, batch limits, controls |
| Unsafe transforms | No arbitrary expression evaluation |
| Temporary files | Restricted permissions and cleanup |

User SQL is executable; parameters do not make arbitrary SQL safe. Use read-only source accounts unless writes are explicitly required.

### 49. Privacy

No central transmission of user data, credentials or metadata. Any future telemetry must be opt-in and documented. No raw records in logs; quarantine and intermediate persistence explicitly configured.
