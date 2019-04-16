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
AVAILABLE_PROPERTIES = ["name","port","uuid","collector_group_name",]

REF_PROPERTIES = {
    "name": "/axapi/v3/acos-events/log-server",
    "port": "/axapi/v3/acos-events/log-server/port",
}

MODULE_NAME = "log-server"

PARENT_KEYS = ["collector_group_name",]

CHILD_KEYS = ["name","port",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/acos-events/collector-group/{collector_group_name}/log-server/{name}+{port}"
    f_dict = {}
    f_dict["name"] = ""
    f_dict["port"] = ""
    f_dict["collector_group_name"] = kwargs["collector_group_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/acos-events/collector-group/{collector_group_name}/log-server/{name}+{port}"
    f_dict = {}
    f_dict["name"] = kwargs["name"]
    f_dict["port"] = kwargs["port"]
    f_dict["collector_group_name"] = kwargs["collector_group_name"]

    return url_base.format(**f_dict)