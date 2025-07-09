import sqlite3

class ExecuteQuery:
    def __init__(self, query, params=(), db_path='users.db'):
        self.query = query
        self.params = params
        self.db_path = db_path
        self.conn = None
        self.result = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()
        cursor.execute(self.query, self.params)
        self.result = cursor.fetchall()
        return self.result  # This becomes the value returned by `with ... as result`

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()

# ✅ Use the context manager to run parameterized query
query = "SELECT * FROM users WHERE age > ?"
param = (25,)

with ExecuteQuery(query, param) as results:
    print(results)
