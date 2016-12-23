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



now = datetime.datetime.now().time()

#print(now)
# Silence mode on after midnight till 7am .I am subtracting 4 to 7 since the time is in utc  and we are 4 hr ahead  and checking midnight for 20 again since we are 4 hr ahead
#if now <= datetime.time((7-4),00) or now >= datetime.time(20,00):
#    exit()


cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('user-agent','Mozilla/5.0')]


def shellQuote(s):
    return "'" + s.replace("'", "'\\''") + "'"

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
                if cnt <= 10:
                    news = news +  unicode(description,"ascii")  + "  "
                     
        except Exception, e:
            return  str(e)


    except Exception, e:
        return str(e)

    return news



def localSensors():
    r = requests.get('http://52.25.60.112/localsensors/rest.php')
    jdata = r.json();
    #data = json.load(r.json())
    systemdTime =datetime.datetime.utcnow()
    serverdTime = datetime.datetime.strptime(jdata["tstamp"], "%Y-%m-%d %H:%M:%S")



    difference =  systemdTime- serverdTime ;
	
    # check if the local reading are not more than 10 min old
    cutoffTime = 100000*60;
    localSensorReading = ""
    if difference.total_seconds() <= cutoffTime:
        localSensorReading = " Local sensor readings. Your local room temperature  is recorded at " +jdata["t"]+" degrees celsius,local humidity recorded at "+jdata["h"]+" percent and local pressure recorded at "+jdata["p"]+" millibars"
        

    return localSensorReading







    	


news = newsFeed()
sensors = localSensors()

#print(sensors)
#exit()
textToSpeach = shellQuote(news + "  " + sensors)
#textToSpeach = sensors


mixer.init()
mixer.music.load('bbc.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(loops = -1)


os.system("./tts.sh "+ textToSpeach + " > file.log 2>&1")
mixer.music.fadeout(2000)
time.sleep(3)


#while mixer.music.get_busy() == True:
#    continue











