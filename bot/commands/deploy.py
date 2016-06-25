#!/usr/bin/env python

import os
from .command import Command
from bot.resources import messages as msg
from bot.resources import deploy_commands as dc
from time import strptime, strftime, gmtime


class DeployAWS(Command):
    """
    Command:
        provision aws uat
    """

    def execute(self, command, user):
        self.logger.info(
            'Runing command by ' + user.real_name + '->' + dc.AWS_UAT_PROVISION)

        self.notifier.notify(
            message=user.real_name + ' is provisioning the UAT infrastructure')

        if self.valid_action(user):
            status = os.system(dc.AWS_UAT_PROVISION)

            if status == 0:
                return msg.SUCCESSFUL
            return msg.FAILED

        return msg.UNAUTHORIZED_ACTION

    def valid_action(self, user):
        """
        Check wheather it is valid user to deploy
        Note: The deployment window timings are in GMT.
        Sample Date Format Expected: '2016-06-23 23:55:45'
        """
        start_time = os.environ.get('DEPLOY_START_TIME')
        end_time = os.environ.get('DEPLOY_END_TIME')

        current_gmt_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        current_gmt_time = strptime(current_gmt_time, "%Y-%m-%d %H:%M:%S")
        deploy_start_time = strptime(start_time, "%Y-%m-%d %H:%M:%S")
        deploy_end_time = strptime(end_time, "%Y-%m-%d %H:%M:%S")

        valid_time = deploy_start_time <= current_gmt_time <= deploy_end_time

        return True

