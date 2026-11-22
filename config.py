import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_KEY = os.getenv("LLM_API_KEY", "")
    BASE_URL = os.getenv("LLM_BASE_URL", "")
    MODEL = os.getenv("LLM_MODEL", "gpt-3.5-turbo")
