from __future__ import annotations

from uuid import uuid4

from ai_monitoring.alerts import evaluate_alerts
from ai_monitoring.config import settings
from ai_monitoring.incidents import append_incident
from ai_monitoring.schemas import HealthReport, MetricEvent
from ai_monitoring.scoring import calculate_health_score, status_from_score
from ai_monitoring.storage import append_metric


class MonitoringService:
    def process(self, event: MetricEvent) -> HealthReport:
        append_metric(event, path=settings.metric_store_path)
        score = calculate_health_score(event)
        status = status_from_score(score)
        alerts = evaluate_alerts(event)
        incident_id = str(uuid4()) if status in {'degraded', 'critical'} or alerts else None
        report = HealthReport(
            service_name=event.service_name,
            health_score=score,
            status=status,
            alerts=alerts,
            incident_id=incident_id,
            monitor_version=settings.monitor_version,
            environment=event.environment,
            recommended_action=self._recommended_action(status, alerts),
        )

        if incident_id:
            append_incident(
                {
                    'incident_id': incident_id,
                    'service_name': event.service_name,
                    'status': status,
                    'alerts': alerts,
                    'event': event.model_dump(),
                    'report': report.model_dump(),
                },
                settings.incident_store_path,
            )

        return report

    @staticmethod
    def _recommended_action(status: str, alerts: list[str]) -> str:
        if status == 'critical':
            return 'page_on_call_and_investigate_immediately'
        if 'model_drift' in alerts:
            return 'review_model_drift_and_recent_data_distribution'
        if 'high_error_rate' in alerts:
            return 'inspect_application_logs_and_recent_deployments'
        if 'high_latency' in alerts:
            return 'check_service_capacity_and_downstream_dependencies'
        if status == 'degraded':
            return 'monitor_service_and_prepare_mitigation'
        return 'no_action_required'
