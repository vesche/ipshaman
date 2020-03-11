import requests


class Client:
    """
    The ipshaman API client.

    The client provides simplistic interaction with the ipshaman-server. It 
    can send requests to perform lookups on single IP addresses.
    """

    def __init__(self, server=None):
        self.server = server or 'http://ipshaman.com/'
        self.session = requests.session()

        if not self.server.startswith('http'):
            self.server = 'http://' + self.server
        if not self.server.endswith('/'):
            self.server += '/'
    
    def __repr__(self):
        return f'<ipshaman {self.__class__.__name__}: {self.server}>'

    def lookup(self, ip):
        response = self.session.get(self.server + ip)
        return response.json()
