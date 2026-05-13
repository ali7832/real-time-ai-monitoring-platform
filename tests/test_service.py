from ai_monitoring.schemas import MetricEvent
from ai_monitoring.service import MonitoringService


def test_monitoring_service_returns_incident_for_bad_metrics():
    event = MetricEvent(
        service_name='rag-api',
        latency_ms=6000,
        error_rate=0.10,
        throughput_rpm=0,
        cost_usd=0.40,
        drift_score=0.50,
        service_version='1.2.0',
        environment='staging',
        region='eu-west',
    )

    report = MonitoringService().process(event)

    assert report.incident_id
    assert report.status in {'degraded', 'critical'}
    assert report.alerts
    assert report.monitor_version
    assert report.recommended_action != 'no_action_required'
