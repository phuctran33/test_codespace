from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator

app = Flask(__name__)
CORS(app)  # Cho phép mọi domain gọi vào API

translator = Translator()

@app.post("/translate")
def translate_text():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Missing text"}), 400

    try:
        result = translator.translate(text, src="en", dest="vi")
        return jsonify({"translated": result.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5501)
