import requests
import json
import datetime
import os
from pygame import mixer

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
	mixer.init()
	mixer.music.load('/var/pythonFiles/stormyPython/1.mp3');
	mixer.music.play();
	while mixer.music.get_busy() == True:
		continue


