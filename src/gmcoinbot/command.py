#!/usr/bin/env python

from logging import getLogger

logger = getLogger(__name__)


class Command:
    __name__ = "BasicCommand"

    @staticmethod
    def handles():
        """Gets a list of handles

        Returns:
            list -- list of handles
        """

        return []

    @classmethod
    def help(clss):
        return '/' + clss.__name__ + ' - N/A'

    # Telegram Support
    @classmethod
    def telegramHandle(cls, *argvs, **kargvs):
        raise Exception('Telegram handle is currently not supported')

    @staticmethod
    def _telegramUsernameFromChat(chat):
        if chat.type == 'group':
            return chat.title
        elif chat.type == 'private' and hasattr(chat, 'username'):
            return chat.username
        return "UnknownUser"

    @classmethod
    def telegramLogInfo(cls, chat, message=None):
        message = ' - ' + message if message is not None else ''
        logger.info("{} :: [{}] {}".format(
            cls.__name__, Command._telegramUsernameFromChat(chat), message
        ))

    @classmethod
    def telegramLogWarning(cls, chat, message=None):
        message = ' - ' + message if message is not None else ''
        logger.warning("{} :: [{}] {}".format(
            cls.__name__, Command._telegramUsernameFromChat(chat), message
        ))

    # Discord Support
    @classmethod
    def discordHandle(cls, *argvs, **kargvs):
        raise Exception('Discord handle is currently not supported')
