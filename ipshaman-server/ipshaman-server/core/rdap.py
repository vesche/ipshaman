"""ipshaman-server RDAP lookup"""

import requests

from core import util
from core.constants import RESP_CODES


class RDAPLookup:
    """
    Conducts an RDAP query based on the recommended method by ARIN.

    Resource: https://www.arin.net/resources/rdap.html
    """
    
    def __init__(self):
        self.url = 'http://rdap.arin.net/registry/ip/'
        self.session = requests.session()

    def lookup(self, ip):
        if not util.validate_ip(ip):
            return {'ip': ip, 'error': RESP_CODES[1]}
        
        response = self.session.get(self.url + ip)
        return response.json()


"""
from ipwhois import IPWhois
import warnings

class RDAPLookup:
    
    def __init__(self):
        pass

    def lookup(self, ip):
        if not util.validate_ip(ip):
            return { 'ip': ip, 'error': RESP_CODES[1] }
        
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning)
            i = IPWhois(ip)
            data = i.lookup_rdap(depth=1)

        if data:
            return data
        else:
            return { 'ip': ip, 'error': RESP_CODES[2] }
"""