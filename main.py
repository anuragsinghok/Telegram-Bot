import constants as keys
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
import Responses as R
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler


print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type something random to get started!')

def help_command(update, context):
    update.message.reply_text('If you need help, you should ask for it on Google!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    responses = R.sample_responses(text)

    update.message.reply_text(responses)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater("5882513098:AAFVs68V4wHd-LFjQOl1NR3okGJn2DsQaUA", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
