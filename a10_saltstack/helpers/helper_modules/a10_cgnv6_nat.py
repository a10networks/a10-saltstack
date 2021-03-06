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
AVAILABLE_PROPERTIES = ["icmp","icmpv6","inside","pool_group_list","pool_list","range_list_list",]

REF_PROPERTIES = {
    "icmp": "/axapi/v3/cgnv6/nat/icmp",
    "icmpv6": "/axapi/v3/cgnv6/nat/icmpv6",
    "inside": "/axapi/v3/cgnv6/nat/inside",
    "pool_group_list": "/axapi/v3/cgnv6/nat/pool-group/{pool-group-name}",
    "pool_list": "/axapi/v3/cgnv6/nat/pool/{pool-name}",
    "range_list_list": "/axapi/v3/cgnv6/nat/range-list/{name}+{partition}",
}

MODULE_NAME = "nat"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/cgnv6/nat"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/cgnv6/nat"
    f_dict = {}

    return url_base.format(**f_dict)