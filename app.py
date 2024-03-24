import os
import json
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

OpenAI.api_key = os.getenv("OPENAI_API_KEY")
openai_model = os.getenv("OPENAI_MODEL")

client = OpenAI()


def get_answer(question, domain_context):
    response = client.chat.completions.create(
        model=openai_model,
        messages=[
            {
                "role": "user",
                "content": f"{domain_context}\nQ: {question}\nA:",
            }
        ],
    )
    answer = response.choices[0].message.content
    return answer


with open("prompt.json") as prompt_file:
    file_contents = prompt_file.read()
prompt_json = json.loads(file_contents)
domain_context = prompt_json["domain_context"]
questions = prompt_json["questions"]

for question in questions:
    print(f"Question: {question}")
    answer = get_answer(question, domain_context)
    print(f"Answer: {answer}\n\n")
