
import requests


class Client:
    """The ipshaman API client.

    The client provides simplistic interaction with the ipshaman-server. It 
    can send requests to perform GeoIP and RDAP lookups on single and multiple
    IP addresses.
    """

    def __init__(self, server=None):
        self.server = server if server else 'http://ipshaman.com/'
        self.session = requests.session()

        if not self.server.startswith('http'):
            self.server = 'http://' + self.server
        if not self.server.endswith('/'):
            self.server += '/'
    
    def __repr__(self):
        return '<{cls}: {server}>'.format(
            cls=self.__class__.__name__,
            server=self.server
        )

    def geoip(self, ip):
        url = '{server}{ip}{uri}'.format(
            server=self.server,
            ip=ip,
            uri='/geo')
        r = self.session.get(url)
        return r.json()
    
    def rdap(self, ip):
        url = '{server}{ip}{uri}'.format(
            server=self.server,
            ip=ip,
            uri='/rdap')
        r = self.session.get(url)
        return r.json()