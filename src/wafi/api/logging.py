import json
import logging
import sys


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        return json.dumps(
            {
                "level": record.levelname,
                "message": record.getMessage(),
                "logger": record.name,
                "trace_id": getattr(record, "trace_id", None),
            }
        )


def configure(level: str) -> None:
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(JsonFormatter())
    r = logging.getLogger()
    r.handlers.clear()
    r.addHandler(h)
    r.setLevel(level)
