from . import prompts
import openai
import os
from dotenv import load_dotenv

load_dotenv('./.env')
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
def generate_questions_ai(title: str, tags: str, count, complexity):
    
    prompt = prompts.get_prompt_for_questions(title, tags, n_questions=count, complexity=complexity)
    
    client = openai.OpenAI(
    api_key='sk-SwDj282n2Anwwu96iaisTDxPUf1n15hG',
    base_url="https://api.proxyapi.ru/openai/v1"
    )
    messages=[
                {"role": "user", "content": str(prompt)}
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1000,
        temperature=0.7
    )
    
    ans = response.choices[0].message.content.split("\n")
    return ans
