from telegram import ParseMode
from telegram.ext import CommandHandler, CallbackQueryHandler

from main.utils import get_user_from_message
from main.keyboards import start_markup
from main.texts import start_text


def start_command(bot, update):
    ''' The start was called with /start '''
    message = update.message
    user = get_user_from_message(message)

    sent_message = message.reply_text(start_text, parse_mode=ParseMode.MARKDOWN, reply_markup=start_markup)

    user.update_dialog(bot, sent_message.message_id)
    message.delete()


def start(bot, update):
    ''' The start was called with inline keyboard '''
    query = update.callback_query

    query.answer()
    query.edit_message_text(start_text, parse_mode=ParseMode.MARKDOWN, reply_markup=start_markup)


start_command_handler = CommandHandler('start', start_command)
start_handler = CallbackQueryHandler(start, pattern='start')