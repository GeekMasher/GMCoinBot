
from gmcoinbot import Config, Command, logger


class SetExchange(Command):

    @classmethod
    def telegramHandle(bot, update, args):
        chat = update.effective_chat
        user = cls._telegramUsernameFromChat(chat)

        try:
            ex = args.pop(0) if len(args) == 1 else 'UNKNOWN'

            if Config.checkExchanges(ex.lower()):
                cls.telegramLogInfo(chat, ex)
                
                Config.updateChatSettings(chat, exchange=ex)

                update.message.reply_text(
                    'Set `{}` exchange to `{}`'.format(user, ex)
                )
            else:
                msg_err = 'Unknown Exchange: {}'.format(ex)
                cls.telegramLogWarning(chat, msg_err)

                update.message.reply_text(msg_err)

        except Exception as err:
            cls.telegramLogWarning(chat, str(err))
            update.message.reply_text('Usage: /setexchange <exchange>')

