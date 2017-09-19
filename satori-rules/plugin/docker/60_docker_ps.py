#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

# -- stdlib --
import json
import os
import sys
import time

# -- third party --
# -- own --

# -- code --
ts = int(time.time())

rst = []
if os.system('which docker > /dev/null'):
    print '[]'
    sys.exit(0)

stuck = bool(os.system("timeout -k 3s 3s sudo docker ps > /dev/null 2>&1"))

rst = [{
    'metric': 'docker.stuck',
    'timestamp': ts,
    'value': int(stuck),
}]

print json.dumps(rst)
