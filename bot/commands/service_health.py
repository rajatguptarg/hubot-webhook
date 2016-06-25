#!/usr/bin/env python

from .command import Command


class ServiceHealth(Command):
    """
    Command:
        provision aws uat
    """

    def execute(self, command, user):
        return 'Your service is up and running.'
