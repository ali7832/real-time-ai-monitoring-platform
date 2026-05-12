from fastapi import FastAPI

from ai_monitoring.schemas import HealthReport, MetricEvent
from ai_monitoring.service import MonitoringService

app = FastAPI(title='Real-Time AI Monitoring Platform')
_service = MonitoringService()


@app.get('/health')
def health() -> dict:
    return {'status': 'ok'}


@app.post('/metrics', response_model=HealthReport)
def ingest_metric(event: MetricEvent) -> HealthReport:
    return _service.process(event)
