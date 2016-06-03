#!/usr/bin/env python

import re
from .hello_command import HelloCommand
from .vagrant_status import VagrantStatus


class CommandFactory(object):
    """
    Factory which provides the command objects
    """

    def perform(self, command, channel):
        if(re.search('(H)(i|ello)(.*)$', command, re.IGNORECASE)):
            return self.hello_command.execute(command, channel)

        if(re.search('vagrant status$', command, re.IGNORECASE)):
            return self.vagrant_status.execute(command, channel)

        return "Sorry I can't understand you."

    def __init__(self):
        super(self.__class__, self).__init__()
        self.hello_command = HelloCommand()
        self.vagrant_status = VagrantStatus()
