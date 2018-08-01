"""ipshaman-server utilities"""

import ipaddress


def validate_ip(ip):
    """Checks if an IP address is valid"""
    try:
        if ipaddress.ip_address(ip).is_private:
            return False
    except ValueError:
        return False

    return True