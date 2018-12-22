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
mixer.music.load('bbc.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(loops = -1)