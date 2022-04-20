#!/usr/bin/env python3

from scapy.all import *


def ISAKMPparser(pkt):
    # IKEv1 has ISAKMP_payload_SA and IKEv2 ISAKMP_payload
    if pkt[IKEv2].version == 0x10:
        # Decode pkt IKEv2 to IKEv1
        pkt[UDP].decode_payload_as(ISAKMP)
        if (pkt.haslayer(ISAKMP_payload_SA)):
            print("{} -> {}".format(pkt[IP].src, pkt[IP].dst))
            pkt[ISAKMP_payload_SA][ISAKMP_payload_Proposal].show()
    elif pkt[IKEv2].version == 0x20:
        if pkt.haslayer(IKEv2) and pkt.haslayer(IKEv2_payload_Transform):
            print("{} -> {}".format(pkt[IP].src, pkt[IP].dst))
            pkt[IKEv2_payload_Transform].show()

load_contrib("ikev2")
print("[*] Starting sniffing...")
sniff(filter='udp and (dst port 500)', iface='eth0', prn=ISAKMPparser)

