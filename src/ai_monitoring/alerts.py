from __future__ import annotations

from ai_monitoring.schemas import MetricEvent


def evaluate_alerts(event: MetricEvent) -> list[str]:
    alerts: list[str] = []

    if event.latency_ms > 3000:
        alerts.append('high_latency')
    if event.error_rate > 0.05:
        alerts.append('high_error_rate')
    if event.cost_usd > 0.25:
        alerts.append('high_cost')
    if event.drift_score > 0.30:
        alerts.append('model_drift')
    if event.throughput_rpm < 1:
        alerts.append('no_traffic')

    return alerts
