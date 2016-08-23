#!/usr/bin/env python

import re
from .hello_command import HelloCommand
from .vagrant_status import VagrantStatus
from .ai_bot import AIBot
from .flight_status import FlightStatus
from .deploy import DeployAWS
from .service_health import ServiceHealth


class CommandFactory(object):
    """
    Factory which provides the command objects
    """
    # TODO: Future Work
    """
        Future Work
        ~~~~~~~~~~~

        Ask the command object for the respective command from the deep
        mind module.

    """

    def get_command(self, command):
        if(re.search('(H)(i|ello)(.*)$', command, re.IGNORECASE)):
            return HelloCommand()

        if(re.search('vagrant status(.*)$', command, re.IGNORECASE)):
            return VagrantStatus()

        if(re.search('flight status(.*)$', command, re.IGNORECASE)):
            return FlightStatus()

        if(re.search('provision aws(.*)uat(.*)$', command, re.IGNORECASE)):
            return DeployAWS()

        if(re.search('(.*) service(.*)$', command, re.IGNORECASE)):
            return ServiceHealth()

        return AIBot()

    def __init__(self):
        super(self.__class__, self).__init__()
