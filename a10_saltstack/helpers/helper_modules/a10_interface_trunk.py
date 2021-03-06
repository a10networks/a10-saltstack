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
AVAILABLE_PROPERTIES = ["access_list","action","bfd","ddos","do_auto_recovery","icmp_rate_limit","icmpv6_rate_limit","ifnum","ip","ipv6","isis","l3_vlan_fwd_disable","lw_4o6","map","mtu","name","nptv6","ports_threshold","timer","trap_source","user_tag","uuid",]

REF_PROPERTIES = {
    "bfd": "/axapi/v3/interface/trunk/{ifnum}/bfd",
    "ddos": "/axapi/v3/interface/trunk/{ifnum}/ddos",
    "ip": "/axapi/v3/interface/trunk/{ifnum}/ip",
    "ipv6": "/axapi/v3/interface/trunk/{ifnum}/ipv6",
    "isis": "/axapi/v3/interface/trunk/{ifnum}/isis",
    "lw_4o6": "/axapi/v3/interface/trunk/{ifnum}/lw-4o6",
    "map": "/axapi/v3/interface/trunk/{ifnum}/map",
    "nptv6": "/axapi/v3/interface/trunk/{ifnum}/nptv6",
}

MODULE_NAME = "trunk"

PARENT_KEYS = []

CHILD_KEYS = ["ifnum",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/interface/trunk/{ifnum}"
    f_dict = {}
    f_dict["ifnum"] = ""

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/interface/trunk/{ifnum}"
    f_dict = {}
    f_dict["ifnum"] = kwargs["ifnum"]

    return url_base.format(**f_dict)