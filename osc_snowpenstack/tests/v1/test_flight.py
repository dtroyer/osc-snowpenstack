#   Copyright 2013 Nebula Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

from osc_snowpenstack.tests import base
from osc_snowpenstack.tests import fakes
from osc_snowpenstack.v1 import flight

# Load the plugin init module for the plugin list and show commands
plugin_name = 'osc_snowpenstack'
plugin_client = 'osc_snowpenstack.plugin'


class FakeFlightV1Client(object):
    def __init__(self, **kwargs):
        self.auth_token = kwargs['token']
        self.management_url = kwargs['endpoint']


class TestFlightV1(base.TestCommand):
    def setUp(self):
        super(TestFlightV1, self).setUp()

        self.app.client_manager.osc_snowpenstack = FakeFlightV1Client(
            endpoint=fakes.AUTH_URL,
            token=fakes.AUTH_TOKEN,
        )


class TestFlightList(TestFlightV1):

    def setUp(self):
        super(TestFlightList, self).setUp()

        # Get the command object to test
        self.cmd = flight.FlightList(self.app, None)

    def test_plugin_list(self):
        arglist = []
        verifylist = []
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        collist = ('Name', 'Whistle')
        datalist = ['1.txt', '2.txt']

        # DisplayCommandBase.take_action() returns two tuples
        columns, data = self.cmd.take_action(parsed_args)
        self.assertEqual(collist, columns)
        for d in data:
            self.assertTrue(d[0] + '.txt' in datalist)


class TestFlightShow(TestFlightV1):

    def setUp(self):
        super(TestFlightShow, self).setUp()

        # Get the command object to test
        self.cmd = flight.FlightShow(self.app, None)

    def test_flight_show(self):
        arglist = [
            plugin_name,
        ]
        verifylist = [
            ('name', plugin_name),
        ]
        parsed_args = self.check_parser(self.cmd, arglist, verifylist)

        collist = ['name', 'whistle', 'data']
        datalist = [
            plugin_name,
            True,
            '',
        ]

        columns, data = self.cmd.take_action(parsed_args)

        self.assertEqual(collist, columns)
        self.assertEqual(datalist, data)
