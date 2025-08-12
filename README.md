# QR Code Generator Telegram Bot 🤖

A simple Telegram bot that lets users create custom QR codes with optional logo images.  
Users can send data, upload a picture, and instantly generate a personalized QR code.

---

## ✨ Features

- `/start` — Displays welcome message and available commands
- `/data your_text_here` — Sets the data to be embedded in the QR code
- Upload a picture — Adds your image/logo to the QR code center
- `/generate` — Generates the QR code (with or without logo)
- `/nopicture` — Removes the previously uploaded logo image

---

## 📦 Requirements

- Python 3.8+
- Telegram Bot API token (from [BotFather](https://core.telegram.org/bots#botfather))

---

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/qr-code-generator-bot.git
   cd qr-code-generator-bot

2. **Install dependencies**
   ``` pip install python-telegram-bot python-dotenv qrcode pillow
3. **Set up environment variables**
    ```Create a .env file in the project root:
    API_BOT=your_telegram_bot_token_here
4. **Run the bot**
   ```python main.py

..**📖 Usage**
Start the bot in Telegram: 
/start
Set data:
/data https://example.com
Upload a logo
(like upload any image in telegram)
Generate QR code:
/generate
Remove logo and use plain QR:
/nopicture

**📂 Project Structure**

.
├── main.py          # Bot entry point
├── functions.py     # Bot command functions
├── .env             # Environment variables
└── README.md        # Project documentation


