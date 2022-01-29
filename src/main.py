import os
from os import environ
import logging

from flask import Flask, request
import telebot

from src.bot import messages, tools

MODE = bool(int(environ.get("MODE")))  # True: work version (webhook); False: test mode (polling)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

if MODE:
    TG_API_TOKEN = environ.get("TG_API_TOKEN")
    telegram_bot = telebot.TeleBot(TG_API_TOKEN)
    HEROKU_APP_NAME = 'HEROKU_APP_NAME'
    server = Flask(__name__)


    @server.route('/' + TG_API_TOKEN, methods=['POST'])
    def getMessage():
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        telegram_bot.process_new_updates([update])
        return "!", 200


    @server.route("/")
    def webhook():
        telegram_bot.remove_webhook()
        telegram_bot.set_webhook(url=HEROKU_APP_NAME + TG_API_TOKEN)
        return "Welcome!", 200

else:
    TG_API_TOKEN = environ.get("TG_API_TOKEN")
    telegram_bot = telebot.TeleBot(TG_API_TOKEN)


# Handle '/start'
@telegram_bot.message_handler(commands=['start'])
def send_welcome(message):
    tools.deletion_from_context(message.chat.id)
    telegram_bot.send_message(message.chat.id, messages.start, parse_mode="Markdown")

    logger.info(f"User with chat_id {message.chat.id} sent /start")


# Handle '/help'
@telegram_bot.message_handler(commands=['help'])
def send_help(message):
    tools.deletion_from_context(message.chat.id)
    telegram_bot.send_message(message.chat.id, messages.support, parse_mode="Markdown")

    logger.info(f"User with chat_id {message.chat.id} sent /help")


@telegram_bot.message_handler(content_types=['text'])
def answer_all(message):
    context = tools.context.get(message.chat.id)
    # Project logic


if MODE:
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
else:
    telegram_bot.infinity_polling()
