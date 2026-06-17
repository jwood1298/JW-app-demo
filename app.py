from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    user = request.args.get("user")
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE name = '{user}'"
    result = conn.execute(query).fetchall()
    return str(result)

app.run(host="0.0.0.0", port=5000)