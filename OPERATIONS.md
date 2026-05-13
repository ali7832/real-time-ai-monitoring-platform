# Operations Runbook

## Purpose

This service ingests AI service telemetry and returns health reports with alerts, incident IDs, and recommended actions.

## Runtime Configuration

Configuration is controlled through `.env.example`:

- `AIMON_ENV`: deployment environment.
- `AIMON_SERVICE_NAME`: platform service identifier.
- `AIMON_MONITOR_VERSION`: monitor rule version.
- `AIMON_METRIC_STORE_PATH`: JSONL metric event path.
- `AIMON_INCIDENT_STORE_PATH`: JSONL incident event path.
- `AIMON_DEGRADED_THRESHOLD`: degraded health threshold.
- `AIMON_CRITICAL_THRESHOLD`: critical health threshold.

## Metric Lifecycle

1. A service submits telemetry to `/metrics`.
2. The platform writes the metric event to JSONL storage.
3. Health score is calculated from latency, error rate, cost, and drift.
4. Alert rules detect operational risks.
5. Degraded or critical events receive an incident ID.
6. Incident records are persisted for review.
7. The API returns recommended action guidance.

## Demo Readiness

Expose `/health` and `/metrics` for hosted demos. The `/health` endpoint returns service name, environment, and monitor version.

## Production Roadmap

- Prometheus metrics export.
- Grafana dashboards.
- PagerDuty or Slack incident routing.
- SLO and error budget tracking.
- Model drift dashboards.
- Multi-service fleet views.
- Kubernetes deployment and autoscaling.
