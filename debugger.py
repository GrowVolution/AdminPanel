from datetime import datetime
from pathlib import Path
import os

_enhanced_logging = False
_log_dir = Path(__file__).parent / "logs"
_log_dir.mkdir(exist_ok=True)
_session_timestamp = datetime.now().strftime("%d%m%Y%H%M%S")


def get_time() -> str:
    offset = datetime.now().astimezone().utcoffset()
    hours = int(offset.total_seconds() // 3600)
    minutes = int((offset.total_seconds() % 3600) // 60)

    sign = '+' if offset.total_seconds() >= 0 else '-'
    offset_str = f"{sign}{abs(hours):02d}{abs(minutes):02d}"

    return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {offset_str}"


def log(category: str, message: str, enhanced: bool = False):
    if enhanced and not _enhanced_logging:
        return

    log_str = f"[{get_time()}] [{os.getpid()}] [{category.upper()}] {message}\n"
    with open(_log_dir / f"{_session_timestamp}.log", 'a') as file:
        file.write(log_str)


def debug_msg(message: str):
    log('debug', message, True)


def set_loglevel(debug: bool):
    global _enhanced_logging
    _enhanced_logging = debug
