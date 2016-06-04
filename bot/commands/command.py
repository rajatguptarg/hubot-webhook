#!/usr/bin/env python

from abc import ABCMeta, abstractmethod
import logging
from logging.config import dictConfig


class Command(object):
    """
    Command Object
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
    logger = logging.getLogger()
    logger.debug('Logger Initiated.')

    @abstractmethod
    def execute(self, command, channel):
        pass
