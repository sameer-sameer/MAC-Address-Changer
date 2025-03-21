#!/usr/bin/env python

import subprocess
import argparse
import re


def get_arguments():
    parser = argparse.ArgumentParser(description="Change MAC Address of a Network Interface")
    parser.add_argument("-i", "--interface", dest="interface", required=True,
                        help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="New MAC address")

    return parser.parse_args()


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
        mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

        if mac_address_search:
            return mac_address_search.group(0)
        else:
            print("[-] Could not read MAC address.")
            return None
    except subprocess.CalledProcessError:
        print(f"[-] Error: Unable to fetch MAC address for {interface}. Ensure the interface exists.")
        return None


# Get user input
options = get_arguments()
current_mac = get_current_mac(options.interface)

if current_mac:
    print(f"Current MAC = {current_mac}")

    change_mac(options.interface, options.new_mac)

    new_mac = get_current_mac(options.interface)

    if new_mac == options.new_mac:
        print(f"[+] MAC address was successfully changed to {new_mac}")
    else:
        print("[-] MAC address did not get changed.")
