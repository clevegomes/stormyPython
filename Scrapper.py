import requests
import json
import datetime
import os
from pygame import mixer
import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time
import sys




cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('user-agent','Mozilla/5.0')]



def newsFeed():
    news = ""
    try:
        page = "http://feeds.bbci.co.uk/news/world/rss.xml"
        sourceCode = opener.open(page).read()

        try:
            descriptions = re.findall(r'<description>(.*?)</description>',sourceCode)
            cnt = 0;
            for description in descriptions:
                cnt += 1
                if cnt <= 3:
                    news = news +  unicode(description,"ascii")  + "  "

        except Exception, e:
            return  str(e)


    except Exception, e:
        return str(e)



def localSensors():
    r = requests.get('http://52.25.60.112/localsensors/rest.php')
    jdata = r.json();
    #data = json.load(r.json())
    systemdTime =datetime.datetime.utcnow()
    serverdTime = datetime.datetime.strptime(jdata["tstamp"], "%Y-%m-%d %H:%M:%S")



    difference =  systemdTime- serverdTime ;

    cutoffTime = 30*60;
    localSensorReading = ""
    if difference.total_seconds() <= cutoffTime:
        localSensorReading = "Local sensor reading.Your local room temperature sensor reading is recorded at " +jdata["t"]+" degrees celsius,local humidity recorded at "+jdata["h"]+" percent and local pressure recorded at "+jdata["p"]+" millibars"
        

    return localSensorReading







    	


news = newsFeed()
sensors = localSensors()

textToSpeach = sensors

os.system("/var/pythonFiles/stormyPython/tts.sh "+ textToSpeach + " > file.log 2>&1")

mixer.init()
mixer.music.load('/var/pythonFiles/stormyPython/bbc.mp3')
mixer.music.set_volume(0.3)
mixer.music.play();
while mixer.music.get_busy() == True:
    continue











