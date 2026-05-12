from __future__ import annotations

from ai_monitoring.schemas import MetricEvent


def calculate_health_score(event: MetricEvent) -> float:
    latency_penalty = min(event.latency_ms / 10000, 1.0) * 0.30
    error_penalty = min(event.error_rate, 1.0) * 0.35
    cost_penalty = min(event.cost_usd / 1.0, 1.0) * 0.15
    drift_penalty = min(event.drift_score, 1.0) * 0.20
    score = 1.0 - latency_penalty - error_penalty - cost_penalty - drift_penalty
    return round(max(0.0, min(1.0, score)), 4)


def status_from_score(score: float) -> str:
    if score >= 0.85:
        return 'healthy'
    if score >= 0.65:
        return 'degraded'
    return 'critical'
