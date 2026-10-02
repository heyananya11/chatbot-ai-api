import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

print("🤖 AI Chatbot Started (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye 👋")
        break

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"""
Explain the topic: {user_input}

Give output in this format:

📘 Explanation:
(simple explanation in easy words)

😂 Meme:
(short funny relatable line)

📝 Exam Definition:
(1 line formal definition)

Keep it clean and structured.
"""
    )

    print("\nAI:\n", response.text, "\n")