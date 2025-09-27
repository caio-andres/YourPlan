from openai import OpenAI
from src.environment.openai import api_key

client = OpenAI(api_key=api_key)
