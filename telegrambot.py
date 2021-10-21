from telegram.ext import *
from accounts.models import User
from offers.models import Parcel

API_KEY='2093405201:AAGfXsXabvaLwThegS2u0kUnr9jEckmqx1k'

print('Bot started')

def handle_message(update, context):
    text = str(update.message.text).lower()
    user = update["message"]["chat"]["first_name"]
    user_db = User.objects.filter(telegram=user)

    if user_db:
        update.message.reply_text(f'Hi from telegram bot {update["message"]["chat"]["first_name"]}')
    else:
        print('eblan')

if __name__=='__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling(1.0)
    updater.idle()