import logging

import pytest
from python_std_logging import basic_logger


def test_SQLiteHandler(tmpdir):
#     fp = tmpdir / "test.db"
    fp = "test.db"
    logger = logging.getLogger(__name__)
    handler = basic_logger.SQLiteHandler(fp)
    logger.addHandler(handler)
    logger.critical("test message")
    assert False

