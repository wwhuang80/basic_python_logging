import logging
from pathlib import Path
import sqlite3


class SQLiteHandler(logging.Handler):
    def __init__(self, fp: Path | str):
        self.fp = fp
        super().__init__()
        self._load_db()

    def emit(self, record):
        with self.lock:
            with sqlite3.connect(self.fp) as conn:
                print(type(record.msg))
                print(record.msg)
                conn.execute("INSERT INTO records(record) VALUES (?);", (record.msg,))
                conn.commit()

    def _load_db(self):
        with self.lock:
            if not Path(self.fp).exists():
                try:
                    with sqlite3.connect(self.fp) as conn:
                        conn.execute(
                                "CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY, record TEXT);"
                                )
                except Exception as exc:
                    raise exc

            with sqlite3.connect(self.fp) as db:
                table = db.execute("PRAGMA table_info(table_name);")

if __name__=="__main__":
    hand = SQLiteHandler("abc.db")
    hand._load_db()
