from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

def get_conn():
    return pymysql.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"],
        connect_timeout=5
    )

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/metadata/latest")
def latest():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT file_name, processed_at, status FROM metadata ORDER BY id DESC LIMIT 5")
            rows = cur.fetchall()
        return jsonify(rows), 200
    finally:
        conn.close()
