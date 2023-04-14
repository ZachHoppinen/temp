import logging
log = logging.getLogger(__name__)

def add(x, y):
    log.debug(f"adding {x}, {y}")
    return x + y