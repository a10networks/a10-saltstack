# a10_saltstack
Repository of for saltstack modules

This code is now being generated using the SDK generator at https://github.com/a10networks/sdkgenerator

## Summary
a10-salstack is a set of Saltstack modules and example playbooks for interacting with AXAPI v3 for configuration and monitoring of A10 ACOS-based hardware and virtual appliances. The module code and example playbooks are generated using a combination of Python code and Jinja templates.

## Installation
a10-saltstack is distributed as a Python package. It can be installed from the Github repository. It is assumed that saltstack is already installed and configured.

### Github Installation
~~~
git clone https://github.com/a10networks/a10-saltstack a10-saltstack
pip install -e a10-saltstack/
~~~

## Examples
Please see (https://github.com/a10networks/a10-saltstack/tree/master/examples/states) for example states.

## Bug Reporting and Feature Requests
Please submit bug reports and feature requests via GitHub issues. When reporting bugs, please include the playbook that demonstrates the bug and the Saltstack output. Stack traces are always nice, but state files work well. Please ensure any sensitive information is redacted as Issues and Pull Requests are publicly viewable.

## Contact
If you have a question that cannot be submitted via Github Issues, please email openstack-dl@a10networks.com with "a10-saltstack" in the subject line. 
