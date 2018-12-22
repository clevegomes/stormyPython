
from pygame import mixer
import time



mixer.init()
mixer.music.load('~/projects/stormyPython/crib.pyfarm-animals.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(loops=0, start=0.0)
while mixer.music.get_busy():
    time.sleep(1)

mixer.music.load('~/projects/stormyPython/crib.pysilent-night.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(loops=0, start=0.0)
while mixer.music.get_busy():
    time.sleep(1)

mixer.music.load('~/projects/stormyPython/crib.pynoel.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(loops=0, start=0.0)
while mixer.music.get_busy():
    time.sleep(1)

mixer.music.load('~/projects/stormyPython/crib.pywe-three-kings.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(loops=0, start=0.0)
while mixer.music.get_busy():
    time.sleep(1)