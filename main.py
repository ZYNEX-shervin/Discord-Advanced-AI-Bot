import discord
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# --- CONFIG ---
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# --- CHARACTER PROFILE ---
CHAR_NAME = "YourBotName"
CHAR_DETAILS = """
- Age: 24
- Origin: Forged in the depths of a digital storm...
...
"""
SYSTEM_PROMPT = f"""
You are roleplaying as {CHAR_NAME}.
{CHAR_DETAILS}

IMPORTANT RULES:
1. Stay in character. You are NOT an AI.
2. Keep replies SHORT (1-2 sentences). Speak in the defined Writing Style.
3. Keep conversation PG-13 and safe.
"""

print(f"--- STARTING BOT: {CHAR_NAME} ---")

client_ai = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=GROQ_API_KEY)
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
chat_history = []

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        chat_history.append({"role": "user", "content": message.content})
        if len(chat_history) > 15:
            chat_history.pop(0)

        payload = [{"role": "system", "content": SYSTEM_PROMPT}] + chat_history
        response = client_ai.chat.completions.create(model="llama-3.1-8b-instant", messages=payload)
        reply = response.choices[0].message.content

        chat_history.append({"role": "assistant", "content": reply})
        await message.channel.send(reply)
    except Exception as e:
        print(f"Error: {e}")

client.run(DISCORD_TOKEN)
