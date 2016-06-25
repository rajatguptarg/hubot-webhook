#!/usr/bin/env python

from .command import Command
import random


class HelloCommand(Command):
    """
    Commands:
        Hi
        Hello

    Type:
        Case-Insensetive
    """
    message = [
        'Hi', 'Hello', 'Hi There', 'Bonjor'
    ]

    def execute(self, command, user):
        msg_number = random.randrange(0, len(self.message))
        return self.message[msg_number]
