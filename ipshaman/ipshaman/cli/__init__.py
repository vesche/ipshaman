#!/usr/bin/env python

"""
ipshaman cli
"""

import argparse
import os
import re

from ipshaman import __version__
from ipshaman.cli import filt
from ipshaman.core import client


def get_parser():
    parser = argparse.ArgumentParser(description='ipshaman cli')
    parser.add_argument('-s', '--server',
                        help='ipshaman domain or IP to use (default: ipshaman.com)',
                        type=str)
    parser.add_argument('-l', '--lookup',
                        help='specify an IP address',
                        type=str)
    parser.add_argument('-g', '--geo',
                        help='perform a GeoIP lookup',
                        action='store_true')
    parser.add_argument('-r', '--rdap',
                        help='perform a RDAP lookup',
                        action='store_true')
    parser.add_argument('-i', '--input',
                        help='specify an input file containing IP addresses',
                        type=str)
    parser.add_argument('-f', '--filter',
                        help='filter incoming results (see documentation)',
                        type=str)
    parser.add_argument('--force',
                        help='force input file to process',
                        action='store_true')
    parser.add_argument('-v', '--version',
                        help='displays the current version of ipshaman',
                        action='store_true')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['version']:
        print(__version__)
        return
    
    if not (args['lookup'] or args['input']):
        parser.print_help()
        return

    if not (args['geo'] or args['rdap']):
        parser.print_help()
        return
    
    # parse filter syntax
    raw_filter = args['filter']
    filters = None
    if raw_filter:
        filters = filt.parse_filter(raw_filter)

    server = args['server']
    c = client.Client(server)
    
    if args['lookup']:
        ip = args['lookup']
        if args['geo']:
            results = c.geoip(ip)
        elif args['rdap']:
            results = c.rdap(ip)
        if filters:
            filter_results = filt.parse_data(results, filters)
            if filter_results:
                print(filter_results)
        else:
            print(results)
        return

    if args['input']:
        input_file = args['input']
        if not os.path.isfile(input_file):
            print("Error: Input file does not exist.")
            return

        ips = []
        with open(input_file) as f:
            for line in f.read().splitlines():
                ips += re.findall(r'[0-9]+(?:\.[0-9]+){3}', line)

        if (len(ips) > 300) and not args['force']:
            print("Error: Over 300 IP's in input file!")
            print("Please don't hurt ipshaman.com, but you can use the --force to ignore this.")
            return

        for ip in ips:
            if args['geo']:
                results = c.geoip(ip)
            elif args['rdap']:
                results = c.rdap(ip)
            if filters:
                filter_results = filt.parse_data(results, filters)
                if filter_results:
                    print(filter_results)
            else:
                print(results)


if __name__ == '__main__':
    main()
