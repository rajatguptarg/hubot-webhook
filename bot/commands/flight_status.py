#!/usr/bin/env python

from .command import Command
from bot.resources import messages as msg
from bot.air_transport import FlightStatusGateway
import re


class FlightStatus(Command):
    """
    Command:
        flight status 9W412
    """

    def execute(self, command, user):
        gateway = FlightStatusGateway()
        flight_number = re.sub(r'[?.,!@#$%^&*]*', '', command).split()[-1]

        self.logger.info(
            'Getting flight info of flight number ' + flight_number)

        gateway.process_fight_update(flight_number, user.channel)

        return msg.POWERED_BY_CTRIP
