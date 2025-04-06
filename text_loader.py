from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables")

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro', api_key=google_api_key)

loader = TextLoader("data/sample.txt",encoding="utf-8")

# Load the documents
docs = loader.load()


prompt = PromptTemplate(
    template='Write a summary about following biography - \n {sample}',
    input_variables=['sample']
)

parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({'sample': docs[0].page_content}))




# print(docs)
# print(type(docs))

# print(docs[0].page_content)
# print(docs[0].metadata)

# print(len(docs))
# print(docs[0])
# print(type(docs[0]))