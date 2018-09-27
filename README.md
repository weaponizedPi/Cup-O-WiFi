# Cup-O-WiFi
Cup-O-WiFi configuration files

This respository contains all the configuration files needed to perform the Cup-O-WiFi attack demo from Cactus Cons 2018 talk "Weaponizing Your Pi".  The scripts were all built in Kali 4.9.0-kali3-amd64 and ported to a RaspberryPi 3B with Kali linux. You will need the folloiwng installed: 

Python 2.7
WifiPhisher 
Wireless Card 

#Files
-wifiPhisherAttack.py - Main wrapper used in the attack to cycle the wifiphisher's ESSID/MAC every X seconds
-ESSID.lst - Contains a list of ESSIDs for wifiPhisherAttack.py to choose from. 
-sso_long - A custom Facebook/Gmail login portal, customized with City of Phoenix emblem. 

