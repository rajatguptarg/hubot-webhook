#!/usr/bin/env python
import os
from slackclient import SlackClient
import logging


BOT_NAME = 'sam'
slack_client = SlackClient(os.environ.get('SAM_TOKEN'))


class BotInfo(object):
    """
    Bot Details from Slack
    """
    @staticmethod
    def get_bot_id():
        """
        Returns the bot id from Slack
        """
        api_call = slack_client.api_call("users.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == BOT_NAME:
                    logging.info("Bot ID for '" + user['name'] + "' is " + user.get('id'))
                    return user.get('id')
        else:
            logging.error("could not find bot user with the name " + BOT_NAME)
            return None

    def __init__(self):
        super(self.__class__, self).__init__()
