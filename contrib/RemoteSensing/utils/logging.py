# coding: utf8
# Copyright (c) 2019 PaddlePaddle Authors. All Rights Reserve.
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

import time
import os
import sys
import __init__

levels = {0: 'ERROR', 1: 'WARNING', 2: 'INFO', 3: 'DEBUG'}


def log(level=2, message=""):
    current_time = time.time()
    time_array = time.localtime(current_time)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    if __init__.log_level >= level:
        print("{} [{}]\t{}".format(current_time, levels[level],
                                   message).encode("utf-8").decode("latin1"))
        sys.stdout.flush()


def debug(message=""):
    log(level=3, message=message)


def info(message=""):
    log(level=2, message=message)


def warning(message=""):
    log(level=1, message=message)


def error(message=""):
    log(level=0, message=message)