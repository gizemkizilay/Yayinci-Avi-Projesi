from scapy.all import *
from datetime import datetime

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{time_stamp}] Trafik: {ip_src} -> {ip_dst}\n"
        print(log_entry)
        with open("trafik_log.txt", "a") as log_file:
            log_file.write(log_entry)

sniff(iface="eth0", filter="tcp port 1935 or tcp port 443 or udp port 443", prn=packet_callback, store=0)
