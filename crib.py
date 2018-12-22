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



mixer.init()
mixer.music.load('farm-animals.mp3')
mixer.music.set_volume(0.7)
mixer.music.play(loops=0, start=0.0)
# mixer.music.fadeout(9000)
# time.sleep(9)
while pygame.mixer.music.get_busy():
    time.sleep(1)