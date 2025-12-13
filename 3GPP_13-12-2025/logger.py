import logging
import json
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("3GPPLogger")

def log_event(level, message, exception_code=None):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "level": level,
        "module": "Parser",
        "message": message,
        "exception_code": exception_code
    }
    logger.log(getattr(logging, level.upper(), logging.INFO), json.dumps(log_entry))