#!/usr/bin/env python


class CommandHandler(object):
    """
    Handles the commands coming from slack
    """

    def handle_command(self, command, channel):
        """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
        """
        print(command, channel)
        response = 'hello'
        if channel is not None and command is not None:
            return self.slack_client.api_call(
                "chat.postMessage", channel=channel, text=response, as_user=True)

    def __init__(self, slack_client):
        super(self.__class__, self).__init__()
        self.slack_client = slack_client
