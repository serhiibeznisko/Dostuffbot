
from telegram.ext import Updater

import env
from bots import handlers as bots_handlers
from main import logger


def main():
    # Configure bot
    updater = Updater(env.TOKEN)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(bots_handlers.start_cmd_handler)
    dp.add_handler(bots_handlers.start_handler)
    dp.add_handler(bots_handlers.add_bot_handler)
    dp.add_handler(bots_handlers.my_bots_handler)
    dp.add_handler(bots_handlers.token_handler)
    dp.add_handler(bots_handlers.unknown_handler)

    # Log all errors
    dp.add_error_handler(logger.error)

    # Start bot
    updater.start_polling()
    print('Bot is running.')
    updater.idle()
