import requests
import json

def create_chat_completion(messages, model="whatever", node="localhost", node_port=5000, temperature=1.0, max_tokens=1024)->str:
    data = {
        'messages': messages,
        'temperature': temperature,
        'max_tokens': max_tokens,
    }

    response = requests.post(f"http://{node}:{node_port}/ask_llm", json=data)
    response_json = response.json()

    return response_json['response']
