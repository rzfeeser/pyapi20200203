#!/usr/bin/python3
"""Russell Zachary Feeser -- exploring argument parsing"""

# standard library imports
import argparse

def server(port):
    x = f"Your choice was server and it will run on port {port}"
    return x

def client(port):
    x = f"Your choice was client and it will run on port {port}"
    return x

if __name__ == "__main__":
    # yankeedoodle = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description="send and receive UDP locally")
    parser.add_argument('role', choices=[client, server], nargs='?', default=server, help="which role to play")
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port (default 1060)')
    args = parser.parse_args()
    # print(f"THE CURRENT VALUE OF args.role is {args.role}")
    # print(f"THE CURRENT VALUE OF args.p is {args.p}")
    #function = yankeedoodle[args.role]
    print(args.role(args.p))
