import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://hoodblaqo.github.io"]}})

def valid_codes():
    codes = {item.strip().upper() for item in os.getenv("ACCESS_CODES", "").split(",") if item.strip()}
    extra_codes = {item.strip().upper() for item in os.getenv("EXTRA_CODES", "").split(",") if item.strip()}
    codes.update(extra_codes)
    test_code = os.getenv("TEST_CODE", "").strip().upper()
    if test_code:
        codes.add(test_code)
    return codes

@app.get("/health")
def health():
    return jsonify(status="ok", service="ramn-ipa")

@app.post("/verify")
def verify():
    payload = request.get_json(silent=True) or {}
    code = str(payload.get("code", "")).strip().upper()
    if not code or code not in valid_codes():
        return jsonify(ok=False, message="Invalid access code."), 401
    download_url = os.getenv("DOWNLOAD_URL", "").strip()
    if not download_url:
        return jsonify(ok=True, downloadReady=False), 200
    if not download_url.startswith("https://"):
        return jsonify(ok=False, message="Download is not configured securely."), 503
    return jsonify(ok=True, downloadReady=True, downloadUrl=download_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "10000")))
