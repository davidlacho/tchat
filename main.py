from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.llms import OpenAI

prompt = ChatPromptTemplate(
  input_variables=["content"],
  messages=[
    HumanMessagePromptTemplate.from_template("{content}"),
  ]
)



while True:
  content = input(">> ")  
