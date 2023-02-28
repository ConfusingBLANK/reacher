import ipaddress
import argparse

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def identify_unreachable_cidr(cidr_file, ip_file):
    cidr_list = read_file(cidr_file)
    reachable_ips = read_file(ip_file)
    unreachable_cidr = []
    for cidr in cidr_list:
        network = ipaddress.ip_network(cidr, strict=False)
        for ip in reachable_ips:
            if ipaddress.ip_address(ip) in network:
                break
        else:
            unreachable_cidr.append(cidr)
    return unreachable_cidr

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Identify unreachable CIDR networks.')
    parser.add_argument('cidr_file', metavar='cidr_file', type=str,
                        help='The file containing the list of CIDR networks')
    parser.add_argument('ip_file', metavar='ip_file', type=str,
                        help='The file containing the list of reachable IP addresses')
    args = parser.parse_args()

    unreachable_cidr = identify_unreachable_cidr(args.cidr_file, args.ip_file)
    print("Non reachable networks")
    for cidr in unreachable_cidr:
        print(cidr)
