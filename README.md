# OS
## RASPBERRY OS
Install Raspberry Pi OS Lite  

## SPI
Activate SPI on Raspberry Pi:
- Use this command:  
```sudo raspi-config``` 

- Then, choose these options:  
```Interfacing Options``` > ```SPI``` > ```Yes``` > ```Finish```

# LIBRARIES
## bottle library
Use these command:  
```sudo pip3 install bottle```   

## bcm2835 library
Use these commands:  
```cd ~```  
```wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.70.tar.gz```  
```tar xvfz bcm2835-1.70.tar.gz```  
```cd bcm2835-1.70/```  
```./configure ```  
```make```  
```sudo make install```  
  
## pi-rc522 library 
Use this command:  
```sudo pip3 install pi-rc522```

## qrcode library  
Use these commands:  
- ```pip install pillow```  
- ```pip install qrcode```

## ST7735 library
Use these commands:  
- ```sudo pip3 install Adafruit_GPIO```  
- ```git clone https://github.com/cskau/Python_ST7735```  
- ```cd Python_ST7735```  
- ```sudo python3 setup.py install```  

# MARIA-DB
## install maria-db
Use this command:  
```sudo apt install mariadb-server``` 

## setup maria-db
### root access
Use this command:  
```sudo mysql_secure_installation``` 

Then choose these options:  
```enter``` > ```Yes``` > ```<password>``` > ```<re-password>``` > ```Yes``` > ```Yes``` > ```Yes``` > ```Yes```  
(ici, mdp : fablabscanner) 

### root connection
Use this command:  
- ```sudo mysql -uroot -p``` 

### admin and database creation
Use thes commands:  
- ```CREATE DATABASE <database_name>;```  
(ici, database_name : id_db)  

- ```CREATE USER '<username>'@'localhost' IDENTIFIED BY '<password>'```  
(ici, username : admin , password : fablabscanner)  

- ```GRANT ALL PRIVILEGES ON <dbname>.* TO '<username>'@'localhost';```
- ```FLUSH PRIVILEGES;```

# MySQL
## install MySQL
Use this command:  
 ```pip install mysql-connector-python-rf```  