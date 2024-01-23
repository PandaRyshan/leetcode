import sqlite3
import threading


class Database:
    _instance = None
    _lock = threading.Lock()

    def __call__(cls, filename):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance._conn = sqlite3.connect(filename)
                cls._instance._cursor = cls._instance._conn.cursor()
        return cls._instance

    def close(self):
        self._conn.close()

    def execute(self, query):
        self._cursor.execute(query)

    def list_all_tables(self):
        self.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return self._cursor.fetchall()


db1 = Database('src/demo.db')
print(db1.list_all_tables())

db2 = Database('demo.db')
print(db2.list_all_tables())

print(db1 is db2)
