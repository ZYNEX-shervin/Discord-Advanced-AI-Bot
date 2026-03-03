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
.env
README.md
```

---

# ⚙ Requirements

- Python 3.11 (handled automatically by FPS)  
- Discord Bot Token  
- Groq API Key  
- `python-dotenv` package (included in requirements)  

---

# 🔐 Using `.env` for Security

Create a file called `.env` in your project folder:

```
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

> Replace with your actual keys.  

Update `.gitignore` to prevent committing `.env`:

```
# Secrets
.env
```

This ensures your tokens **never get uploaded to GitHub**.

---

# 🛒 Deploy Using FPS.ms (Panel Method Only)

No SSH or Git required.  

FPS.ms → Discord → Bot Hosting (Python)

---

## 🟢 Step 1 — Purchase Hosting

1. Go to:  
   https://panel.fps.ms/deploy/discord-bot  
2. Select: Discord → Bot Hosting (Python)  
3. Complete payment  
4. Wait for server creation  

---

## 🟢 Step 2 — Upload Bot Files

1. Open your server   
2. Click **Files**  
3. Upload:  
   - main.py  
   - requirements.txt  
   - .env  

⚠ Filenames must match exactly.  

---

## 🟢 Step 3 — Configure Startup Settings

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

> User Uploaded Files **must be 1**  
> Leave startup command as default  

---

## 🟢 Step 4 — Start the Bot

1. Go to **Console**  
2. Click **Start**  

Expected output:

```
--- STARTING BOT: YourBotName ---
Logged in as YourBotName
```

---

# 🎮 Creating the Discord Bot

1. Go to the Discord Developer Portal  
2. Create New Application  
3. Add a Bot  
4. Copy the Bot Token  
5. Enable **Message Content Intent**  
6. Invite bot to your server using OAuth2 URL Generator  

---

# 🔐 Getting Groq API Key

1. Create an account at Groq  
2. Generate API Key  
3. Paste into `.env`  

---

# 🧠 How the Bot Works

1. User sends a message  
2. Bot adds message to chat history (last 15)  
3. System prompt defines character personality  
4. Conversation sent to Groq API  
5. Model generates short in-character reply  
6. Bot sends response to Discord  

---

# 📦 requirements.txt

```
discord.py
openai
python-dotenv
```

---

# 🛡 Security Tips

- Never commit `.env` to GitHub  
- Never share Discord token or Groq API key  
- Regenerate keys immediately if leaked  
- Consider using `.env` for any future secrets  

---

# ❌ Troubleshooting

- Bot not starting? Check:  
  - main.py filename correct  
  - requirements.txt exists  
  - .env exists with correct keys  
  - User Uploaded Files = 1  
  - Message Content Intent enabled  

- Module Not Found? Ensure `requirements.txt` includes:  

```
discord.py
openai
python-dotenv
```

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

Edit `main.py`:

- CHAR_NAME  
- CHAR_DETAILS  
- Writing Style  
- Personality  
- Likes & Dislikes  

Create any type of AI roleplay bot you imagine.

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

Give it a star and expand with:

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
