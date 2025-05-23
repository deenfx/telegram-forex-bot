import os
import requests
from flask import Flask, request

app = Flask(__name__)

# Get your Telegram bot token and chat ID from environment variables
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Function to send message to Telegram
def send_signal(message):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=data)

# 🚨 This is the webhook endpoint route — paste it here
@app.route('/signal', methods=['POST'])
def signal():
    data = request.json
    msg = f"📊 New Signal:\nPair: {data['pair']}\nAction: {data['action']}\nPrice: {data['price']}"
    send_signal(msg)
    return 'Signal sent', 200

# Optional: only needed if testing locally
if __name__ == '__main__':
    app.run()
