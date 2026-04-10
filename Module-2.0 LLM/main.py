from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai.chat_models import ChatMistralAIChat

model = ChatMistralAIChathatMi(model="mistral-small-latest")

responce = model.invoke("Hello")

print(responce.text)