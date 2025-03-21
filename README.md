# MAC-Address-Changer
A Python script to change MAC addresses on Kali Linux

Linux commands:
cd Downloads

git clone https://github.com/sameer-sameer/MAC-Address-Changer.git

cd Downloads/MAC-Address-Changer/MAC-Address-Changer

ifconfig <check your interface and ether >

sudo python mac_changer.py -i <interface> -m <new_mac_address>

#examples:

for eth0

sudo python mac_changer.py -i eth0 -m 00:11:22:33:44:55:66

sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55:66

for wlan0

sudo python mac_changer.py -i wlan0 -m 00:11:22:33:44:55:66

sudo python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55:66

ifconfig <check your mac address is changed>
