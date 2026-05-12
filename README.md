# Real-Time AI Monitoring Platform

Production-ready monitoring platform for AI/ML services, covering latency, error rate, throughput, model drift signals, cost, and service health.

## Features

- AI service metric ingestion
- Health scoring engine for latency, errors, cost, and drift
- Alert rule evaluation
- FastAPI monitoring API
- CLI workflows for demo and metric submission
- JSONL metric event storage
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest test suite
- Architecture and deployment documentation

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

## Docs

- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `sample_metric.json`

## Portfolio Highlights

- Demonstrates AI platform engineering and production monitoring
- Useful for LLM, RAG, ML model APIs, and agent systems
- Strong foundation for Prometheus/Grafana, alerting, SLOs, model drift monitoring, and AI service reliability engineering
