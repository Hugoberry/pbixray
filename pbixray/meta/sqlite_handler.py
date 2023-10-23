import apsw
import pandas as pd
import warnings

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
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            try:
                return pd.read_sql_query(sql, self.conn)
            except apsw.ExecutionCompleteError:  
                return pd.DataFrame()  # Return an empty DataFrame for ExecutionCompleteError
            except apsw.SQLError as e:  # Handle other SQLErrors
                print(f"SQL error: {e}")
                return pd.DataFrame()  # Optional: Return an empty DataFrame or you can raise the error again

    def close_connection(self):
        """Close the SQLite connection."""
        self.conn.close()
