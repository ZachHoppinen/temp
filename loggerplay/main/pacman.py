from foo.bar import add
from log_test.spicy_logging import setup_logging
import logging

setup_logging(debug = True, log_dir = '../logs')

log = logging.getLogger(__name__)

add(1, 2)

log.debug("hello?")