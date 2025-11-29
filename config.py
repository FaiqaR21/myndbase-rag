import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# This must NOT come from .env
BASE_URL = "https://openrouter.ai/api/v1"
