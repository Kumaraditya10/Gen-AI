from dotenv import load_dotenv
load_dotenv()

from tavily import Tavily
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
import os

tavily_client = Tavily.Client(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def surfInternet(query: str):
    """Use this tool for getting the latest information from the internet. """
    
    result = tavily_client.search(query=query)
    
    return str(result.results)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

agent = create_agent(model=model, tools=[surfInternet])

response = agent.invoke(HumanMessage(content="Who is the president of the United States?"))

print(response["message"][-1].text)