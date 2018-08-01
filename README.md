# ipshaman

This is an IP address information gathering utility capable of looking up [GeoIP](https://www.maxmind.com/en/geoip2-services-and-databases) and [RDAP](https://en.wikipedia.org/wiki/Registration_Data_Access_Protocol) information.

The [ipshaman.com](http://ipshaman.com) web server, client API, and command-line tool all currently live in this repo.

## Usage

ipshaman is easy to use from the command-line using curl:

```
$ dig +short python.org
23.253.135.79

$ curl ipshaman.com/23.253.135.79/geo
{"country_code":"US","country_code3":"USA", ... }

$ curl ipshaman.com/23.253.135.79/rdap
{"nir":null,"asn_registry":"arin", ... }
```

ipshaman also has a complete command-line utility with some special features!

Install the ipshaman CLI easily with: `pip install ipshaman`

```
$ ipshaman --help
usage: __init__.py [-h] [-s SERVER] [-l LOOKUP] [-g] [-r] [-i INPUT]
                   [-f FILTER] [--force] [-v]

ipshaman cli

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        ipshaman domain or IP to use (default: ipshaman.com)
  -l LOOKUP, --lookup LOOKUP
                        specify an IP address
  -g, --geo             perform a GeoIP lookup
  -r, --rdap            perform a RDAP lookup
  -i INPUT, --input INPUT
                        specify an input file containing IP addresses
  -f FILTER, --filter FILTER
                        filter incoming results (see documentation)
  --force               force input file to process
  -v, --version         displays the current version of ipshaman

$ ipshaman --lookup 23.253.135.79 --geo
{'country_code': 'US', 'country_code3': 'USA', ... }

$ ipshaman --lookup 23.253.135.79 --rdap
{'nir': None, 'asn_registry': 'arin', ... }

$ ipshaman --input ipshaman/inputs/list_of_ips_short.txt --geo
{'ip': '244.36.171.60', 'error': 'INVALID_IP'}
{'country_code': 'ES', 'country_code3': 'ESP', 'country_name': 'Spain', 'region': '58', ... }
{'country_code': 'NL', 'country_code3': 'NLD', 'country_name': 'Netherlands', 'region': '07', ... }
...

$ ipshaman --input ipshaman/inputs/list_of_ips_short.txt --geo --filter "country_code=US,region_name=Colorado"
{'country_code': 'US', 'country_code3': 'USA', 'country_name': 'United States', 'region': 'CO', ... }
{'country_code': 'US', 'country_code3': 'USA', 'country_name': 'United States', 'region': 'CO', ... }
```

ipshaman can also be used easily within Python code:

```python
>>> import ipshaman
>>> c = ipshaman.Client()
>>> c.geoip('23.253.135.79')
{'country_code': 'US', 'country_code3': 'USA', ... }
>>> c.rdap('23.253.135.79')                               
{'nir': None, 'asn_registry': 'arin', ... }
```

ipshaman also has a primitive web interface: http://ipshaman.com

![scrot](scrot.png)

## I want to run my own ipshaman server!

ipshaman has been tested with Debian 9.5, here's how to get up and running:

```
# apt-get update && apt-get install -y git
# git clone https://github.com/vesche/python_challenge
# cd python_challenge/ipshaman-server
# bash install.sh
```

Once installed, ipshaman can be administered using systemd:

```
$ sudo systemctl status ipshaman
 ipshaman.service - ipshaman
   Loaded: loaded (/lib/systemd/system/ipshaman.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2018-08-01 01:21:29 UTC; 20min ago
 Main PID: 9023 (python3.5)
    Tasks: 8 (limit: 4915)
   CGroup: /system.slice/ipshaman.service
           9023 /usr/bin/python3.5 /opt/ipshaman-server/server.py

Aug 01 01:21:29 debian systemd[1]: Stopped ipshaman.
Aug 01 01:21:29 debian systemd[1]: Started ipshaman.
Aug 01 01:21:30 debian python3.5[9023]: [2018-08-01 01:21:30 +0000] [9023] [INFO] Goin' Fast @ http://0.0.0.0:80
Aug 01 01:21:30 debian python3.5[9023]: [2018-08-01 01:21:30 +0000] [9023] [INFO] Starting worker [9023]
```

Keep in mind that the ipshaman command-line tool and client API will use [ipshaman.com](http://ipshaman.com) by default, so be sure to specify your own server like so:

```
$ ipshaman --server localhost:8000 --lookup 23.253.135.79 --geo
{"country_code":"US","country_code3":"USA", ... }
```

```python
>>> import ipshaman
>>> c = ipshaman.Client('localhost:8000')
>>> c.geoip('23.253.135.79')
{'country_code': 'US', 'country_code3': 'USA', ... }
```

Also, note that the server will host on `0.0.0.0:8000` by default.
