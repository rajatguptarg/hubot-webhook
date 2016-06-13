#!/usr/bin/env python


class CommandParser(object):
    """
    To parse the commands coming from Slack Channels
    """

    def parse_slack_output(self, slack_rtm_output):
        """
        The Slack Real Time Messaging API is a firehose of data, so
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
        """
        output_list = slack_rtm_output
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output.get('user') != self.BOT_ID and output and 'text' in output:
                    print(output)
                    return output['text'], output['channel'], output['user']
                return None, None, None
        return None, None, None

    def __init__(self, BOT_ID):
        super(self.__class__, self).__init__()
        self.BOT_ID = BOT_ID
