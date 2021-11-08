from flask import Flask, request
import telebot

secret = "asdas312asdasd"
bot = telebot.TeleBot('2127817624:AAHey_t9W97Q2LvILZ8HThiWR1l9N_iZjLw', threaded=False)
bot.remove_webhook()
bot.set_webhook(url="https://telegrambotshop.pythonanywhere.com/{}".format(secret))

app = Flask(__name__)
@app.route('/{}'.format(secret), methods=["POST"])
def flask_start():
    update = request.get_json()
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        bot.send_message(chat_id, "you said '{}'".format(text))
    return "ok"

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id, "Hi!")
