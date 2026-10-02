from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class UserInput(BaseModel):
    message: str

@app.post("/chat")
def chat(input: UserInput):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""
Explain the topic: {input.message}

Give output in this format:

📘 Explanation:
(simple explanation)

😂 Meme:
(short funny line)

📝 Exam Definition:
(1 line)
"""
    )

    return {"reply": response.text}