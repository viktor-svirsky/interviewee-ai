import os
import csv
import json
from openai import OpenAI
from dotenv import load_dotenv


class OpenAIChatBot:
    def __init__(self):
        load_dotenv()
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

    def load_prompt(self, filename):
        with open(filename) as prompt_file:
            file_contents = prompt_file.read()
        prompt_json = json.loads(file_contents)
        domain_context = prompt_json["domain_context"]
        questions = prompt_json["questions"]
        return domain_context, questions

    def result_to_csv(self, questions, answers, filename):
        with open(filename, mode="w") as result_file:
            result_writer = csv.writer(result_file, delimiter=",")
            result_writer.writerow(["Question", "Answer"])
            for question in questions:
                result_writer.writerow([question, answers[question]])


if __name__ == "__main__":
    chatbot = OpenAIChatBot()
    domain_context, questions = chatbot.load_prompt("prompt.json")
    result = {}
    for question in questions:
        result[question] = chatbot.get_answer(question, domain_context)
    chatbot.result_to_csv(questions, result, "result.csv")
