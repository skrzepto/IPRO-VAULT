import Adafruit_DHT
from datetime import datetime, timezone

class DHT11:
    def __init__(self, gpio_pin=4, sensor_ver=11):
        self.humidity
        self.temperature
        self.gpio_pin = gpio_pin
        self.sensor_version = sensor_ver
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def read_sensors(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor_ver, self.gpio_pin)
        humidity, temperature = Adafruit_DHT.read_retry()
        self.timestamp = datetime.now(timezone.utc).isoformat()
        if self.humidity is not None and self.temperature is not None:
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(self.temperature, self.humidity))

    def get_json(self):
        self.read_sensors()
        return {"temp": self.temperature,
                "humidity": self.humidity}
