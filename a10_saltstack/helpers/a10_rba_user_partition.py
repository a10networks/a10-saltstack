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
    "partition_name",
    "role_list",
    "rule_list",
    "user_tag",
    "uuid",
    "user_name",
]

REF_PROPERTIES = {
    "partition_name": "/axapi/v3/partition",
}

MODULE_NAME = "partition"

PARENT_KEYS = ["user_name",]

CHILD_KEYS = ["partition-name",]


def new_url():
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/rba/user/{user_name}/partition/{partition-name}"
    f_dict = {}
    f_dict["partition-name"] = ""
    f_dict["user_name"] = kwargs["user_name"]

    return url_base.format(**f_dict)


def existing_url():
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/rba/user/{user_name}/partition/{partition-name}"
    f_dict = {}
    f_dict["partition-name"] = kwargs["partition-name"]
    f_dict["user_name"] = kwargs["user_name"]

    return url_base.format(**f_dict)