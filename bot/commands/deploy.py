#!/usr/bin/env python

import os
from .command import Command
from bot.resources import messages as msg
from bot.resources import deploy_commands as dc


class DeployAWS(Command):
    """
    Command:
        provision aws uat
    """

    def execute(self, command, user_name, user_id):
        self.logger.info(
            'Runing command by ' + user_name + '->' + dc.AWS_UAT_PROVISION)

        self.notifier.notify(
            message=user_name + 'is provisioning the UAT infrastructure')
        status = os.system(dc.AWS_UAT_PROVISION)

        if status == 0:
            return msg.SUCCESSFUL
        return msg.FAILED
