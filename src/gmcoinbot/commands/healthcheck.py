
from gmcoinbot import Config, Command, version

from logging import getLogger

logger = getLogger(__name__)

HEALTH_DATA = """\
GMCoinBot v{version}
"""


class HealthCheck(Command):
    __name__ = "healthcheck"

    @staticmethod
    def help():
        return "/healthcheck - make sure everything is ship-shape!"

    @classmethod
    def telegramHandle(cls, bot, update, chat_data):
        try:
            chat = update.effective_chat
            cls.telegramLogInfo(chat)

            settings = Config.getChatSettings(chat)

            cls.telegramLogInfo(chat, str(chat))

            msg = HEALTH_DATA.format(
                version=version
            )

            update.message.reply_text(msg)

        except Exception as err:
            logger.warning(str(err))
