
from pygame import mixer
import time



mixer.init()
mixer.music.load('farm-animals.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(loops=0, start=0.0)
while mixer.music.get_busy():
    time.sleep(1)

mixer.music.load('silent-night.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(loops=0, start=0.0)
while mixer.music.get_busy():
    time.sleep(1)

mixer.music.load('noel.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(loops=0, start=0.0)
while mixer.music.get_busy():
    time.sleep(1)

mixer.music.load('we-three-kings.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(loops=0, start=0.0)
while mixer.music.get_busy():
    time.sleep(1)