# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import abc

import six

from st2common.runners.utils import get_logger_for_python_runner_action

__all__ = [
    'Action'
]


@six.add_metaclass(abc.ABCMeta)
class Action(object):
    """
    Base action class other Python actions should inherit from.
    """

    description = None

    def __init__(self, config=None, action_service=None):
        """
        :param config: Action config.
        :type config: ``dict``

        :param action_service: ActionService object.
        :type action_service: :class:`ActionService~
        """
        self.config = config or {}
        self.action_service = action_service

        if action_service and getattr(action_service, '_action_wrapper', None):
            log_level = getattr(action_service._action_wrapper, '_log_level', 'debug')
        else:
            log_level = 'debug'

        self.logger = get_logger_for_python_runner_action(action_name=self.__class__.__name__,
                                                          log_level=log_level)

    @abc.abstractmethod
    def run(self, **kwargs):
        pass
