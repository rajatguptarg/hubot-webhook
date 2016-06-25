#!/usr/bin/env python

import re
from .command import Command
from bot.resources import *     # noqa


class AIBot(Command):
    """
    Command:
        <any unknown command>
    """

    def execute(self, command, user):
        command = re.sub(r'<(.*)>(: | )', r'', command)
        self.logger.info('Calling clever bot api for ' + command)
        clever_bot = Cleverbot()
        return clever_bot.ask(command)
