from pathlib import Path
import logging
import sqlite3

import pytest
from hypothesis import given, settings, strategies as st

from python_std_logging import basic_logger


@pytest.fixture(autouse=True)
def cwd(monkeypatch, request):
    monkeypatch.chdir(request.fspath.dirname)

@given(st.text(st.characters(codec="ascii"), min_size=0, max_size=20))
@settings(max_examples=5)
def test_SQLiteHandler(text):
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    fp = output_dir / "test.db"

    logger = logging.getLogger(__name__)
    handler = basic_logger.SQLiteHandler(fp)
    logger.addHandler(handler)
    logger.critical(text)

    with sqlite3.connect(fp) as conn:
        last_entry = conn.execute("SELECT record FROM records ORDER BY id DESC LIMIT 1;").fetchone()
    assert last_entry[0] == text
