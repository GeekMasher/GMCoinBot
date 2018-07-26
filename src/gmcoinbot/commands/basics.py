
from logging import getLogger

from gmcoinbot.command import Command
from gmcoinbot.commands import command_helpers


logger = getLogger(__name__)


class Start(Command):
    __name__ = "start"

    @staticmethod
    def help():
        return "/start - welcome message"

    @classmethod
    def telegramHandle(cls, bot, update):
        cls.telegramLogInfo(update.effective_chat)
        update.message.reply_text("Hello Crypto lover...")


class Help(Command):
    __name__ = "help"

    @classmethod
    def telegramHandle(cls, bot, update):
        cls.telegramLogInfo(update.effective_chat)
        update.message.reply_text('\n'.join(command_helpers))


class Error(Command):
    __name__ = "error"

    @staticmethod
    def telegramHandle(bot, update, error):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, error)
