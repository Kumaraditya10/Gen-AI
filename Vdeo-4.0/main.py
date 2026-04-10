from dotenv import load_dotenv

load_dotenv()
import os


from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage



embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", 
)

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("py-index")

vector_store = PineconeVectorStore(embedding=embeddings, index=index)


@tool
def getContext(query:str):
    """Use this tool for get more information for fulfilling the user demand

    provide the query parameter for what you are looking for.
    """
    
    result = vector_store.similarity_search(query=query,k=2)
    
    return str(result)


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(model=model,tools=[getContext])


response = agent.invoke({
    "messages":[HumanMessage("what was the first chapter of the ARAV story ? and summarise it")]
})

print(response["messages"][-1].text)