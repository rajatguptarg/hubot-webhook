#!/usr/bin/env python

import os


class VagrantStatus(object):
    """
    Command:
        vagrant status
    """

    def execute(self, command, channel):
        status = os.system("ssh vagrant@192.168.33.10 'bash' < bash/vagrant_status.sh")
        if status == 0:
            return "Vagrant box is up"
        return "Vagrant box is down."
