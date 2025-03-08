#!/usr/bin/env python

import subprocess
import optparse

def get_argumnts():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change itc MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="NEW MAC address")
    (option, arguments) = parser.parse_args()
    if not option.interface:
        parser.error("[-] Plzz specify an interface, use --help for more information")
    elif not option.new_mac:
        parser.error("[-] Plzz specify a new mac, use --help for more information")
    return option

def change_mac(interface, new_mac):
    print("[+] changing mac address for " + interface + "to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

option = get_argumnts()
change_mac(option.interface,option.new_mac)