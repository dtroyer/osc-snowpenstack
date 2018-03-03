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

"""Plugin action implementation"""

import logging

from cliff import lister
from cliff import show


class FlightList(lister.Lister):
    """List flights"""

    auth_required = False
    log = logging.getLogger(__name__ + ".FlightList")

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)" % parsed_args)

        data = []

        columns = ("Name", "Whistle")
        return (columns, data)


class FlightShow(show.ShowOne):
    """Show flight information"""

    auth_required = False
    log = logging.getLogger(__name__ + '.FlightShow')

    def get_parser(self, prog_name):
        parser = super(FlightShow, self).get_parser(prog_name)
        parser.add_argument(
            'name',
            metavar='<flight-name>',
            help='Flight to show',
        )
        return parser

    def take_action(self, parsed_args):
        self.log.debug('take_action(%s)' % parsed_args)

        return (
            ["name", "whistle", "data"],
            [parsed_args.name, True, ''],
        )
