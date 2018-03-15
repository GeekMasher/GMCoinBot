
from gmcoinbot import Config, Command

from logging import getLogger

logger = getLogger(__name__)


class HealthCheck(Command):
    __name__ = "healthcheck"

    @classmethod
    def telegramHandle(cls, bot, update, chat_data):
        try:
            chat = update.effective_chat
            cls.telegramLogInfo(chat)

            settings = Config.getChatSettings(chat)

            cls.telegramLogInfo(chat, str(chat))

            update.message.reply_text('Health check test...')

        except Exception as err:
            logger.warning(str(err))
