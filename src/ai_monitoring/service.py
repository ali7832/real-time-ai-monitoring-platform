from __future__ import annotations

from ai_monitoring.alerts import evaluate_alerts
from ai_monitoring.schemas import HealthReport, MetricEvent
from ai_monitoring.scoring import calculate_health_score, status_from_score
from ai_monitoring.storage import append_metric


class MonitoringService:
    def process(self, event: MetricEvent) -> HealthReport:
        append_metric(event)
        score = calculate_health_score(event)
        return HealthReport(
            service_name=event.service_name,
            health_score=score,
            status=status_from_score(score),
            alerts=evaluate_alerts(event),
        )
