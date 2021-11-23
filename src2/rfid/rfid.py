import RPi.GPIO as GPIO
from pirc522 import RFID
import time

def initRFID():
    GPIO.setwarnings(False)
    return RFID(bus=1, device=0, pin_rst=25, pin_mode=GPIO.BCM, pin_ce=18)

def readRFID(rc522):
    rc522.wait_for_tag()
    (error, tag_type) = rc522.request()
    if not error:
        (error, uid) = rc522.anticoll()
        if not error:
            time.sleep(2)
            return uid