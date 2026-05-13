from fastapi import FastAPI

from ai_monitoring.config import settings
from ai_monitoring.schemas import HealthReport, MetricEvent, PlatformHealth
from ai_monitoring.service import MonitoringService

app = FastAPI(title='Real-Time AI Monitoring Platform', version='0.2.0')
_service = MonitoringService()


@app.get('/health', response_model=PlatformHealth)
def health() -> PlatformHealth:
    return PlatformHealth(
        status='ok',
        service_name=settings.service_name,
        environment=settings.environment,
        monitor_version=settings.monitor_version,
    )


@app.post('/metrics', response_model=HealthReport)
def ingest_metric(event: MetricEvent) -> HealthReport:
    return _service.process(event)
