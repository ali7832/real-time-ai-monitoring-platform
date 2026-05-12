from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from ai_monitoring.schemas import MetricEvent


def append_metric(event: MetricEvent, path: str | Path = 'metrics.jsonl') -> None:
    record = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        **event.model_dump(),
    }
    with Path(path).open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(record) + '\n')
