# Real-Time AI Monitoring Platform

Deployable AI operations monitoring platform for ingesting service telemetry, calculating health scores, generating alerts, creating incident IDs, and returning recommended operational actions.

## Core Capabilities

- AI service metric ingestion API
- Health scoring for latency, error rate, throughput, cost, and drift
- Alert rule evaluation
- Incident ID generation for degraded and critical states
- Recommended action guidance for operators
- JSONL metric event stream for local demo mode
- JSONL incident stream for local incident review
- Service version, environment, and region metadata
- FastAPI `/metrics` endpoint
- CLI workflows for demo and metric submission
- Runtime configuration through environment variables
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest coverage
- Operations runbook and architecture decision record

## Quickstart

```bash
pip install .[dev]
aimon demo
uvicorn ai_monitoring.api:app --reload
pytest -q
```

## API

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/metrics \
  -H 'Content-Type: application/json' \
  -d @sample_metric.json
```

## Docker

```bash
docker-compose up --build
```

## Runtime Configuration

See `.env.example` for monitor version, metric store path, incident store path, and health threshold settings.

## Documentation

- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `OPERATIONS.md`
- `docs/adr-001-health-scoring-and-incidents.md`
- `sample_metric.json`

## Production Roadmap

- Prometheus metrics export
- Grafana dashboards
- PagerDuty or Slack incident routing
- SLO and error budget tracking
- Model drift dashboards
- Multi-service fleet views
- Kubernetes deployment and autoscaling
