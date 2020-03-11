#!/usr/bin/env python

"""
ipshaman-server
"""

import json

from core import geoip

from sanic import Sanic
from sanic import response

app = Sanic()
g = geoip.GeoIPLookup()


@app.route('/')
async def index(request):
    return await response.file('index.html')


@app.route('/', methods=['POST',])
async def post_handler(request):
    ip = request.form.get('ip') or '8.8.8.8'
    url = app.url_for('lookup', ip=ip)
    return response.redirect(url)


@app.route('/<ip>')
async def lookup(request, ip):
    data = json.dumps(g.lookup(ip), indent=2, sort_keys=True)
    return response.text(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
