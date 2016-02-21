# embedded-project-rcs

bbb config

setup beaglebone black internet connection

PC config
$sudo su
#wlan0 is my internet facing interface, eth1 is the BeagleBone USB connection
$ifconfig eth1 192.168.7.1
$iptables --table nat --append POSTROUTING --out-interface wlan0 -j MASQUERADE
$iptables --append FORWARD --in-interface eth1 -j ACCEPT
$echo 1 > /proc/sys/net/ipv4/ip_forward


config on beaglebone
$ifconfig usb0 192.168.7.2
$route add default gw 192.168.7.1
$echo "nameserver 8.8.8.8" >> /etc/resolv.conf

To Get USBee connected via USB to Windows:

Download Pulseview and Sigrok:
http://sigrok.org/wiki/Downloads

Then run Zadig to get drivers:
Device specific USB driver
The device specific USB driver shipped with the vendor software is not going to work in almost all cases. You will need to install the WinUSB driver.
For installing the WinUSB driver you can use the Zadig executable from the libwdi project. There are two versions, one for Windows XP (zadig_xp.exe), and another one for all other (Vista or higher) supported Windows versions (zadig.exe). Both 32 and 64 bit Windows versions are supported. The sigrok-cli and PulseView installers ship with both Zadig executable files for convenience and they're available from the Windows "Start" menu (the Zadig *.exe files themselves are located in the installation directory of the respective application).
If you already installed the vendor driver previously, you need to run Zadig and switch to the WinUSB driver (see above). There's no need to uninstall or deactivate the vendor driver manually, Zadig will handle all of this.
See also the Zadig wiki page for more information.
