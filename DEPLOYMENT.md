# Deployment Guide

## Local Development

```bash
pip install .[dev]
uvicorn ai_monitoring.api:app --reload
```

## CLI Demo

```bash
aimon demo
aimon submit
```

## Docker

```bash
docker build -t ai-monitoring .
docker run -p 8000:8000 ai-monitoring
```

## Docker Compose

```bash
docker-compose up --build
```

## Health Check

```bash
curl http://localhost:8000/health
```

## Submit Metrics

```bash
curl -X POST http://localhost:8000/metrics \
  -H 'Content-Type: application/json' \
  -d @sample_metric.json
```
