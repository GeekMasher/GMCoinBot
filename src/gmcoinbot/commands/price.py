
import logging

from gmcoinbot import Config

from ccxt.base.errors import ExchangeError

logger = logging.getLogger(__name__)

PRICE_FORMAT = """\
{symbol} :: {price:<12} ({exchange})\
"""


def cmd_price(bot, update, args):
    """
    """

    try:
        chat = update.effective_chat

        user = chat.title if chat.type == 'group' else chat.username
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

            logger.info('[{}] price :: {}'.format(user, msg))

            update.message.reply_text(msg)
        else:
            update.message.reply_text('Unknown Symbol: {}'.format(symbol))

    except (IndexError, ValueError) as err:
        update.message.reply_text('Usage: /price <symbol>')
        logger.warning(str(err))
        
        if Config.isTesting():
            raise err
    except ExchangeError as err:
        update.message.reply_text('Error: ' + str(err))


def cmd_setexchange(bot, update, args):
    try:
        chat = update.effective_chat
        user = chat.title if chat.type == 'group' else chat.username

        ex = args.pop(0) if len(args) == 1 else 'kraken'

        if Config.checkExchanges(ex.lower()):
            logger.info('[{}] setexchange :: {}'.format(user, ex))

            Config.updateChatSettings(chat, exchange=ex)
            
            update.message.reply_text(
                'Set `{}` exchange to `{}`'.format(user, ex)
            )
        else:
            update.message.reply_text('Unknown Exchange: {}'.format(ex))

    except Exception as err:
        update.message.reply_text('Usage: /setexchange <exchange>')
        logger.warning(str(err))
