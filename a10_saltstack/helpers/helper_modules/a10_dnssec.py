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
AVAILABLE_PROPERTIES = ["dnskey","ds","key_rollover","sign_zone_now","standalone","template_list","uuid",]

REF_PROPERTIES = {
    "dnskey": "/axapi/v3/dnssec/dnskey",
    "ds": "/axapi/v3/dnssec/ds",
    "key_rollover": "/axapi/v3/dnssec/key-rollover",
    "sign_zone_now": "/axapi/v3/dnssec/sign-zone-now",
    "template_list": "/axapi/v3/dnssec/template/{dnssec-temp-name}",
}

MODULE_NAME = "dnssec"

PARENT_KEYS = []

CHILD_KEYS = []


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/dnssec"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/dnssec"
    f_dict = {}

    return url_base.format(**f_dict)