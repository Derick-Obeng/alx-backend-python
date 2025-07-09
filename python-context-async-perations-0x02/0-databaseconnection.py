import sqlite3

# ✅ Custom context manager for database connection
class DatabaseConnection:
    def __init__(self, db_path='users.db'):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn  # This is what gets assigned to `as` in the with statement

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

# ✅ Use the custom context manager to fetch users
with DatabaseConnection() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
