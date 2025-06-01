import logging
from pathlib import Path
import sqlite3


class SQLiteHandler(logging.Handler):
    def __init__(self, fp: Path | str):
        self.fp = fp
        super().__init__()
        self._check_db()

    def emit(self, record):
        with self.lock:
            with sqlite3.connect(self.fp) as conn:
                print(record.getMessage())
                conn.execute(
                    "INSERT INTO records(record) VALUES (?);", (self.format(record),)
                )
                conn.commit()

    def _check_db(self):
        SCHEMA = "CREATE TABLE records (id INTEGER PRIMARY KEY, record TEXT)"
        with self.lock:
            if not Path(self.fp).exists():
                try:
                    with sqlite3.connect(self.fp) as conn:
                        conn.execute(
                            "CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY, record TEXT)"
                        )
                except Exception as exc:
                    raise exc

            with sqlite3.connect(self.fp) as db:
                schema = db.execute(
                    "SELECT * from sqlite_master WHERE type='table' AND name='records';"
                ).fetchone()
                if not schema:
                    raise KeyError("table not found in sqlite3 DB.")
                elif schema[4] != SCHEMA:
                    print(schema[4])
                    raise KeyError("incorrect DB schema")
