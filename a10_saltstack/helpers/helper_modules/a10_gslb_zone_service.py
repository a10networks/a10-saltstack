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
AVAILABLE_PROPERTIES = ["action","disable","dns_a_record","dns_cname_record_list","dns_mx_record_list","dns_naptr_record_list","dns_ns_record_list","dns_ptr_record_list","dns_record_list","dns_srv_record_list","dns_txt_record_list","forward_type","geo_location_list","health_check_gateway","health_check_port","policy","sampling_enable","service_name","service_port","user_tag","uuid","zone_name",]

REF_PROPERTIES = {
    "dns_a_record": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-a-record",
    "dns_cname_record_list": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-cname-record/{alias-name}",
    "dns_mx_record_list": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-mx-record/{mx-name}",
    "dns_naptr_record_list": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-naptr-record/{naptr-target}+{service-proto}+{flag}",
    "dns_ns_record_list": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-ns-record/{ns-name}",
    "dns_ptr_record_list": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-ptr-record/{ptr-name}",
    "dns_record_list": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-record/{type}",
    "dns_srv_record_list": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-srv-record/{srv-name}+{port}",
    "dns_txt_record_list": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/dns-txt-record/{record-name}",
    "geo_location_list": "/axapi/v3/gslb/zone/{name}/service/{service-port}+{service-name}/geo-location/{geo-name}",
}

MODULE_NAME = "service"

PARENT_KEYS = ["zone_name",]

CHILD_KEYS = ["service-port","service-name",]


def new_url(**kwargs):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/gslb/zone/{zone_name}/service/{service-port}+{service-name}"
    f_dict = {}
    f_dict["service-port"] = ""
    f_dict["service-name"] = ""
    f_dict["zone_name"] = kwargs["zone_name"]

    return url_base.format(**f_dict)


def existing_url(**kwargs):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/gslb/zone/{zone_name}/service/{service-port}+{service-name}"
    f_dict = {}
    f_dict["service-port"] = kwargs["service-port"]
    f_dict["service-name"] = kwargs["service-name"]
    f_dict["zone_name"] = kwargs["zone_name"]

    return url_base.format(**f_dict)