#!/usr/bin/env python

import os
from .command import Command
from bot.resources import messages as msg


NOTIFIER = os.getcwd() + '/bot/notifer/service_notifier.py'


class ServiceHealth(Command):
    """
    Command:
        check services on (uat | prod)
    """

    def execute(self, command, user):
        self.logger.info(
            'Running command by ' + user.real_name + ' -> ' + str(command))

        # TODO: Future Work
        """
            Future scope
            ~~~~~~~~~~~~

            Ask the environment for which notifier should run from the Deep Mind
            Module.

        """
        env = None
        env = 'uat' if 'uat' in command else env
        env = 'prod' if 'prod' in command else env

        if env:
            python_path = os.popen('which python').read().strip()
            cmd = [python_path, 'python', NOTIFIER, '-e', env]
            pid = os.spawnlp(os.P_NOWAIT, *cmd)

        self.notifier.notify(
            message=user.real_name + ' started the notification service for ' + env +
            'with pid ' + str(pid)
        )

        return msg.SERVICE_NOTIFIER_SUCCESS
