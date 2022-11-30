import time
import json
import datetime
import os

#from numpy as np
#from paho.mqtt import client as mqtt_client
#from bluepy import btle
import paho.mqtt.client as mqtt_client
from bluepy.btle import Scanner, DefaultDelegate 

broker = '124.156.247.198'
port = 1883
topic = "IOT/lab/station0028/"
client_id ='station0028'
username = 'station0028'
password = '8G+<*xV(C"YjUvJw'

sookjai = '415054'

#print(os.system("python --version"))

class ScanDelegate(DefaultDelegate):
	def __init__(self):
		DefaultDelegate.__init__(self)

	def handleDiscovery(self, dev, isNewDev, isNewData):
		if isNewDev:
			pass
			#print "Discovered device", dev.addr
		elif isNewData:
			pass
			#print "Received new data from", dev.addr



def connect_mqtt():
	def on_connect(client, userdata, flags, rc):
		if rc == 0:
			print("Connected to MQTT Broker!")
		else:
			print("Failed to connect, return code %d\n", rc)
   
	def on_disconnect(clinet, userdata, flags, rc):
			pass
	#Set Connecting Client ID
	client = mqtt_client.Client(client_id)
	client.username_pw_set(username, password)
	client.on_connect = on_connect
	client.on_disconnet = on_disconnect
	client.connect(broker, port)
	return client


def main():
	scanner = Scanner().withDelegate(ScanDelegate())
	#devices = scanner.scan(10.0)

	client = connect_mqtt()
	client.loop_start()
	while True:
		devices = scanner.scan(1.0)
		for dev in devices:
			for(adtype, desc, value) in dev.getScanData():
				if((adtype == 22) and (desc == '16b Service Data')):
					#print("%s"% value[8:14])
					if(value[8:14] == sookjai):
						instance = value[8:]

						activity = int(instance[1],16)
						battery = int(instance[30:32],16)
						device_id = int(instance[14:20],16)
						count = int(instance[20:24],16)
						rssi = dev.rssi

						#print("%s%d %s %s %d %s"%(instance,dev.rssi,battery,device_id,count,value[28:32])) 
						msg = "tencent" + ",d=" + str(device_id) + ",c=" +str(count) + ",t=T " + "m=0" + ",b=" + str(battery) + ",r=" + str(rssi) + ",a=0,v=0,f=0"
						print(msg)

						client.publish(topic,msg)

if __name__ == "__main__":
	main()
