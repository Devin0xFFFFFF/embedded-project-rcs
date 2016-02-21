# embedded-project-rcs

bbb config

setup beaglebone black internet connection

on PC---
sudo su
#wlan0 is my internet facing interface, eth1 is the BeagleBone USB connection
ifconfig eth1 192.168.7.1
iptables --table nat --append POSTROUTING --out-interface wlan0 -j MASQUERADE
iptables --append FORWARD --in-interface eth1 -j ACCEPT
echo 1 > /proc/sys/net/ipv4/ip_forward
---

on beaglebone---
ifconfig usb0 192.168.7.2
route add default gw 192.168.7.1
------
