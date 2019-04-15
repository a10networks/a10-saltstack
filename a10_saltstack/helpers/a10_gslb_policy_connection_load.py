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
    "connection_load_enable",
    "connection_load_fail_break",
    "connection_load_interval",
    "connection_load_limit",
    "connection_load_samples",
    "limit",
    "uuid",
    "policy_name",
]

REF_PROPERTIES = {
}

MODULE_NAME = "connection-load"

PARENT_KEYS = ["policy_name",]

CHILD_KEYS = []


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/policy/{policy_name}/connection-load"
    f_dict = {}
    f_dict["policy_name"] = kwargs["policy_name"]

    return url_base.format(**f_dict)


def existing_url():
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/policy/{policy_name}/connection-load"
    f_dict = {}
    f_dict["policy_name"] = kwargs["policy_name"]

    return url_base.format(**f_dict)