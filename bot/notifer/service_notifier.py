#!/usr/bin/env python

from apscheduler.schedulers.blocking import BlockingScheduler
import argparse

sched = BlockingScheduler()
parser = argparse.ArgumentParser()


parser.add_argument(
    '-e', '--env', action='store', dest='env',
    help='Environment of the Services', required=True
)

options = parser.parse_args()


@sched.scheduled_job('interval', minutes=0)
def timed_job():
    print('This job is run every three minutes.')

sched.start()
