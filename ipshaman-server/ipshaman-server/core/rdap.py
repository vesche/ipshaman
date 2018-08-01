"""ipshaman-server RDAP lookup"""

from ipwhois import IPWhois
import warnings

from core import util
from core.constants import RESP_CODES


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
