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
AVAILABLE_PROPERTIES = [
    "ip_nat",
    "ip_nat_floating_list",
    "metric_ip_nat",
    "metric_type_ip_nat",
    "ospf_list",
    "redist_list",
    "route_map_ip_nat",
    "tag_ip_nat",
    "uuid",
    "vip_floating_list",
    "vip_list",
    "ospf_process_id",
]

REF_PROPERTIES = {
}

MODULE_NAME = "redistribute"

PARENT_KEYS = ["ospf_process_id",]

CHILD_KEYS = []


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/router/ospf/{ospf_process_id}/redistribute"
    f_dict = {}
    f_dict["ospf_process_id"] = kwargs["ospf_process_id"]

    return url_base.format(**f_dict)


def existing_url():
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/router/ospf/{ospf_process_id}/redistribute"
    f_dict = {}
    f_dict["ospf_process_id"] = kwargs["ospf_process_id"]

    return url_base.format(**f_dict)