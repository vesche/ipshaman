#!/usr/bin/env python

"""
ipshaman cli
"""

import argparse
import os
import re

from ipshaman import __version__
from ipshaman.core import client


def get_parser():
    parser = argparse.ArgumentParser(description='ipshaman cli')
    parser.add_argument('-s', '--server',
                        help='ipshaman domain or IP to use (default: ipshaman.com)',
                        type=str)
    parser.add_argument('-l', '--lookup',
                        help='specify an IP address',
                        type=str)
    parser.add_argument('-i', '--input',
                        help='specify an input file containing IP addresses',
                        type=str)
    parser.add_argument('-f', '--force',
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

    server = args['server']
    c = client.Client(server)
    
    if args['lookup']:
        ip = args['lookup']
        results = c.lookup(ip)
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

        if len(ips) > 100 and not args['force']:
            print("Error: Over 100 IP's in input file!")
            print("       Please don't hurt ipshaman.com...")
            print("       However, you can use --force to ignore this.")
            return

        for ip in ips:
            results = c.lookup(ip)
            print(results)


if __name__ == '__main__':
    main()
