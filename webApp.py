from flask import Flask, request, jsonify, g
from flask import render_template
import sqlite3
import time

app = Flask(__name__)

DB_PATH = "bank.db"

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect("bank.db")
        g.db.row_factory = sqlite3.Row
        # Force rollback journal mode (avoids creating .db-wal/.db-shm)
        g.db.execute("PRAGMA journal_mode=DELETE;")
    return g.db


# Test DB connection
with app.app_context():
    db = get_db()
    print("DB opened:", db)


# Routes
@app.route("/accounts")
def accounts():
    db = get_db()
    rows = db.execute(
        "SELECT name, balance FROM accounts"
    ).fetchall()

    return render_template(
        "accounts.html",
        accounts=rows
    )


# Run App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1000, debug=True)

