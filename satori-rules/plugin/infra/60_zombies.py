#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

# -- stdlib --
import json
import os
import socket
import time

# -- third party --
# -- own --

# -- code --
ts = int(time.time())


def get_state(pid):
    try:
        return open('/proc/%s/stat' % i).read().split()[2]
    except Exception:
        return ''


l = filter(str.isdigit, os.listdir('/proc'))
states = ''.join([get_state(i) for i in l])

rst = [{
    'metric': 'proc.zombies',
    'timestamp': ts,
    'value': states.count('Z'),
}, {
    'metric': 'proc.uninterruptables',
    'timestamp': ts,
    'value': states.count('D'),
}]

print json.dumps(rst)
