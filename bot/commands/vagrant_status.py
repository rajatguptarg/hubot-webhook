#!/usr/bin/env python

import os
from .command import Command
from bot.resources import messages as msg
from bot.resources import deploy_commands as dc


class VagrantStatus(Command):
    """
    Command:
        vagrant status
    """

    def execute(self, command, user):
        self.logger.info(
            'Running command by ' + user.real_name + ' -> ' + dc.VAGRANT_STATUS)

        status = os.system(dc.VAGRANT_STATUS)
        self.notifier.notify(
            message=user.real_name + ' is testing the Deployment Box status.')

        if status == 0:
            return msg.VAGRANT_UP
        return msg.VAGRANT_DOWN
