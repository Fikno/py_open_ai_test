import os
import openai
import json
import time
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

# Reading API key from environment variables and setting it
API_KEY = os.getenv("OPENAI_API_KEY")


client = openai.OpenAI()

def show_json(obj):
    print(json.loads(obj.model_dump_json()))

