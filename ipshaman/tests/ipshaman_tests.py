#!/usr/bin/env python

import unittest

from ipshaman.core import client
from ipshaman.cli.filt import parse_filter, parse_data

c = client.Client()


class IpshamanTests(unittest.TestCase):

    def test_parse_filter(self):
        self.assertEqual(
            parse_filter("country_code=US,city=Boulder"),
            {"country_code":"US", "city":"Boulder"}
        )

    def test_parse_data(self):
        self.assertEqual(
            parse_data({'a':'b','c':'d'}, {'a':'b'}),
            {'a':'b','c':'d'}
        )
    
    def test_geoip_invalid(self):
        self.assertEqual(
            c.geoip('0.0.0.0')['error'],
            'INVALID_IP'
        )
    
    def test_geoip_valid(self):
        self.assertEqual(
            c.geoip('8.8.8.8')['latitude'],
            37.7509994507
        )

    def test_rdap_valid(self):
        self.assertEqual(
            c.rdap('8.8.8.8')['asn_description'],
            'GOOGLE - Google LLC, US'
        )


if __name__ == '__main__':
    unittest.main()