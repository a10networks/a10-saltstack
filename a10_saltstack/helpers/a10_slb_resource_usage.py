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
AVAILABLE_PROPERTIES = [    "client_ssl_template_count",
    "conn_reuse_template_count",
    "fast_tcp_template_count",
    "fast_udp_template_count",
    "health_monitor_count",
    "http_template_count",
    "nat_pool_addr_count",
    "pbslb_subnet_count",
    "persist_cookie_template_count",
    "persist_srcip_template_count",
    "proxy_template_count",
    "real_port_count",
    "real_server_count",
    "server_ssl_template_count",
    "service_group_count",
    "stream_template_count",
    "uuid",
    "virtual_port_count",
    "virtual_server_count",
]

MODULE_NAME = "resource-usage"

def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/resource-usage"
    f_dict = {}

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/resource-usage"
    f_dict = {}

    return url_base.format(**f_dict)