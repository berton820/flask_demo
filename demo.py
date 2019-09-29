#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
predict_service.py.py
2019-01-18 19:28 by berton
berton820@126.com
"""

import os
import sys

from flask import Flask, request, jsonify

app = Flask(__name__)


def get_list(inp):
    return [_ for _ in inp]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        query = request.args.get('query', '')
    try:
        res = get_list(query)
        return jsonify({'status': '0',
                        'result': res  #
                        })
    except:
        return jsonify({'status': '1'})


if __name__ == '__main__':
    app.run(debug=None, host='0.0.0.0', port=12315)
