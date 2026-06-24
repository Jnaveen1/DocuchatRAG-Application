from langchain.chat_models import init_chat_model
from config import GOOGLE_API_KEY

print("Google API Key:", GOOGLE_API_KEY)

def get_llm():

    model = init_chat_model(
        "google_genai:gemini-2.5-flash",
        api_key=GOOGLE_API_KEY
    )

    return model