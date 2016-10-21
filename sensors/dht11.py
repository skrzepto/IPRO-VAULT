import Adafruit_DHT
from datetime import datetime, timezone

class DHT11:
    def __init__(self, gpio_pin=4, sensor_ver=11):
        self.humidity=-1
        self.temperature=-1
        self.gpio_pin = gpio_pin
        self.sensor_ver= sensor_ver

    def read_sensors(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor_ver, self.gpio_pin)
        if self.humidity and self.temperature:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(self.temperature, self.humidity))

    def get_json(self):
        self.read_sensors()
        return {"temperature": self.temperature,
                "humidity": self.humidity}
