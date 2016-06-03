#!/usr/bin/env python

from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    """
    Command Object
    """

    @abstractmethod
    def execute(self, command, channel):
        pass
