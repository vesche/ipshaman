#!/usr/bin/env python

"""
ipshaman-server
"""

from core import geoip
from core import rdap

from sanic import Sanic
from sanic import response


app = Sanic()
g = geoip.GeoIPLookup()
r = rdap.RDAPLookup()


@app.route('/')
async def index(request):
    return await response.file('index.html')


@app.route("/post", methods=['POST',])
async def post(request):
    geo_ip = request.form.get('geo')
    rdap_ip = request.form.get('rdap')
    if geo_ip:
        return response.json(g.lookup(geo_ip))
    elif rdap_ip:
        return response.json(r.lookup(rdap_ip))


@app.route('/<ip>/geo')
async def geo(request, ip):
    return response.json(g.lookup(ip))


@app.route('/<ip>/rdap')
async def rdap(request, ip):
    return response.json(r.lookup(ip))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
