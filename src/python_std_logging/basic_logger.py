import logging
from pathlib import Path
import sqlite3

class SQLiteHandler(logging.Handler) -> logging.Handler:
    def __init__(local_path: Path | str):
        self.local_path = local_path
        super().init()

    def emit(self, record): 
        with self.lock:
            with sqlite3.connect(self.local_path) as conn:
                conn.execute("{}".format(record)
                conn.commit()

