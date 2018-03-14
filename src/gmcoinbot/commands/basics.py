

import logging
logger = logging.getLogger(__name__)


def cmd_start(bot, update):
    logger.info('start')
    update.message.reply_text("Hello Crypto lover...")


def cmd_help(bot, update):
    logger.info('help')

    from gmcoinbot.commands import command_helpers

    update.message.reply_text('\n'.join(command_helpers))


def cmd_error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

