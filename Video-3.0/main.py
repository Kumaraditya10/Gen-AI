from dotenv import load_dotenv

load_dotenv()
import os


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader("./story.pdf")

docs = loader.load()


embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", 
)

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("py-index")

vector_store = PineconeVectorStore(embedding=embeddings, index=index)


print(vector_store.similarity_search(query="debugging",k=1))