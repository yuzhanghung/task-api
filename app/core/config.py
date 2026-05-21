import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
TEST_EMAIL = os.getenv("TEST_EMAIL")