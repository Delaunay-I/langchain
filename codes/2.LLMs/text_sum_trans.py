from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# summarization_template = "Summarize the following text to one sentence: {text}"
# summarization_prompt = PromptTemplate(input_variables=["text"], template=summarization_template)
# summarization_chain = LLMChain(llm=llm, prompt=summarization_prompt)

# text = "LangChain provides many modules that can be used to build language model applications. Modules can be combined to create more complex applications, or be used individually for simple applications. The most basic building block of LangChain is calling an LLM on some input. Let’s walk through a simple example of how to do this. For this purpose, let’s pretend we are building a service that generates a company name based on what the company makes."
# summarized_text = summarization_chain.predict(text=text)
# print(summarized_text)

translation_template = "Translate the following text from {source_language} to {target_language}: {text}"
translation_prompt = PromptTemplate(input_variables=["source_language", "target_language", "text"], template=translation_template)
translation_chain = LLMChain(llm=llm, prompt=translation_prompt)

source_language = "English"
target_language = "Farsi"
text = "I am having fun here, and living a good life. Everything is good."
translated_text = translation_chain.predict(source_language=source_language, target_language=target_language, text=text)
print(translated_text)