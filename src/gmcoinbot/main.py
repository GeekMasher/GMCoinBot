
import os
import logging

from gmcoinbot import Config, __name__
from gmcoinbot.commands import *

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.error import InvalidToken

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def main():
    """
    """
    Config.initCLI()

    # This will be fixed in new version of GMUtils
    Config.ENV = os.environ.get(__name__.upper() + '_ENV', 'TESTING')
    
    config_file = './data/config.{}.json'.format(Config.ENV.lower())
    if os.path.exists(config_file):
        logger.info('Config.load("{}")'.format(config_file))
        Config.loadFile(config_file)

    config_file = '/etc/{}/config.{}.json'.format(__name__, Config.ENV.lower())
    if os.path.exists(config_file):
        logger.info('Config.load("{}")'.format(config_file))
        Config.loadFile(config_file)
    
    try:
        updater = Updater(Config.API_KEYS.get('telegram'))
    except InvalidToken:
        logger.error('Invalid Telegram Token...')
        return

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler(
        "start", cmd_start
    ))
    dp.add_handler(CommandHandler(
        "help", cmd_help
    ))
    dp.add_handler(CommandHandler(
        "price", cmd_price, pass_args=True
    ))
    dp.add_handler(CommandHandler(
        "setexchange", cmd_setexchange, pass_args=True
    ))

    dp.add_handler(CommandHandler(
        "healthcheck", cmd_healthcheck, pass_chat_data=True
    ))

    # log all errors
    dp.add_error_handler(cmd_error)

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

    # export the current settings 
    Config.export('./data/config.json')
