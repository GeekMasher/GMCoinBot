
from gmcoinbot.__version__ import (
    __banner__, __name__,
    __version__ as version
)
import logging

import logging
import gmutils
import ccxt

from gmcoinbot.utils.config import Config
from gmcoinbot.command import Command

Config.load()

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)
