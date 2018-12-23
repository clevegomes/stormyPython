
import RPi.GPIO as GPIO
from pygame import mixer
import time


def playMusic(url = ''):
    mixer.init()
    mixer.music.load(url)
    mixer.music.set_volume(0.2)
    mixer.music.play(loops=0, start=0.0)
    while mixer.music.get_busy():
        time.sleep(1)


def startRelay():
    GPIO.setmode(GPIO.BCM)

    # init list with pin numbers

    pinList = [2, 3, 4, 17]

    # loop through pins and set mode and state to 'high'

    for i in pinList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

    # time to sleep between operations in the main loop

    SleepTimeL = 2

    try:
        GPIO.output(2, GPIO.LOW)
        print "ONE"
        time.sleep(SleepTimeL);
        GPIO.output(3, GPIO.LOW)
        print "TWO"
        time.sleep(SleepTimeL);
        GPIO.output(4, GPIO.LOW)
        print "THREE"
        time.sleep(SleepTimeL);
        GPIO.output(17, GPIO.LOW)
        print "FOUR"
        time.sleep(SleepTimeL);
        GPIO.cleanup()
        print "Good bye!"

    # End program cleanly with keyboard
    except KeyboardInterrupt:
        print "  Quit"

        # Reset GPIO settings
        GPIO.cleanup()

# startRelay()
playMusic('/home/pi/projects/stormyPython/farm-animals.mp3')
playMusic('/home/pi/projects/stormyPython/silent-night.mp3')
playMusic('/home/pi/projects/stormyPython/noel.mp3')
playMusic('/home/pi/projects/stormyPython/we-three-kings.mp3')

