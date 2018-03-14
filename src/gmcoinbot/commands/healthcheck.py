
from gmcoinbot import Config

from logging import getLogger

logger = getLogger(__name__)


def cmd_healthcheck(bot, update, chat_data):
    try:
        chat = update.effective_chat

        settings = Config.getChatSettings(chat)

        # logger.info(Config.export(export_object=update))
        logger.info('[{}] - {}'.format(type(chat), chat))

        update.message.reply_text('Test...')
    except Exception as err:
        logger.warning(str(err))