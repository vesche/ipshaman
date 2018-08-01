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
        self.g = GeoIP.open("/usr/local/share/GeoIP/GeoLiteCity.dat",
            GeoIP.GEOIP_STANDARD)
    
    def lookup(self, ip):
        if not util.validate_ip(ip):
            return { 'ip': ip, 'error': RESP_CODES[1] }

        data = self.g.record_by_name(ip)
        if data:
            return data
        else:
            return { 'ip': ip, 'error': RESP_CODES[2] }
