
import requests


class Client:
    """The ipshaman API client.

    The client provides simplistic interaction with the ipshaman-server. It 
    can send requests to perform lookups on single IP addresses.
    """

    def __init__(self, server=None):
        self.server = server if server else 'http://ipshaman.com/'
        self.session = requests.session()

        if not self.server.startswith('http'):
            self.server = 'http://' + self.server
        if not self.server.endswith('/'):
            self.server += '/'
    
    def __repr__(self):
        return '<ipshaman {cls}: {server}>'.format(
            cls=self.__class__.__name__,
            server=self.server
        )

    def lookup(self, ip):
        url = '{server}{ip}'.format(
            server=self.server,
            ip=ip)
        r = self.session.get(url)
        return r.json()
