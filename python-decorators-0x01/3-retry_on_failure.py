import time
import sqlite3
import functools
from dotenv import load_dotenv
import os

# ✅ Load env vars (if using .env for DB path)
load_dotenv()
DB_PATH = os.getenv("DB_PATH", "users.db")

# ✅ Reuse this from earlier
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect(DB_PATH)
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# ✅ Decorator to retry function on failure
def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"[Retry {attempt}/{retries}] Error: {e}")
                    time.sleep(delay)
            print("[‼️] All retries failed.")
            raise last_exception
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# ✅ Attempt fetch with automatic retries
users = fetch_users_with_retry()
print(users)
