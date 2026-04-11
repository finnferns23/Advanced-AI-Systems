from config import MODEL_NAME, TEMPERATURE
from openai import OpenAI

client = OpenAI()

def generate_idea(prompt: str):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE
    )
    return response.choices[0].message.content.strip()
