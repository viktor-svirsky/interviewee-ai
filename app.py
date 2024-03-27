from dotenv import load_dotenv

from src.file import CSVFile, JSONFile
from src.ai import OpenAIChatBot

if __name__ == "__main__":
    load_dotenv()

    prompt_file = JSONFile("prompt.json")
    result_file = CSVFile("result.csv")
    chatbot = OpenAIChatBot()

    prompts = prompt_file.read()
    for question in prompts["questions"]:
        result_file.write(
            [question, chatbot.get_answer(question, prompts["domain_context"])]
        )
