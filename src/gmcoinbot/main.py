
import os
import logging

from gmcoinbot import Config, logger, __name__
from gmcoinbot.commands import *
from gmcoinbot.services import run_telegram


def main():
    """
    """
    Config.initCLI()
    # This will be fixed in new version of GMUtils
    Config.ENV = os.environ.get(__name__.upper() + '_ENV', 'TESTING')

    config_files = [
        '/etc/{name}/config.json',
        '/etc/{name}/config.{env}.json',
        './data/config.json'
        './data/config.{env}.json'
    ]

    for config_file in config_files:
        config_file = config_file.format(
            env=Config.ENV.lower(),
            name=__name__
        )
        if os.path.exists(config_file):
            logger.info('Config.load("{}")'.format(config_file))
            Config.loadFile(config_file)
            break

    logger.info('ENV : ' + Config.ENV)

    run_telegram()

    # export the current settings
    export_file = '/etc/{}/config.curr.json'.format(__name__)
    Config.export(export_file)
    logging.info('Config.export("{}")'.format(export_file))

