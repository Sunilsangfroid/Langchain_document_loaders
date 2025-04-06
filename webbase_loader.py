from langchain_community.document_loaders import WebBaseLoader
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

prompt = PromptTemplate(
    template='Answer the following question- \n {question} from the following text - \n {sample}',
    input_variables=['question', 'sample']
)

parser = StrOutputParser()

url = "https://www.amazon.in/s?k=apple+iphone&adgrpid=1326012628879468&hvadid=82876058711374&hvbmt=bp&hvdev=c&hvlocphy=144046&hvnetw=o&hvqmt=p&hvtargid=kwd-82876675613104%3Aloc-90&hydadcr=25231_2783807&mcid=30e31fc7fa5e3d759866a4f1a2b3021c&msclkid=016a3d8aa70a1df0888d5a7b7eda515d&tag=msndeskstdin-21&ref=pd_sl_3rta2jmxxv_p"
loader = WebBaseLoader(url)

docs = loader.load()

# print(len(docs))
# print(docs[0].page_content)

chain = prompt | model | parser

print(chain.invoke({'question': 'What is the price of iPhone 14 ?', 'sample': docs[0].page_content}))