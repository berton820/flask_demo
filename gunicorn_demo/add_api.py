#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
add_api.py
2018/7/31 下午4:23 by berton
"""
import json
import requests


def add_api(zh, en):
    URL = 'http://0.0.0.0:16384/'
    payload = {'zh': zh,
               'en': en
               }
    res = requests.get(URL, payload)
    if res.status_code == 200:
        result = json.loads(res.content)
        return (result['total'])


add_api(16, 2)
