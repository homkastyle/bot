import requests

def send_telegram_message(message):
    """Отправка сообщения в Telegram."""
    bot_token = 'your_telegram_bot_token'
    chat_id = 'your_chat_id'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)
