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

# Extract original descriptions from context
def extract_original_descriptions(data):
    contexts = []
    for case in data['data']:
        if 'paragraphs' in case and len(case['paragraphs']) > 0:
            context = case['paragraphs'][0].get('context', '')
            contexts.append(context)
    return contexts

# Extract private keywords (company names) from specific indices in 'qas' section
def extract_private_keywords(data):
    keywords = []
    for case in data['data']:
        case_keywords = []
        if 'paragraphs' in case and len(case['paragraphs']) > 0:
            qas_section = case['paragraphs'][0].get('qas', [])
            if len(qas_section) > 1:
                these_keywords = qas_section[1].get('answers', [])
                for answer in these_keywords:
                    keyword_text = answer.get('text', '')
                    if keyword_text:
                        case_keywords.append(keyword_text)
        keywords.append(case_keywords)
    return keywords

# Generate synthetic company names with SDV
def generate_synthetic_company_names(keywords):
    # Flatten the keywords list to use for SDV
    flattened_keywords = [kw for case_keywords in keywords for kw in case_keywords if kw]

    # Prepare DataFrame for SDV
    keywords_df = pd.DataFrame(flattened_keywords, columns=['company_name'])

    # Define metadata and initialize SDV synthesizer
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(keywords_df)
    metadata.update_column('company_name', sdtype='text')

    synthesizer = CTGANSynthesizer(metadata)
    synthesizer.fit(keywords_df)

    # Generate synthetic company names
    synthetic_keywords_df = synthesizer.sample(num_rows=len(flattened_keywords))

    # Reformat synthetic names into original array-of-arrays structure
    synthetic_keywords = []
    index = 0
    for case_keywords in keywords:
        case_synthetic_names = []
        for _ in case_keywords:
            if index < len(synthetic_keywords_df):
                case_synthetic_names.append(synthetic_keywords_df.iloc[index]['company_name'])
                index += 1
        synthetic_keywords.append(case_synthetic_names)
    
    return synthetic_keywords

# Replace each keyword in descriptions with the corresponding synthetic company name
def replace_keywords_with_synthetic_names(descriptions, keywords, synthetic_names):
    modified_descriptions = []
    
    for i in range(len(descriptions)):
        description = descriptions[i]
        case_keywords = keywords[i]
        case_synthetic_names = synthetic_names[i]
        
        # Replace each keyword with the corresponding synthetic name
        for original, synthetic in zip(case_keywords, case_synthetic_names):
            description = re.sub(rf"\b{re.escape(original)}\b", synthetic, description)
        
        modified_descriptions.append(description)
    
    return modified_descriptions

# Main function
def main():
    data = load_data('/Users/danielazbib/legalSDV/backend/data/CUADv1.json')
    original_descriptions = extract_original_descriptions(data)
    keywords = extract_private_keywords(data)
    synthetic_names = generate_synthetic_company_names(keywords)
    modified_descriptions = replace_keywords_with_synthetic_names(original_descriptions, keywords, synthetic_names)

    # Output original vs. modified for verification
    print("Original:", original_descriptions)
    print("Modified:", modified_descriptions)

if __name__ == "__main__":
    main()
