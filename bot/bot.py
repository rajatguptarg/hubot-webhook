#!/usr/bin/env python
import os
import time
from slackclient import SlackClient
from bot_details import BotDetails


BOT_ID = BotDetails.get_bot_id()
slack_client = SlackClient(os.environ.get('SAM_TOKEN'))


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    print(command, channel)
    response = 'hello'
    if channel is not None and command is not None:
        return slack_client.api_call(
            "chat.postMessage", channel=channel, text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is a firehose of data, so
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        print(output_list)
        for output in output_list:
            if output.get('user') != BOT_ID and output and 'text' in output:
                return output['text'], output['channel']
            else:
                return None, None
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1    # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("CallBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
