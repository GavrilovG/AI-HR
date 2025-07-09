
import openai


openai_api_key = 'sk-SwDj282n2Anwwu96iaisTDxPUf1n15hG'
url = "https://api.proxyapi.ru/openai/v1"

def get_responce(
    prompt:str
):
    client = openai.OpenAI(
    api_key=openai_api_key,
    base_url=url
    )
    messages=[
                {"role": "user", "content": prompt}
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=1000,
        temperature=0.7
    )
    ans = response.choices[0].message.content
    return ans

def generate_questions_ai(title: str, tags: str):
    prompt = (f"Ты — опытный hr-специалист. Сейчас ты составляешь вопросы для собеседования на вакансию '{title}'. "
        f"Кандидат должен обладать навыками: {tags}. Сгенерируй ровно 15 вопросов. "
        "Вопросы должны быть релевантны вакансии и направлены на оценку как профессиональных навыков, так и soft skills. Выведи просто список из вопросов без пояснений или дополнительных комментариев."
        )
    
    responce = get_responce(prompt)
    return {
        'title': title,
        'tags': tags,
        'questions': responce
    }