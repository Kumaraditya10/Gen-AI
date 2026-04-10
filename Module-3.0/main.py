from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAI
from langchain.tools import tool
from langchain.messages import HumanMessage, ToolMessage
from datetime import date

@tool
def getCurrentDate():
    """Use this tool to get the current date."""
    return str(date.today())

model = ChatMistralAI(model="mistral-small").bind_tools([getCurrentDate])

responce = model.invoke("today's date?")

tool_result = getCurrentDate.invoke(responce.tool_calls[0],["args"])

second_responce = model.invoke([
    HumanMessage("today's date?"),
    ToolMessage(tool.result)
    ])

print(second_responce.text)