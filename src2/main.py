from rfid.rfid import initRFID, readRFID

from tft_screen import Screen
from tft_screen.config import cfg as screen_cfg

from configparser import ConfigParser

import multiprocessing
import time

def main():

    config = ConfigParser()
    config.read('./config/config.ini')

    # init rfid
    rc522 = initRFID()
    
    # init screen
    screen = Screen(config["SCREEN"])
    screen.clear()
    
    # sleep_process.terminate()
    
    while True:
        # run sleep mode
        sleep_process = multiprocessing.Process(target=screen.sleep, args=('src/tft_screen/assets/logo_ups_square'))
        sleep_process.start()
        
        # wait for rfid
        while True:
            uid = readRFID(rc522)
            if uid != None:
                sleep_process.terminate()
                break
        
        screen.clear()
        screen.display('src/tft_screen/assets/test_qrcode.png')
        
        print("end")
        break
    
if __name__ == "__main__":
    main()