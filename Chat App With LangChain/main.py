from dotenv import load_dotenv
load_dotenv()


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai.chat_models import ChatMistralAI

from langchain.messages import HumanMessage,AIMessage

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model = ChatMistralAI(model="mistral-small-latest")

message = []

while True:
    userInput = input("Enter your prompt:")
    
    message.append(HumanMessage(userInput))
    
    response = model.invoke(message)
    
    message.append(AIMessage(response.content))
    
    print(response.text)