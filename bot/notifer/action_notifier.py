#!/usr/bin/env python

from bot.info import BotInfo
import json


class Notifier(object):
    """
    Notify the group about the user actions
    """
    def notify(self, channel='#testops', message='', user=True):
        """
        Send action message to slack channel
        """
        return self.client.api_call(
            "chat.postMessage", channel=channel, text=message, as_user=user)

    def send_attachments(self, channel, text, attachment):
        """
        Send attachments to the user
        """
        return self.client.api_call(
            "chat.postMessage", channel=channel, text=text,
            parse="full", attachments=json.dumps(attachment), as_user=True)

    def __init__(self):
        super(self.__class__, self).__init__()
        self.client = BotInfo.slack_client()
