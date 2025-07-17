from flask import Blueprint, json, request, jsonify
import requests
import os

PROMPT_FILE = os.path.join(os.path.dirname(__file__), 'prompts', 'category_prompt.txt')

api = Blueprint('api', __name__)

def load_prompt():
    with open(PROMPT_FILE, 'r') as f:
        return f.read()

@api.route('/categorize', methods=['POST'])
def categorize_entry():
    print("API endpoint hit!")
    data = request.get_json()
    description = data.get('description')
    if not description:
        return jsonify({"error": "Missing description"}), 400

    # Prepare prompt
    prompt = load_prompt().format(entry=description)
    ollama_payload = {
        "model": "llama3:latest",
        "prompt": prompt,
        "stream": False
    }

    ollama_url = "http://192.168.50.201:11434/api/generate"
    try:
        ollama_response = requests.post(ollama_url, json=ollama_payload, timeout=10)
        ollama_response.raise_for_status()
        ollama_json = ollama_response.json()
        response_str = ollama_json.get("response", "")

        # Parse the string in "response" into a dict
        import json
        category_data = {}
        if response_str.strip().startswith("{"):
            try:
                category_data = json.loads(response_str)
            except Exception as e:
                print(f"Error parsing Ollama response JSON: {e}")
                return jsonify({"error": "Invalid response from model"}), 500

        category = category_data.get('category', '')
        reasoning = category_data.get('reasoning', '')

        print(f"Category: {category}, Reasoning: {reasoning}")

    except requests.RequestException as e:
        print(f"Error calling Ollama API: {e}")
        return jsonify({"error": "Failed to categorize entry"}), 500

    return jsonify({"category": category, "reasoning": reasoning}), 200