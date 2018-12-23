
import RPi.GPIO as GPIO
from pygame import mixer
import time


def playMusic(url = '',decoLightsOn = 0):
    blinkRelay(2, 0.2, 6)
    # if decoLightsOn == 1 :
        # onRelay(3)
    mixer.init()
    mixer.music.load(url)
    mixer.music.set_volume(0.2)
    mixer.music.play(loops=0, start=0.0)
    while mixer.music.get_busy():
        time.sleep(1)


def startRelay():
    GPIO.setmode(GPIO.BCM)

    # init list with pin numbers

    pinList = [2, 3]

    # loop through pins and set mode and state to 'high'

    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)




def blinkRelay(pin, SleepTimeL = 2, count = 2):

    # time to sleep between operations in the main loop
    try:
        i = 1
        while i <= count:
            i += 1
            GPIO.output(pin, GPIO.LOW)
            time.sleep(SleepTimeL);
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(SleepTimeL);
        # GPIO.cleanup()
        print "Good bye!"

    # End program cleanly with keyboard
    except KeyboardInterrupt:
        print "  Quit"

        # Reset GPIO settings
        GPIO.cleanup()

def onRelay(pin):
    GPIO.output(pin, GPIO.LOW)

def offRelay(pin):
    GPIO.output(pin, GPIO.HIGH)


def cleanUpRelay():
    GPIO.cleanup()

startRelay()
playMusic('/home/pi/projects/stormyPython/farm-animals.mp3', 1)
playMusic('/home/pi/projects/stormyPython/silent-night.mp3')
playMusic('/home/pi/projects/stormyPython/noel.mp3')
playMusic('/home/pi/projects/stormyPython/we-three-kings.mp3')
cleanUpRelay()
