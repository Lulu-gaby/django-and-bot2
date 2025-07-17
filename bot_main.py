from telebot.types import Message
import telebot
import requests


API_URL = 'http://127.0.0.1:8000/api'
BOT_TOKEN = '7530834954:AAF8lbHwo9eLR02TCsTryyAbA3RUQtNKgUs'

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start'])
def start_command(message: Message):
    data = {
        'user_id': message.from_user.id,
        'username':message.from_user.username
    }
    response = requests.post(API_URL + '/register/', json=data)
    if response.status_code == 200:
        if response.json().get('message'):
            bot.send_message(message.chat.id, 'Вы уже были зарегистрированы ранее!')
        else:
            bot.send_message(message.chat.id, f"Вы успешно зарегистрированы! Ваш уникальный номер: {response.json()['id']}")


if __name__=='__main__':
    bot.polling(non_stop=True)