# Monitoring and scheduling

[Documentation home](../README.md) · [Complete master plan](../architecture/master-plan.md)

> Design specification — proposed capabilities unless explicitly marked verified.

### 50. Logging

```json
{
  "timestamp": "2026-11-25T17:00:00Z",
  "level": "INFO",
  "pipeline": "customer_orders",
  "run_id": "example-run-001",
  "stage": "extraction",
  "event": "batch_completed",
  "rows": 50000,
  "duration_seconds": 2.41
}
```

### 51. Metrics

Total, successful and failed runs; total and stage durations (extract, transform, validate, load); extracted, loaded and rejected rows; quality failures; retry attempts; throughput.

### 52. Scheduling

Proposed APScheduler; cron and interval schedules, manual runs, time zones and missed-run policies. Requires an active process or persistent service. Prevent overlaps, lock executions and document recovery.

### 53. External orchestration

Airflow, Prefect, Dagster, cron and systemd can invoke CLI or SDK; no need for a distributed orchestration system.
