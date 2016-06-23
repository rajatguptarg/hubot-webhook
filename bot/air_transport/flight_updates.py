#!/usr/bin/env python

import requests as r
from bs4 import BeautifulSoup
from bot.notifer import Notifier


class FlightStatusGateway(object):
    """
    Gateway of CTrip website and Messanger
    """

    def process_fight_update(self, flight_number, user_id):
        """
        Process the flight status for user
        """
        flight_plans = self.get_flight_plans(flight_number)
        self.send_flight_plans(flight_plans, user_id)

    def get_flight_plans(self, flight_number):
        """
        Get all flight plans for flight
        """
        response = r.get('http://english.ctrip.com/flights/status-' + flight_number)
        html = response.content

        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", attrs={"class": "flightDynamic_table"})

        # The first tr contains the field names.
        headings = [th.get_text() for th in table.find("tr").find_all("th")]

        datasets = list()

        for row in table.find_all("tr")[1:]:
            dataset = list(zip(
                headings, (td.get_text() for td in row.find_all("td"))))
        datasets.append(dataset)

        flight_plans = list()

        for flight_plan in datasets:
            d = dict()
            for item in flight_plan:
                x = item[0].strip()
                y = item[1].strip()
                d[x] = y
            flight_plans.append(d)

        return flight_plans

    def send_flight_plans(self, flight_plans, user_id):
        """
        Send the available flight plans
        """
        for flight_plan in flight_plans:
            attachment = self.create_flight_attachment(flight_plan)
            return self.notifier.send_attachments(
                    user_id, 'Here are the details you asked for. :blush:', attachment)

    def create_flight_attachment(self, flight):
        """
        Create a attachment needs to be send
        """
        attachment = [{
            "fallback": "Flight Status",
            "color": "good",
            "title": "Flight Status Details",
            "text": "The details of the flight you asked for are: ",
            "fields": [
                {
                    "title": "Flight Number",
                    "value": flight.get('Flight No.'),
                    "short": "true"
                },
                {
                    "title": "Status",
                    "value": flight.get('Status'),
                    "short": "true"
                },
                {
                    "title": "Depature",
                    "value": flight.get('Dep.airport'),
                    "short": "true"
                },
                {
                    "title": "Arrival",
                    "value": flight.get('Arr.airport'),
                    "short": "true"
                },
                {
                    "title": "Estimated Time",
                    "value": flight.get('Estimated'),
                    "short": "false"
                },
                {
                    "title": "Actual Time",
                    "value": flight.get('Actual'),
                    "short": "false"
                },
                {
                    "title": "Scheduled Time",
                    "value": flight.get('Scheduled'),
                    "short": "false"
                }
            ],
            "thumb_url": "http://icons.iconarchive.com/icons/martz90/circle-addon2/512/plane-flight-icon.png"   # noqa
        }]

        return attachment

    def __init__(self):
        super(self.__class__, self).__init__()
        self.notifier = Notifier()
