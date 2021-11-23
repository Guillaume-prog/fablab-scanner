from PIL import Image
import ST7735 as TFT
import Adafruit_GPIO.SPI as SPI

class Screen:

    def __init__(self, cfg):
        self.sleep = True

        self.disp = TFT.ST7735(
            cfg["DC"],
            rst=cfg["RST"],
            spi=SPI.SpiDev(
                cfg["SPI_port"], 
                cfg["SPI_device"], 
                max_speed_hz=cfg["speed"]
            )
        )
        self.disp.begin()

        self.cfg = cfg

    def clear(self):
        image = Image.new('RGB', (self.cfg["width"], self.cfg["height"]), color=(255, 255, 255))
        self.disp.display(image)

    def display(self, path):
        bg = Image.new('RGB', (self.cfg["width"], self.cfg["height"]), color=(255, 255, 255))
        image = Image.open(path)
        bg.paste(image, (0, 16))
        self.disp.display(bg)

    def display_code(self, uid):
        pass # show qrcode

    def display_message(self, msg, timeout):
        pass # show message for timeout duration
    
    
    def sleep(self, path):
        # if sleep
        logo = Image.open(path)
        x_size, y_size = int(self.cfg["width"] // 2.5), int(self.cfg["height"] // 3)
        x, y = int((self.cfg["width"] - x_size) // 2), int((self.cfg["height"] - x_size) // 2)
        x_speed, y_speed = 2, 2
        logo = logo.resize((x_size, y_size))
        

        while True:
            bg = Image.new('RGB', (self.cfg["width"], self.cfg["height"]), color=(255, 255, 255))
            x += x_speed
            y += y_speed
            if(x + x_size >= self.cfg["width"] or x <= 0):
                x_speed = -x_speed
            
            if(y + y_size >= self.cfg["height"] or y <= 0):
                y_speed = -y_speed
            
            bg.paste(logo, (int(x), int(y)))
            self.disp.display(bg)