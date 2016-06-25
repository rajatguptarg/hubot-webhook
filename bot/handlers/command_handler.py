#!/usr/bin/env python

from bot.commands import CommandFactory
from bot.info import BotInfo


class CommandHandler(object):
    """
    Handles the commands coming from slack
    """

    def handle_command(self, message, channel, user_id):
        """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
        """
        if channel is not None and message is not None:
            user = BotInfo.get_user(user_id)
            user.channel = channel
            command = self.command_factory.get_command(message)
            response = command.execute(message, user)
            return self.slack_client.api_call(
                "chat.postMessage", channel=channel, text=response, as_user=True)

    def __init__(self, slack_client):
        super(self.__class__, self).__init__()
        self.command_factory = CommandFactory()
        self.slack_client = slack_client
