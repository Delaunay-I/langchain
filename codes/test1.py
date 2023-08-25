from langchain.llms import GPT4All
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

template = """What is a good name for a company that makes {product}?

Answer:"""

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
llm = GPT4All(model="./models/ggml-model-q4_0.bin", callback_manager=callback_manager, verbose=True)
# prompt = PromptTemplate(
#     input_variables=["product"],
#     template=template,
# )

# chain = LLMChain(prompt=prompt, llm=llm)

# chain.run("eco-friendly water bottles")

conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)

conversation.predict(input="Tell me about yourself.")
# Continue the conversation
conversation.predict(input="What can you do?")
conversation.predict(input="How can you help me with data analysis?")

# Display the conversation
print(conversation)