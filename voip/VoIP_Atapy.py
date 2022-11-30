import os
import RPi.GPIO as GPIO
import time
import json
#import linphone
import subprocess
import sys

BUTTON_PIN = 5
LED_PIN = 3
Led_status = 1
button = 0

def button_callback(channel):
	global button
	
	#print "before",button
	if os.system("linphonecsh status hook") == 16384:
		status = os.system("linphonecsh generic 'answer'")
	else:
		#button += 1
		#if button == 1:
			#print button
			#os.system("sudo /home/pi/linphone-desktop/OUTPUT/no-ui/bin/linphonecsh dial +66935815528")
	
		#if  button == 2 and os.system("sudo /home/pi/linphone-desktop/OUTPUT/no-ui/bin/linphonecsh dial +66935815528") == 8192 :
		if os.system("linphonecsh status hook") == 8192 or os.system("linphonecsh status hook") == 4096:
			#print button
			#os.system("sudo /home/pi/linphone-desktop/OUTPUT/no-ui/bin/linphonecsh generic terminate" )
			os.system("linphonecsh hangup")
			#os.system("aplay /home/pi/Desktop/phone-disconnect-1.wav > /dev/null")
			os.system("aplay /home/pi/Desktop/phone-hang-up-2b.wav > /dev/null")
			#button = 0
		else:
			os.system("linphonecsh dial somjai001")
	
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(BUTTON_PIN,GPIO.FALLING,callback=button_callback, bouncetime=500) # Setup event on pin 10 rising edge
#GPIO.add_event_detect(BUTTON_PIN,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 rising edge
os.system("linphonecsh generic 'autoanswer disable'")  	
#os.system("linphonecsh generic 'autoanswer enable'")
while True :
	#print "test"
	#txt = "call out ; sadqwsad"
	#x = txt.split(' ')[1]
	#x = json.load("call out")
	#print x
	#if (sudo)
	#status = os.system("linphonecsh status hook")
	#status = subprocess.call("linphonecsh status hook",shell=True)
	#print "status: ",str(status)
	#print (status)

	#p = subprocess.check_output(["linphonecsh status hook"])
	#p = subprocess.check_output('linphonecsh status hook')
	#p = subprocess.check_output('linphonecsh status hook',shell=True)
	process = subprocess.Popen(['linphonecsh', 'status' ,'hook'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	returncode = process.wait()
	#print process.stdout.read()
	if(os.system("linphonecsh status hook") != 0):
		value = process.stdout.read()
		status = value.split()
		print str(status)
		print len(status)
		if len(status) == 5:
			deaw = str(status[3]).strip(" \" ")
			#print deaw
			if deaw == "HW":
				time.sleep(2)
				os.system("linphonecsh generic 'answer'")
	#if os.system("linphonecsh status hook") == 16384:
		#time.sleep(5)
		#status = os.system("linphonecsh generic 'answer'")
	#if str(status) == "hook=on-hook":
		#button = 0
	#else :
		
	#	pass
		#button = 1
	#time.sleep(0.5)
