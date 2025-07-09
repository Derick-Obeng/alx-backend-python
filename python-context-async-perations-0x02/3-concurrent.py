import aiosqlite
import asyncio

# ✅ Async function to fetch all users
async def async_fetch_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            results = await cursor.fetchall()
            return results

# ✅ Async function to fetch users older than 40
async def async_fetch_older_users():
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (40,)) as cursor:
            results = await cursor.fetchall()
            return results

# ✅ Run both queries concurrently and print the results
async def fetch_concurrently():
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("[All Users]", all_users)
    print("[Users > 40]", older_users)

# ✅ Entry point
if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
