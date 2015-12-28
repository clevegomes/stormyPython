import requests
import json
import datetime
import os
#import pygame

r = requests.get('http://52.25.60.112/localsensors/rest.php')
jdata = r.json();
#data = json.load(r.json())
systemdTime =datetime.datetime.utcnow()
serverdTime = datetime.datetime.strptime(jdata["tstamp"], "%Y-%m-%d %H:%M:%S")


difference =  systemdTime- serverdTime ;
cutoffTime = 30*60;

if difference.total_seconds() <= cutoffTime:
	print(systemdTime)
	print(serverdTime)
	print(difference.total_seconds())
	os.startfile('C:/Users/Developer1/Downloads/sms_sms.mp3')
	#pygame.mixer.init()
	#pygame.mixer.music.load("C:/Users/Developer1/Downloads/sms_sms.mp3")
	#pygame.mixer.music.play()
	#while pygame.mixer.music.get_busy() == True:
	#	continue


