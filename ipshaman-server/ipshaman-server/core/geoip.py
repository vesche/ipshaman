"""ipshaman-server GeoIP lookup"""

import GeoIP

from core import util
from core.constants import RESP_CODES


class GeoIPLookup:
    """
    Conducts a GeoIP lookup using a local database.

    Resource: https://dev.maxmind.com/geoip/geoip2/geolite2/
    """
    
    def __init__(self):
        self.geoip = GeoIP.open(
            '/usr/local/share/GeoIP/GeoLiteCity.dat',
            GeoIP.GEOIP_STANDARD
        )
    
    def lookup(self, ip):
        if not util.validate_ip(ip):
            return {'ip': ip, 'error': RESP_CODES[1]}

        data = self.geoip.record_by_name(ip)
        if not data:
            data['error'] = {'error': RESP_CODES[2]}

        data['ip'] = ip
        return data
