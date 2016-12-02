#!/usr/bin/env python

import sys
import argparse

from scapy.all import *

def modify_path(replace_ip=None, hops=0):

    count = {}

    def send_valid_reply(src_ip=None, dst_ip=None, icmp_id=None, icmp_seq=None):
        ip = IPv6(src=src_ip, dst=dst_ip)
        icmpv6 = ICMPv6EchoReply(id=icmp_id, seq=icmp_seq)

        p = ip/icmpv6
        send(p)

        return

    def send_time_exceed(src_ip=None, dst_ip=None, replace_ip=None, icmp_id=None,
icmp_seq=None):

        ip = IPv6(src=replace_ip,dst=dst_ip)
        exceed = ICMPv6TimeExceeded(code=0)
        ip_in_icmp = IPv6(src=dst_ip, dst=src_ip, plen=64)
        echo_request = ICMPv6EchoRequest(id=icmp_id, seq=icmp_seq)

        p = ip/exceed/ip_in_icmp/echo_request

        send(p)

        return 

    def get_packet(p):

        orig_src_ip = p[IPv6].src
        orig_dst_ip = p[IPv6].dst
        icmp_id = p[ICMPv6EchoRequest].id
        icmp_seq = p[ICMPv6EchoRequest].seq

        if not orig_src_ip in count:
            count[orig_src_ip] = 0

        if count[orig_src_ip] == hops:
            count[orig_src_ip] = 0
            send_valid_reply(orig_dst_ip, orig_src_ip, icmp_id, icmp_seq)
        else:
            send_time_exceed(orig_dst_ip, orig_src_ip, replace_ip, icmp_id, icmp_seq)
            count[orig_src_ip]+=1

    return get_packet

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--iface', help='interface')
    parser.add_argument('-r', '--replace', help='ip for path modifier')
    parser.add_argument('-o', '--hops', help='hops to add', default=17)
    args = parser.parse_args()
    
    if args.iface and args.replace:
        iface = args.iface
        replace_ip = args.replace
        hops = args.hops
    else:
        parser.print_help()
        sys.exit()


    sniff(iface=iface, filter="icmp6 and ip6[40] == 128",
prn=modify_path(replace_ip, hops))
