import telebot
from flask import Flask
from flask_sslify import SSLify


TOKEN = '5156487975:AAEA4IaC4ivT_08mMjame_ryhOM9-AngDpI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def message_for_me(message):
    bot.send_message(message.chat.id, 'Ты написал /start')

@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling()