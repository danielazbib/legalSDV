import re
import json
import pandas as pd
from sdv.metadata import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer


# Load JSON data
def load_data(file):
    with open(file, "r") as file:
        data = json.load(file)
    return data

# Function to split company names and filter for identifiable patterns
def extract_and_filter_company_name(name):
    match = re.match(r"(.+?)\b(Inc\.|LLC|Ltd\.|Corp\.|Co\.)$", name.strip())
    if match:
        # Return the base name and suffix if matched
        return match.group(1).strip(), match.group(2)
    return None, None  # Return None if the pattern doesn't match

def extract_original_descriptions(data):
    contexts = []
    for case in data['data']:
        if 'paragraphs' in case and len(case['paragraphs']) > 0:
            context = case['paragraphs'][0].get('context', '')
            contexts.append(context)
    return contexts

def extract_private_keywords(data):
    keywords = []
    for case in data['data']:
        case_keywords = []  # Initialize a sub-array for each case
        if 'paragraphs' in case and len(case['paragraphs']) > 0:
            # Access the second 'qas' entry (index 1) in paragraphs[0]
            qas_section = case['paragraphs'][0].get('qas', [])
            if len(qas_section) > 1:
                these_keywords = qas_section[1].get('answers', [])
                # Extract keywords (text) from answers and add to case_keywords
                for answer in these_keywords:
                    keyword_text = answer.get('text', '')
                    if keyword_text:  # Check if text is not empty
                        case_keywords.append(keyword_text)
        keywords.append(case_keywords)  # Append each case's keywords array to the main array
    return keywords

def replace_keywords_with_placeholder(descriptions, keywords, placeholder="ABC Constituent"):
    modified_descriptions = []
    
    for i in range(len(descriptions)):
        description = descriptions[i]
        case_keywords = keywords[i]
        
        # Replace each keyword in the current description with the placeholder
        for keyword in case_keywords:
            description = description.replace(keyword, placeholder)
        
        # Append the modified description to the result list
        modified_descriptions.append(description)
    
    return modified_descriptions

def main():
    data = load_data('./data/CUADv1.json')
    original_descriptions = extract_original_descriptions(data)
    keywords = extract_private_keywords(data)
    modified_descriptions = replace_keywords_with_placeholder(original_descriptions, keywords)
    
    print(modified_descriptions[0])
    print(original_descriptions[0])

if __name__ == "__main__":
    main()
