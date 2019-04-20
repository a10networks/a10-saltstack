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

from a10_saltstack.forest.nodes import InterNode


class ForestGen(object):

    def __init__(self):
        self.node_list = []

    def dfs_cut(self, obj):
        '''
        This iterates over the tree and extracts
        refrence objects out of it
        '''
        if obj.children:
            for child in obj.children:
                if type(child) == InterNode:
                    self.node_list.append(child)
                self.dfs_cut(child)
