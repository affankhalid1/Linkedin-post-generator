from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))


if __name__== "__main__":
    response = llm.invoke("Tell me what is the is the Super Artificial Intelligence")
    print(response.content)