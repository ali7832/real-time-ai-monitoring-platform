# ADR-001: Health Scoring and Incident Generation

## Status

Accepted

## Context

AI services need operational monitoring that goes beyond basic uptime checks. Teams need latency, error rate, throughput, cost, drift signals, alert reasons, incident IDs, and recommended actions in a single response that can feed dashboards and incident workflows.

## Decision

Use a lightweight health-scoring service that combines telemetry into a normalized health score, evaluates alert rules, and creates incident IDs for degraded or critical service states.

## Consequences

Benefits:

- API responses are useful for operators and demo stakeholders.
- Incidents are traceable through JSONL storage in local/demo mode.
- Monitoring logic is testable outside FastAPI routes.
- Recommended actions make the platform more practical for real operations.

Tradeoffs:

- JSONL storage is suitable for demos but should become a database or event stream in production.
- Rule-based health scoring is transparent, but production systems should support configurable SLO policies and historical baselines.
