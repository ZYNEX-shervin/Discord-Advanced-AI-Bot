# Discord_Advanced_AI_Bot – Character AI Discord Bot

A fully customizable roleplay-based Discord bot powered by Groq API.

Hosted 24/7 using FPS.ms Discord Bot Hosting (Python).

---

# 🌌 Features

- 🎭 Custom Character Personality
- 🧠 Powered by llama-3.1-8b-instant (Groq API)
- 💬 Short In-Character Replies (1–2 sentences)
- 🛡 PG-13 Safe Mode
- 🧾 Rolling Memory (last 15 messages)
- ⚡ Lightweight & Beginner Friendly
- ☁ 24/7 Hosting via FPS.ms Panel

---

# 📁 Project Files

```
main.py
requirements.txt
README.md
```

---

# ⚙ Requirements

- Python 3.11 (handled automatically by FPS)
- Discord Bot Token
- Groq API Key

---

# 🛒 Deploy Using FPS.ms (Panel Method Only)

This guide uses:

FPS.ms → Discord → Bot Hosting (Python)

No SSH required.

---

## 🟢 Step 1 — Purchase Hosting

1. Go to:
   https://panel.fps.ms/deploy/discord-bot
2. Select:
   Discord → Bot Hosting (Python)
3. Complete payment.
4. Wait for server creation.

You will now see your server inside the panel dashboard.

---

## 🟢 Step 2 — Upload Bot Files

1. Open your server (example: Habibi_Gamerz)
2. Click **Files**
3. Upload:
   - main.py
   - requirements.txt

Make sure filenames are EXACT:

main.py  
requirements.txt  

No extra .txt at the end.

---

## 🟢 Step 3 — Configure Startup Settings

Go to:

Startup

Set the following:

| Setting | Value |
|----------|--------|
| App py file | main.py |
| Requirements file | requirements.txt |
| User Uploaded Files | 1 |
| Auto Update | 0 |
| Git Repo Address | (leave empty) |
| Git Branch | (leave empty) |
| Additional Python packages | (leave empty) |
| Docker Image | Python 3.11 |

⚠ IMPORTANT:
User Uploaded Files must be set to 1

Do NOT edit the long startup command.
Leave it as default.

---

## 🟢 Step 4 — Add Your Tokens

Open main.py inside Files.

Replace:

```python
DISCORD_TOKEN = "YOUR DISCORD-BOT-TOKEN"
GROQ_API_KEY = "YOUR GROQ_API_KEY"
```

With your real keys.

Click Save.

---

## 🟢 Step 5 — Start the Bot

1. Go to Console
2. Click Start

If everything is correct, you will see:

```
--- STARTING BOT: YourBotName ---
Logged in as YourBotName
```

Your bot is now online 24/7 🎉

---

# 🎮 Creating the Discord Bot

1. Go to the Discord Developer Portal
2. Create New Application
3. Go to Bot → Add Bot
4. Copy the Bot Token
5. Enable:
   MESSAGE CONTENT INTENT

Invite bot to your server using OAuth2 URL Generator.

---

# 🔐 Getting Groq API Key

1. Create account at Groq
2. Generate API Key
3. Paste into main.py

---

# 🧠 How the Bot Works

1. User sends a message.
2. Bot adds message to chat history.
3. System prompt defines character personality.
4. Conversation sent to Groq API.
5. Model generates short in-character reply.
6. Bot sends response to Discord.

Chat history is limited to 15 messages to prevent overload.

---

# 📦 requirements.txt

```
discord.py
openai
```

---

# 🛡 Security Tips

- Never share Discord token.
- Never share Groq API key.
- If leaked → regenerate immediately.
- Consider using environment variables for production.

---

# ❌ Troubleshooting

Bot not starting?

Check:
- main.py filename correct
- requirements.txt exists
- User Uploaded Files = 1
- Tokens are correct
- Message Content Intent enabled

Invalid Token?

Regenerate in Discord Developer Portal.

Module Not Found?

Make sure requirements.txt contains:

discord.py  
openai  

Restart server.

---

# 🌍 Why FPS.ms?

| Feature | FPS Panel |
|----------|------------|
| 24/7 uptime | ✅ |
| No SSH required | ✅ |
| Beginner friendly | ✅ |
| Automatic Python install | ✅ |
| Docker-based | ✅ |

---

# 🎭 Customizing Character

Inside main.py edit:

- CHAR_NAME
- CHAR_DETAILS
- Writing Style
- Personality
- Likes & Dislikes

You can create:
- A wizard
- A villain AI
- A guardian spirit
- A sarcastic robot
- Anything you imagine

---

# 📜 License

Free for personal and educational use.

Do not use for:
- Spam
- Harassment
- Discord ToS violations
- Illegal automation

---

# ⭐ If You Like This Project

Give it a star and expand it with:

- Slash Commands
- Persistent Memory (SQLite)
- Admin Commands
- Personality Switching
- Web Dashboard
- Voice Integration

---

Powered by:
Discord API  
Groq OpenAI-Compatible Endpoint  
Hosted on FPS.ms  

---
