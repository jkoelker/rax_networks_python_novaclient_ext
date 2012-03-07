# Copyright 2011 OpenStack, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from novaclient import base
from novaclient import utils


class Network(base.Resource):
    def delete(self):
        self.manager.delete(network=self)


class NetworkManager(base.ManagerWithFind):
    resource_class = base.Resource

    def list(self):
        return self._list('/rs-networks', 'networks')

    def get(self, network):
        return self._get('/rs-networks/%s', base.getid(network), 'network')

    def delete(self, network):
        self._delete('/rs-networks/%s', base.getid(network))

    def create(self, label, cidr):
        body = 'stub'
        return self._create('/rs-networks', body, 'network')


@utils.arg('network_id', metavar='<network_id>', help='ID of network')
def do_network(cs, args):
    """
    Show a network
    """
    network = cs.rs._networks_python_novaclient_ext.get(args.network_id)
    utils.print_dict(network._info)


def do_network_list(cs, args):
    """
    List networks
    """
    networks = cs.rs._networks_python_novaclient_ext.list()
    utils.print_list(networks)


@utils.arg('label', metavar='<network_label>',
           help='Network label (ex. my_new_network)')
@utils.arg('cidr', metavar='<cidr>',
           help='IP block to allocate from (ex. 172.16.0.0/24 or '
                '2001:DB8::/64)')
def do_network_create(cs, args):
    """
    Create a network
    """
    network = cs.rs._networks_python_novaclient_ext.create(args.label,
                                                           args.cidr)
    utils.print_dict(network._info)


@utils.arg('network_id', metavar='<network_id>', help='ID of network')
def do_network_delete(cs, args):
    """
    Delete a network
    """
    cs.rs._networks_python_novaclient_ext.delete(args.network_id)
