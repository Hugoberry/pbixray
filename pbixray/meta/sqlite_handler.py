import apsw
import pandas as pd

class SQLiteHandler:
    def __init__(self, sqlite_buffer):
        self.sqlite_buffer = sqlite_buffer
        self.conn = self._setup_connection()
        
    def _setup_connection(self):
        """Set up an in-memory SQLite connection and deserialize."""
        conn = apsw.Connection(":memory:")
        conn.deserialize("main", self.sqlite_buffer)
        return conn

    def execute_query(self, sql):
        """Execute a SQL query and return the result as a pandas DataFrame."""
        try:
            return pd.read_sql_query(sql, self.conn)
        except apsw.SQLError as e:
            print(f"SQL error: {e}")

    def close_connection(self):
        """Close the SQLite connection."""
        self.conn.close()
