

command_helpers = [
    "/start - welcome message",
    "/help - print list of commands and help descriptions",
    "/healthcheck - make sure everything is ship-shape!",
    "/setexchange <exchange> - set the exchange",
    "/price <symbol> - gets the current price of a coin from exchange (Kraken)"
]

from gmcoinbot.commands.basics import (
    Start,
    Help,
    Error
)
from gmcoinbot.commands.price import (
    Price
)
from gmcoinbot.commands.set import (
    SetExchange,
    SetSymbol
)
from gmcoinbot.commands.healthcheck import (
    HealthCheck
)
