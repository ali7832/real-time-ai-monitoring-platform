from ai_monitoring.schemas import MetricEvent
from ai_monitoring.scoring import calculate_health_score, status_from_score


def test_health_score_for_good_service():
    event = MetricEvent(
        service_name='rag-api',
        latency_ms=500,
        error_rate=0.01,
        throughput_rpm=100,
        cost_usd=0.01,
        drift_score=0.02,
    )
    score = calculate_health_score(event)
    assert score > 0.85
    assert status_from_score(score) == 'healthy'


def test_status_for_critical_score():
    assert status_from_score(0.4) == 'critical'
