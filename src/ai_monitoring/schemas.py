from __future__ import annotations

from pydantic import BaseModel


class MetricEvent(BaseModel):
    service_name: str
    latency_ms: float
    error_rate: float
    throughput_rpm: float
    cost_usd: float = 0.0
    drift_score: float = 0.0


class HealthReport(BaseModel):
    service_name: str
    health_score: float
    status: str
    alerts: list[str]
