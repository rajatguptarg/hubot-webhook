#!/usr/bin/env python

import re
from .hello_command import HelloCommand
from .vagrant_status import VagrantStatus


class CommandFactory(object):
    """
    Factory which provides the command objects
    """

    def get_command(self, command):
        if(re.search('(H)(i|ello)(.*)$', command, re.IGNORECASE)):
            return HelloCommand()

        if(re.search('vagrant status$', command, re.IGNORECASE)):
            return VagrantStatus()

        return "Sorry I can't understand you."

    def __init__(self):
        super(self.__class__, self).__init__()
