import os

from openai import OpenAI


class OpenAIChatBot:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_MODEL")
        self.client = OpenAI()

    def get_answer(self, question, domain_context):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"{domain_context}\nQ: {question}\nA:",
                }
            ],
        )
        answer = response.choices[0].message.content
        return answer
