from flask import Flask, request, redirect, jsonify
import string
import random

app = Flask(__name__)

# In-memory storage (for demo; in real-world use DB)
url_map = {}

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def home():
    return "URL Shortener Running 🚀"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    long_url = data["url"]

    short_code = generate_short_code()
    url_map[short_code] = long_url

    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 201

@app.route('/<code>')
def redirect_url(code):
    long_url = url_map.get(code)

    if long_url:
        return redirect(long_url)

    return jsonify({"error": "URL not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
