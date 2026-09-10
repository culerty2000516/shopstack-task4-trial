import os

from flask import Flask, jsonify

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "0.1.0")


@app.get("/")
def home():
    return jsonify(
        service="ShopStack Frontend",
        version=VERSION,
        message=f"Hello from ShopStack Frontend v{VERSION}",
    )


@app.get("/healthz")
def healthz():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
