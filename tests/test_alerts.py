from ai_monitoring.alerts import evaluate_alerts
from ai_monitoring.schemas import MetricEvent


def test_alerts_detect_bad_metrics():
    event = MetricEvent(
        service_name='llm-api',
        latency_ms=4000,
        error_rate=0.10,
        throughput_rpm=0,
        cost_usd=0.50,
        drift_score=0.50,
    )
    alerts = evaluate_alerts(event)
    assert 'high_latency' in alerts
    assert 'high_error_rate' in alerts
    assert 'high_cost' in alerts
    assert 'model_drift' in alerts
    assert 'no_traffic' in alerts
