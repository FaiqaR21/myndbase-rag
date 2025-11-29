import requests
from config import OPENROUTER_API_KEY, BASE_URL

def generate_answer(contexts, query):
    prompt = "Use ONLY the context of the user's documents to answer.\n\n"

    for i, ctx in enumerate(contexts):
        prompt += f"Context {i+1}:\n{ctx}\n\n"

    prompt += f"Question: {query}\nAnswer:"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "x-ai/grok-4.1-fast:free",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500
    }

    response = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]

    return f"Error {response.status_code}: {response.text}"
