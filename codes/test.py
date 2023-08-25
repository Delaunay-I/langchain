# from langchain.llms import OpenAI

# llm = OpenAI(model="text-davinci-003", temperature=0.9)

# text = "Suggest a personalized workout routine for someone looking to improve cardiovascular endurance and prefers outdoor activities."
# print(llm(text))


import openai

try:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Hello, world!",
        max_tokens=5
    )
    print("API Key is valid.")
except openai.error.OpenAIError:
    print("API Key is not valid.")
