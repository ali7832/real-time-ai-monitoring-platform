import typer
from rich.console import Console

from ai_monitoring.schemas import MetricEvent
from ai_monitoring.service import MonitoringService

app = typer.Typer(help='Real-time AI monitoring CLI')
console = Console()


@app.command()
def submit(
    service_name: str = 'rag-api',
    latency_ms: float = 850,
    error_rate: float = 0.01,
    throughput_rpm: float = 120,
    cost_usd: float = 0.02,
    drift_score: float = 0.05,
) -> None:
    event = MetricEvent(
        service_name=service_name,
        latency_ms=latency_ms,
        error_rate=error_rate,
        throughput_rpm=throughput_rpm,
        cost_usd=cost_usd,
        drift_score=drift_score,
    )
    report = MonitoringService().process(event)
    console.print_json(data=report.model_dump())


@app.command()
def demo() -> None:
    submit()
