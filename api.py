from flask import Blueprint, request, jsonify
import requests

api = Blueprint('api', __name__)

@api.route('/categorize', methods=['POST'])
def categorize_entry():
    data = request.get_json()
    description = data.get('description')
    if not description:
        return jsonify({"error": "Missing description"}), 400

    # Prepare prompt
    prompt = f"Classify the following entry into one of these categories: Acts of Service, Quality Time, Receiving Gifts, Words of Affirmation, Physical Touch. Only reply with the category name. Entry: '{description}'"

    ollama_payload = {
        "model": "qwen3:14b",
        "prompt": prompt
    }

    ollama_url = "http://192.168.50.201:11434/api/generate"
    try:
        ollama_response = requests.post(ollama_url, json=ollama_payload, timeout=10)
        ollama_response.raise_for_status()
        result = ollama_response.json()
        category = result.get('response', '').strip()
    except Exception as e:
        return jsonify({"error": f"Ollama error: {str(e)}"}), 500

    return jsonify({"category": category})