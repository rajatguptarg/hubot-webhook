#!/usr/bin/env python

from abc import ABCMeta, abstractmethod


class Command(object):
    """
    Command Object
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self, command, channel):
        pass
