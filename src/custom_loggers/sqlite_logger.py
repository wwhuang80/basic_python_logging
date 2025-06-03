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
            conn = sqlite3.connect(self.fp)
            with conn:
                conn.execute(
                    "INSERT INTO records(record) VALUES (?);", (self.format(record),)
                )
                conn.commit()
            conn.close()

    def _check_db(self):
        SCHEMA = "CREATE TABLE records (id INTEGER PRIMARY KEY, record TEXT)"
        with self.lock:
            if not Path(self.fp).exists():
                conn = sqlite3.connect(self.fp) 
                try:
                    with conn:
                        conn.execute(
                            "CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY, record TEXT)"
                        )
                except Exception as exc:
                    raise exc
                finally:
                    conn.close()

            conn = sqlite3.connect(self.fp)
            with conn:
                schema = conn.execute(
                    "SELECT * from sqlite_master WHERE type='table' AND name='records';"
                ).fetchone()
                if not schema:
                    raise KeyError("table not found in sqlite3 DB.")
                elif schema[4] != SCHEMA:
                    print(schema[4])
                    raise KeyError("incorrect DB schema")
            conn.close()
