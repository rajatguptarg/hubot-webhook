#!/usr/bin/env python

import re
from .hello_command import HelloCommand
from .vagrant_status import VagrantStatus
from .ai_bot import AIBot
from .flight_status import FlightStatus
from .deploy import DeployAWS


class CommandFactory(object):
    """
    Factory which provides the command objects
    """

    def get_command(self, command):
        if(re.search('(H)(i|ello)(.*)$', command, re.IGNORECASE)):
            return HelloCommand()

        if(re.search('vagrant status(.*)$', command, re.IGNORECASE)):
            return VagrantStatus()

        if(re.search('flight status(.*)$', command, re.IGNORECASE)):
            return FlightStatus()

        if(re.search('provsion aws(.*)uat$', command, re.IGNORECASE)):
            return DeployAWS()

        return AIBot()

    def __init__(self):
        super(self.__class__, self).__init__()
