#!/bin/bash

echo "Setting up Raspberry Pi with required software"

apt-get update
apt-get install build-essential python-dev python-smbus python-pip git unzip

mkdir vault
cd vault
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git

cd Adafruit_Python_GPIO
python setup.py install

cd ..
wget https://github.com/adafruit_Python_MCP9808/archive/master.zip
unzip master.zip
rm master.zip

git clone https://github.com/skrzepto/IPRO-VAULT.git
