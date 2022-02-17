import telebot
from flask import Flask, request
import os


TOKEN = '5156487975:AAEA4IaC4ivT_08mMjame_ryhOM9-AngDpI'
APP_URL = f'https://heroku123-test-app.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, 'Hello!')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    
    return '!', 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)

    return '!', 200

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))