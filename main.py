from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import (
    ConversationBufferMemory,
    ConversationSummaryMemory,
    FileChatMessageHistory,
)
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

load_dotenv()

chat = ChatOpenAI(verbose=True)

# memory = ConversationBufferMemory(
#     memory_key="messages",
#     return_messages=True,
#     chat_memory=FileChatMessageHistory("messages.json"),
# )

memory = ConversationSummaryMemory(
    memory_key="messages",
    return_messages=True,
    llm=chat,
)

prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)

chain = LLMChain(llm=chat, prompt=prompt, memory=memory, verbose=True)

while True:
    try:
        content = input(">> ")
        result = chain({"content": content})

        print(result["text"])
    except Exception as e:
        print(e)
