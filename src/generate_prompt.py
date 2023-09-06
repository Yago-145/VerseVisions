import requests
import spacy
import os
import json

def extract_keywords(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    keywords = [token.lemma_.lower() for token in doc if token.pos_ in ("NOUN", "PROPN", "ADJ", "VERB")]

    return keywords

def generate_prompt(prompt):
    api_key = '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'
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    system_message = {
        "role": "system",
        "content": """You are an AI model that generates descriptions of images. 
                    You are given a song lyrics as a prompt, and you have to generate 
                    a description of the image that the lyrics describe. In case security 
                    filters are enabled, you have to generate a description that passes 
                    the filters. In case you don't know what to do, you might want to 
                    try to generate a description of the image that the lyrics describe, 
                    either by describing the image or by describing the lyrics in any way you can. 
                    If you are not sure what to do or the lyrics provide no information about any scene, 
                    improvise something related with the lyrics."""
    }
    
    user_message = {
        "role": "user",
        "content": prompt
    }

    messages = [system_message, user_message]

    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "max_tokens": 1000,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        data=json.dumps(data)
    )

    response_json = response.json()
    description = response_json['choices'][0]['message']['content'].strip()

    return description
