from __future__ import annotations

from pydantic import BaseModel, Field


class MetricEvent(BaseModel):
    service_name: str
    latency_ms: float = Field(..., ge=0)
    error_rate: float = Field(..., ge=0, le=1)
    throughput_rpm: float = Field(..., ge=0)
    cost_usd: float = Field(default=0.0, ge=0)
    drift_score: float = Field(default=0.0, ge=0, le=1)
    service_version: str = 'unknown'
    environment: str = 'local'
    region: str = 'local'


class HealthReport(BaseModel):
    service_name: str
    health_score: float
    status: str
    alerts: list[str]
    incident_id: str | None
    monitor_version: str
    environment: str
    recommended_action: str


class PlatformHealth(BaseModel):
    status: str
    service_name: str
    environment: str
    monitor_version: str
