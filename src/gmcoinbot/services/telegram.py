
from gmcoinbot import Config, logger
from gmcoinbot.commands import *

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import InvalidToken


def run_telegram():
    
    try:
        updater = Updater(Config.API_KEYS.get('telegram'))
    except InvalidToken:
        logger.error('Invalid Telegram Token...')
        return

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler(
        "start", Start.telegramHandle
    ))
    dp.add_handler(CommandHandler(
        "help", Help.telegramHandle
    ))
    dp.add_handler(CommandHandler(
        "price", Price.telegramHandle, pass_args=True
    ))
    dp.add_handler(CommandHandler(
        "setexchange", SetExchange.telegramHandle, pass_args=True
    ))

    dp.add_handler(CommandHandler(
        "healthcheck", HealthCheck.telegramHandle, pass_chat_data=True
    ))

    # log all errors
    dp.add_error_handler(Error.telegramHandle)

    #
    logger.info('Init API call')
    price = Config.getPrice()
    logger.info('Init Price : {}'.format(price))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()
