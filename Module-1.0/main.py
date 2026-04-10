from google import genai
from dotenv import load_dotenv
import os   


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
message =   []

while True:

    user_input = input("Enter your message: ")
    
    message.append(
        {
            "role": "user",
            "content": list(map(lambda message: message["role"] + " : " + message["content"], message)) 
        }
    )

    responce = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = user_input
    )
    
    message.append(
        {
            "role": "ai",
            "content": responce.text
        }
    )
    print(responce.text)