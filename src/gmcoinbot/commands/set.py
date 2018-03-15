
from json import dumps

from gmcoinbot import Config, Command, logger


class SetExchange(Command):

    @staticmethod
    def help():
        return "/setexchange <exchange> - set the users exchange settings"

    @classmethod
    def telegramHandle(cls, bot, update, args):
        chat = update.effective_chat
        user = cls._telegramUsernameFromChat(chat)

        try:
            ex = args.pop(0) if len(args) == 1 else 'UNKNOWN'

            if Config.checkExchanges(ex.lower()):
                cls.telegramLogInfo(chat, ex)
                
                Config.updateChatSettings(user, exchange=ex)

                update.message.reply_text(
                    'Symbol set to: "{}"'.format(ex)
                )
            else:
                msg_err = 'Unknown Exchange: {}'.format(ex)
                cls.telegramLogWarning(chat, msg_err)

                update.message.reply_text(msg_err)

        except Exception as err:
            cls.telegramLogWarning(chat, str(err))
            update.message.reply_text('Usage: /setexchange <exchange>')


class SetSymbol(Command):
    
    @staticmethod
    def help():
        return "/setsymbol <symbol> - sets the users symbol settings"

    @classmethod
    def telegramHandle(cls, bot, update, args):
        chat = update.effective_chat
        user = cls._telegramUsernameFromChat(chat)

        try:
            symb = args.pop(0) if len(args) == 1 else 'UNKNOWN'

            item1, item2 = symb.split('/', 1)

            user_settings = Config.getChatSettings(chat)

            if Config.checkSymbol(symb.upper()):
                cls.telegramLogInfo(chat, symb)
                
                Config.updateChatSettings(user, symbol=symb)

                logger.debug(
                    'USER `symbol` SETTING: ' + Config.USERS[user]['symbol']
                )

                update.message.reply_text('Symbol set to: "{}"'.format(symb))
            else:
                msg_err = 'Unknown Symbol: {}'.format(symb)
                cls.telegramLogWarning(chat, msg_err)

                update.message.reply_text(msg_err)

        except Exception as err:
            cls.telegramLogWarning(chat, str(err))
            update.message.reply_text('Usage: /setsymbol <symbol>')


