import sqlite3
import functools
from dotenv import load_dotenv
import os

# ✅ Load env vars from .env
load_dotenv()
DB_PATH = os.getenv("DB_PATH", "users.db")  # default fallback

# ✅ Decorator to inject database connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect(DB_PATH)
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# ✅ Decorator to wrap a function inside a DB transaction
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()  # ✅ Commit if no error
            return result
        except Exception as e:
            conn.rollback()  # ❌ Rollback on any failure
            print(f"[Transaction Error] {e}")
            raise
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

# ✅ Update user's email inside safe transaction
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
