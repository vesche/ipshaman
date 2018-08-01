"""ipshaman-server utilities"""

import ipaddress


def validate_ip(ip):
    """Checks if an IP address is valid for lookup.
    
    Will return False if an IP address is reserved or invalid.
    Resource: https://en.wikipedia.org/wiki/Reserved_IP_addresses"""

    try:
        return not ipaddress.ip_address(ip).is_private
    except ValueError:
        return False
