import Adafruit_DHT
from datetime import datetime, timezone

#DHT11 Temperature Humidity Sensor

class DHT11:
    def __init__(self, gpio_pin=4, sensor_ver=11):
        self.humidity
        self.temperature
        self.gpio_pin = gpio_pin
        self.sensor_version = sensor_ver
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def read_sensors(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor_ver, self.gpio_pin)
        self.timestamp = datetime.now(timezone.utc).isoformat()
        if self.humidity and self.temperature:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(self.temperature, self.humidity))

    def get_json(self):
        self.read_sensors()
        return {"temp": self.temperature,
                "humidity": self.humidity}
