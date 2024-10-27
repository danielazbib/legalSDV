import re
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load JSON data
def load_data(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data

# Extract titles
def extract_titles(data):
    titles = []
    for case in data["data"]:
        if "title" in case:
            titles.append(case["title"])
    return titles

# Extract original descriptions
def extract_original_descriptions(data):
    contexts = []
    for case in data['data']:
        if 'paragraphs' in case and len(case['paragraphs']) > 0:
            context = case['paragraphs'][0].get('context', '')
            contexts.append(context)
    return contexts

# Extract private keywords
def extract_private_keywords(data):
    keywords = []
    for case in data["data"]:
        case_keywords = []
        if "paragraphs" in case and len(case["paragraphs"]) > 0:
            qas_section = case["paragraphs"][0].get("qas", [])
            if len(qas_section) > 1:
                these_keywords = qas_section[1].get("answers", [])
                for answer in these_keywords:
                    keyword_text = answer.get("text", "")
                    if keyword_text:
                        case_keywords.append(keyword_text)
        keywords.append(case_keywords)
    return keywords

# Replace keywords in descriptions
def replace_keywords_with_placeholder(descriptions, keywords, placeholder="ABC Constituent"):
    modified_descriptions = []
    for i in range(len(descriptions)):
        description = descriptions[i]
        case_keywords = keywords[i]
        for keyword in case_keywords:
            description = description.replace(keyword, placeholder)
        modified_descriptions.append(description)
    return modified_descriptions

# Calculate similarity scores
def calculate_similarity(original_descriptions, modified_descriptions):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    similarities = []
    
    for original, modified in zip(original_descriptions, modified_descriptions):
        original_embedding = model.encode([original])
        modified_embedding = model.encode([modified])
        similarity_score = cosine_similarity(original_embedding, modified_embedding)[0][0]
        similarities.append(similarity_score)
    
    similarities = [float(score) for score in similarities]
    avg_similarity = float(sum(similarities) / len(similarities)) if similarities else 0
    return similarities, avg_similarity

# Main function to process data
def process_data(file_path):
    data = load_data(file_path)
    titles = extract_titles(data)
    original_descriptions = extract_original_descriptions(data)
    keywords = extract_private_keywords(data)
    modified_descriptions = replace_keywords_with_placeholder(original_descriptions, keywords)
    similarities, avg_similarity = calculate_similarity(original_descriptions, modified_descriptions)
    
    return titles, original_descriptions, modified_descriptions, similarities, avg_similarity
