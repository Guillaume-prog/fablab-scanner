#!/bin/bash
sudo pip3 install bottle

cd ~
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.70.tar.gz
tar xvfz bcm2835-1.70.tar.gz
cd bcm2835-1.70/
./configure 
make
sudo make install

sudo pip3 install pi-rc522

pip install pillow
pip install qrcode

sudo pip3 install Adafruit_GPIO
git clone https://github.com/cskau/Python_ST7735
cd Python_ST7735
sudo python3 setup.py install

sudo apt install mariadb-server