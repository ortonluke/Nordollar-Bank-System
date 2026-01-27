import sqlite3

conn = sqlite3.connect("bank.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    balance INTEGER NOT NULL
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT NOT NULL,
    receiver TEXT NOT NULL,
    amount INTEGER NOT NULL,
    timestamp INTEGER NOT NULL
)
""")

# Initial users
users = [
    ("Luke", 15),
    ("K", 100000000),
    ("Zach", 10)
]

cur.executemany(
    "INSERT OR IGNORE INTO accounts (name, balance) VALUES (?, ?)",
    users
)

conn.commit()
conn.close()
