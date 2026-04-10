from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.messages import SystemMessage, HumanMessage


loader = PyPDFLoader("./story.pdf", mode="single")

docs = loader.load()

story = docs[0].page_content

model = ChatGoogleGenerativeAI(model="models/gemini-flash-latest")

response = model.invoke(
    [
        SystemMessage("<story>" + story + "</story>"),
        HumanMessage("What is the chapter 1 of arav story ?"),
    ]
)

print(response.text)