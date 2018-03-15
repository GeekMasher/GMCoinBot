
import logging

from gmcoinbot import Config, Command

from ccxt.base.errors import ExchangeError

logger = logging.getLogger(__name__)

PRICE_FORMAT = """\
{symbol} :: {price:<12} ({exchange})\
"""

class Price(Command):
    __name__ = "price"

    @classmethod
    def telegramHandle(cls, bot, update, args):
        chat = update.effective_chat
        user = cls._telegramUsernameFromChat(chat)

        try:
            user_settings = Config.getChatSettings(chat)

            symbol = args.pop(0) if len(args) == 1 else user_settings.get('symbol')

            if Config.checkSymbol(symbol):
                ex = user_settings.get('exchange')
                price = Config.getPrice(symbol, ex)

                msg = PRICE_FORMAT.format(
                    symbol=symbol,
                    price=price,
                    exchange=ex.name
                )
                cls.telegramLogInfo(chat, msg)

                update.message.reply_text(msg)
            else:
                msg_err = 'Unknown Symbol: {}'.format(symbol)
                cls.telegramLogWarning(chat, msg_err)

                update.message.reply_text(msg_err)

        except (IndexError, ValueError) as err:
            cls.telegramLogWarning(chat, str(err))
            update.message.reply_text('Usage: /price <symbol>')

            if Config.isTesting():
                raise err
        except ExchangeError as err:
            cls.telegramLogWarning(chat, str(err))
            update.message.reply_text('Error: ' + str(err))

            if Config.isTesting():
                raise err
