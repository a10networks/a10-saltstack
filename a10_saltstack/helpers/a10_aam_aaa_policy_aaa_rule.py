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
AVAILABLE_PROPERTIES = ["access_list","action","authentication_template","authorize_policy","domain_name","host","index","match_encoded_uri","port","sampling_enable","uri","user_agent","user_tag","uuid","aaa_policy_name",]

REF_PROPERTIES = {
    "authentication_template": "/axapi/v3/aam/authentication/template",
    "authorize_policy": "/axapi/v3/aam/authorization/policy",
}

MODULE_NAME = "aaa-rule"

PARENT_KEYS = ["aaa_policy_name",]

CHILD_KEYS = ["index",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/aam/aaa-policy/{aaa_policy_name}/aaa-rule/{index}"
    f_dict = {}
    f_dict["index"] = ""
    f_dict["aaa_policy_name"] = kwargs["aaa_policy_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/aam/aaa-policy/{aaa_policy_name}/aaa-rule/{index}"
    f_dict = {}
    f_dict["index"] = kwargs["index"]
    f_dict["aaa_policy_name"] = kwargs["aaa_policy_name"]

    return url_base.format(**f_dict)