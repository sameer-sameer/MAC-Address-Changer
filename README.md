# MAC-Address-Changer
A Python script to change MAC addresses on Kali Linux


cd Downloads
git clone https://github.com/sameer-sameer/MAC-Address-Changer.git
cd Downloads/MAC-Address-Changer/MAC-Address-Changer
ifconfig <check your interface and ether >
sudo python mac_changer.py -i <interface> -m <new_mac_address>
#example sudo python mac_changer.py -i eth0 -m 00:11:22:33:44:55:66
ifconfig <check your mac address is changed>
