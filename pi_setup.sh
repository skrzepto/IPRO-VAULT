#!/bin/bash

echo "Setting up Raspberry Pi with required software"

apt-get update
apt-get install build-essential python3-dev python3-smbus python3-pip git unzip

mkdir vault
cd vault
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
wget https://github.com/adafruit/Adafruit_Python_MCP9808/archive/master.zip
git clone https://github.com/skrzepto/IPRO-VAULT.git
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
git clone https://github.com/adafruit/Adafruit_Python_BMP.git

pip3 install requests

cd Adafruit_Python_GPIO
python3 setup.py install
cd ..

unzip master.zip
rm master.zip
cd Adafruit_Python_MCP9808-master
python3 setup.py install
cd ..
cd Adafruit_Python_DHT
python3 setup.py install
cd ..
cd Adafruit_Python_BMP
python3 setup.py install
