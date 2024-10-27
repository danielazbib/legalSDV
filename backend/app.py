# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/similarity")
def get_similarity_data():
    data = {
        "documents": ["Doc 1", "Doc 2", "Doc 3", "Doc 4", "Doc 5"],
        "original_scores": [0.85, 0.78, 0.90, 0.88, 0.82],
        "anonymized_scores": [0.80, 0.75, 0.88, 0.83, 0.81]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
