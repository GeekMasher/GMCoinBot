

command_helpers = [
    "/start - welcome message",
    "/help - print list of commands and help descriptions",
    "/healthcheck - make sure everything is ship-shape!",
    "/setexchange <exchange> - set the exchange",
    "/price <symbol> - gets the current price of a coin from exchange (Kraken)"
]

from gmcoinbot.commands.basics import (
    cmd_start,
    cmd_help,
    cmd_error
)
from gmcoinbot.commands.price import (
    cmd_price,
    cmd_setexchange
)
from gmcoinbot.commands.healthcheck import (
    cmd_healthcheck
)
