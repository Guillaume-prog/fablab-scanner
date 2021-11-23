from PIL import Image
import ST7735 as TFT
import Adafruit_GPIO.SPI as SPI

class Screen:

    def __init__(self, cfg):
        self.disp = TFT.ST7735(
            cfg.screenconfig["DC"],
            rst=cfg.screenconfig["RST"],
            spi=SPI.SpiDev(
                cfg.screenconfig["SPI_port"], 
                cfg.screenconfig["SPI_device"], 
                max_speed_hz=cfg.screenconfig["speed"]
            )
        )
        self.disp.begin()

        self.cfg = cfg

    def clear(self):
        image = Image.new('RGB', (self.cfg.screenconfig["width"], self.cfg.screenconfig["height"]), color=(255, 255, 255))
        self.disp.display(image)

    def display(self, path):
        bg = Image.new('RGB', (self.cfg.screenconfig["width"], self.cfg.screenconfig["height"]), color=(255, 255, 255))
        image = Image.open(path)
        bg.paste(image, (0, 16))
        self.disp.display(bg)
    
    
    def sleep(self, path):
        logo = Image.open(path)
        x_size, y_size = int(self.cfg.screenconfig["width"] // 2.5), int(self.cfg.screenconfig["height"] // 3)
        x, y = int((self.cfg.screenconfig["width"] - x_size) // 2), int((self.cfg.screenconfig["height"] - x_size) // 2)
        x_speed, y_speed = 2, 2
        logo = logo.resize((x_size, y_size))
        

        while True:
            bg = Image.new('RGB', (self.cfg.screenconfig["width"], self.cfg.screenconfig["height"]), color=(255, 255, 255))
            x += x_speed
            y += y_speed
            if(x + x_size >= self.cfg.screenconfig["width"] or x <= 0):
                x_speed = -x_speed
            
            if(y + y_size >= self.cfg.screenconfig["height"] or y <= 0):
                y_speed = -y_speed
            
            bg.paste(logo, (int(x), int(y)))
            self.disp.display(bg)