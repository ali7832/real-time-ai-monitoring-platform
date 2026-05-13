from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class MonitoringSettings:
    environment: str = os.getenv('AIMON_ENV', 'local')
    service_name: str = os.getenv('AIMON_SERVICE_NAME', 'real-time-ai-monitoring-platform')
    monitor_version: str = os.getenv('AIMON_MONITOR_VERSION', 'health-rules-v1')
    metric_store_path: str = os.getenv('AIMON_METRIC_STORE_PATH', 'metrics.jsonl')
    incident_store_path: str = os.getenv('AIMON_INCIDENT_STORE_PATH', 'incidents.jsonl')
    degraded_threshold: float = float(os.getenv('AIMON_DEGRADED_THRESHOLD', '0.65'))
    critical_threshold: float = float(os.getenv('AIMON_CRITICAL_THRESHOLD', '0.40'))


settings = MonitoringSettings()
