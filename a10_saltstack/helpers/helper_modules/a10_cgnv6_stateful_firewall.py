# Copyright 2019 A10 Networks
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["alg","endpoint_independent_filtering","global","stun_timeout_list","tcp","udp","vrid",]

REF_PROPERTIES = {
    "alg": "/axapi/v3/cgnv6/stateful-firewall/alg",
    "endpoint_independent_filtering": "/axapi/v3/cgnv6/stateful-firewall/endpoint-independent-filtering",
    "global": "/axapi/v3/cgnv6/stateful-firewall/global",
    "stun_timeout_list": "/axapi/v3/cgnv6/stateful-firewall/stun-timeout/{port}+{port-end}",
    "tcp": "/axapi/v3/cgnv6/stateful-firewall/tcp",
    "udp": "/axapi/v3/cgnv6/stateful-firewall/udp",
    "vrid": "/axapi/v3/cgnv6/stateful-firewall/vrid",
}

MODULE_NAME = "stateful-firewall"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/stateful-firewall"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/stateful-firewall"
    f_dict = {}

    return url_base.format(**f_dict)