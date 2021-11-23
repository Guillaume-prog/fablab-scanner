from PIL import Image
import tft_screen.config as cfg
import ST7735 as TFT
import Adafruit_GPIO.SPI as SPI   
import time

def initScreen():
    disp = TFT.ST7735(
    cfg.screenconfig["DC"],
    rst=cfg.screenconfig["RST"],
    spi=SPI.SpiDev(cfg.screenconfig["SPI_port"], cfg.screenconfig["SPI_device"], max_speed_hz=cfg.screenconfig["speed"]))
    return disp

def clearScreen(disp):
    image = Image.new('RGB', (cfg.screenconfig["width"], cfg.screenconfig["height"]), color=(255, 255, 255))
    disp.display(image)

def displayImage(disp, path):
    bg = Image.new('RGB', (cfg.screenconfig["width"], cfg.screenconfig["height"]), color=(255, 255, 255))
    image = Image.open(path)
    bg.paste(image, (0, 16))
    disp.display(bg)
  
  
def runSleepMode(disp, path):
    logo = Image.open(path)
    x_size, y_size = int(cfg.screenconfig["width"] // 2.5), int(cfg.screenconfig["height"] // 3)
    x, y = int((cfg.screenconfig["width"] - x_size) // 2), int((cfg.screenconfig["height"] - x_size) // 2)
    x_speed, y_speed = 2, 2
    logo = logo.resize((x_size, y_size))
    

    while True:
        bg = Image.new('RGB', (cfg.screenconfig["width"], cfg.screenconfig["height"]), color=(255, 255, 255))
        x += x_speed
        y += y_speed
        if(x + x_size >= cfg.screenconfig["width"] or x <= 0):
            x_speed = -x_speed
        
        if(y + y_size >= cfg.screenconfig["height"] or y <= 0):
            y_speed = -y_speed
        
        bg.paste(logo, (int(x), int(y)))
        disp.display(bg)