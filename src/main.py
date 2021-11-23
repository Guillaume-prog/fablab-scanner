from rfid.rfid import initRFID, readRFID
from tft_screen.screen import clearScreen, displayImage, initScreen, runSleepMode
import multiprocessing
import time

def main():
    # init rfid
    rc522 = initRFID()
    
    # init screen
    st7735 = initScreen()
    st7735.begin()
    clearScreen(st7735)
    
    # sleep_process.terminate()
    
    while True:
        # run sleep mode
        sleep_process = multiprocessing.Process(target=runSleepMode, args=(st7735, 'src/tft_screen/assets/logo_ups_square'))
        sleep_process.start()
        
        # wait for rfid
        while True:
            uid = readRFID(rc522)
            if uid != None:
                sleep_process.terminate()
                break
        
        clearScreen(st7735)
        displayImage(st7735, 'src/tft_screen/assets/test_qrcode.png')
        
        print("end")
        break
    
if __name__ == "__main__":
    main()