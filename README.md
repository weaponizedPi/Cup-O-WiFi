# Cup-O-WiFi
Cup-O-WiFi configuration files

This respository contains all the configuration files needed to perform the Cup-O-WiFi attack demo from CactusCon's 2018 talk "Weaponizing Your Pi". https://youtu.be/uuv68GX20R8?t=448 

The scripts were built in Kali 4.9.0-kali3-amd64 and ported to a RaspberryPi 3B with Kali linux. I did not spend alot of time creating them, they just needed to work for the demo, feel free to fix/break/upgrade.  

You will need the folloiwng installed: 

1. Python 2.7 
2. WifiPhisher
  - https://github.com/wifiphisher/wifiphisher 
  - apt-get install wifiphisher
3. Wireless Card - Alfa AWUS036NH

# Files
1. wifiPhisherAttack.py

   Main wrapper used in the attack to cycle the wifiphisher's ESSID/MAC every X second.  The ESSID.lst file needs to be present in the working directory during execution.  The script greps the stolen creds from wifiphisher's log file and then outputs to wifiphisherAttack.out.  I've commented as much as I can to help the learning process. 

2. ESSID.lst

   Contains a list of ESSIDs for wifiPhisherAttack.py to choose from, one ESSID per line.  

3. sso_login

   A Facebook/Gmail login portal I 'borrowed' from MathOverFlow.net's login page then customized with City of Phoenix emblem.  There are technically three pages for SSO_login: SSO.html, SSOf.html, and SSOm.html.  The SSO.html forwards to SSOf.html, which tells the user the creds they have entered are invalid.  SSOf.html then forwards to SSOm.html, which pops up a message saying the wireless is currently down. Nothing fancy. Place the directory in the 'wifiphisher/wifiphisher/data/phishing-pages/' directory. Add '-p sso_login' to the wifiphisher command use the payload. 
   
# Testing

To test that everything is configured correctly, use the following command: 

*wifiphisher/bin/wifiphsiher --noextensions --logging -e 'SomeESSID' -p sso_login*

Check to see if a AP named 'SomeESSID' is available and the SSO page comes up after connecting. If all works, then execute the wifiPhisherAttack.py wrapper with the ESSID.lst present in the same folder. *NOTE: Some Android Devices do not display the captive portal for SSO, to fix, request a non-cahced page such as test.com in the browser to get SSO to come up. Its a wifiPhisher issue.*

# RasPi Boot

I tried multiple ways to make the wrapper work at boot and the only stable and successful way to do it is by enabling auto-login to your Kali instance and adding a statup script for the user that does the following:

   *xfce4-terminal -x /path/to/wifiPhisherAttack.py*




