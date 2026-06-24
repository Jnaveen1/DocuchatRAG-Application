from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY

def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY
    )