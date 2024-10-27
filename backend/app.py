from flask import Flask, jsonify
from flask_cors import CORS
from context_data import process_data

app = Flask(__name__)
CORS(app)

# Process data and prepare for API response
titles, original_descriptions, modified_descriptions, similarity_scores, avg_similarity = process_data('./data/CUADv1.json')

@app.route("/api/similarity")
def get_similarity_data():
    data = {
        "documents": titles,
        "original_descriptions": original_descriptions,
        "modified_descriptions": modified_descriptions,
        "similarity_scores": similarity_scores,
        "avg_similarity": avg_similarity,
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
