#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
import logging
from logging.config import dictConfig
from bot.notifer import Notifier


class Command(object):
    """
    Command Object which is being inherited by the all the commands
    which are being executed by the bot.
    """
    __metaclass__ = ABCMeta

    logging_config = dict(
        version=1,
        formatters={
            'f': {'format':
                  '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
        handlers={
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': logging.DEBUG}
        },
        root={
            'handlers': ['h'],
            'level': logging.DEBUG,
        },
    )

    dictConfig(logging_config)

    logger = logging.getLogger(__name__)
    notifier = Notifier()

    @abstractmethod
    def execute(self, command, user):
        pass
