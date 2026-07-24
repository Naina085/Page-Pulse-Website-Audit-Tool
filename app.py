from flask import Flask, render_template, request, jsonify
from analyzer import analyze_website

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # Get JSON data from frontend
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data received"}), 400

        url = data.get("url", "").strip()

        if not url:
            return jsonify({"error": "URL is required"}), 400

        # Debug prints (remove later if you want)
        print("=" * 50)
        print("Received URL:", url)

        result = analyze_website(url)

        print("Analysis Result:", result)
        print("=" * 50)

        return jsonify(result)

    except Exception as e:
        print("ERROR:", str(e))

        return jsonify({
            "status": "Error",
            "response_time": "--",
            "title": "No Title",
            "meta": "Not Found",
            "h1_count": 0,
            "missing_alt": 0,
            "word_count": 0,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)