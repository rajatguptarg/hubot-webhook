#!/usr/bin/env python


class SlackUser(object):
    """
    A slack user details
    """

    def __init__(self, info):
        super(self.__class__, self).__init__()
        self.is_owner = info.get('is_owner')
        self.is_restricted = info.get('is_restricted')

        # This is username of the slack
        self.name = info.get('name')

        # This is Full Name of the user
        self.real_name = info.get('real_name')

        self.id = info.get('id')
        self.channel = None
        self.is_admin = info.get('is_admin')
        self.is_bot = info.get('is_bot')

        # Profile Datails
        self.email = info.get('profile').get('email')
        self.phone = info.get('profile').get('phone')
        self.skype = info.get('profile').get('skype')

        # Meta Data
        self.meta = info
