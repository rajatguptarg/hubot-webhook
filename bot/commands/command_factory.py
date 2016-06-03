#!/usr/bin/env python

import re
from .hello_command import HelloCommand


class CommandFactory(object):
    """
    Factory which provides the command objects
    """

    def perform(self, command, channel):
        if(re.search('(H)(i|ello)(.*)$', command, re.IGNORECASE)):
            return self.hello_command.execute(command, channel)

        return "Sorry I can't understand you."

    def __init__(self):
        super(self.__class__, self).__init__()
        self.hello_command = HelloCommand()
