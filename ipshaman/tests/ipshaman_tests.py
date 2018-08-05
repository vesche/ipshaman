#!/usr/bin/env python

import unittest

from ipshaman.core import client

c = client.Client()


class IpshamanTests(unittest.TestCase):

    def test_geoip_invalid(self):
        self.assertEqual(
            c.lookup('0.0.0.0')['error'],
            'INVALID_IP'
        )
    
    def test_geoip_valid(self):
        self.assertEqual(
            c.lookup('8.8.8.8')['latitude'],
            37.7509994507
        )


if __name__ == '__main__':
    unittest.main()