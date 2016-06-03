#!/usr/bin/env python

import os
import time
from slackclient import SlackClient
from bot.info import BotInfo
from bot.parser import CommandParser
from bot.handlers import CommandHandler


slack_client = SlackClient(os.environ.get('SAM_TOKEN'))
BOT_ID = BotInfo.get_bot_id()
parser = CommandParser(BOT_ID)
handler = CommandHandler(slack_client)


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1    # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("CallBot connected and running!")
        while True:
            command, channel = parser.parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handler.handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
