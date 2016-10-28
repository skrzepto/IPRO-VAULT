import Adafruit_BMP.BMP085 as BMP085

#BMP085 Temperature Pressure Sensor

class BMP180:

    def _init_(self):
        self.sensor = BMP085.BMP085()
        self.temperature
        self.pressure
        self.altitude
        self.sealevel_pressure

    def read_sensors(self):
        # self.temperature = self.sensor.read_temperature()
        self.pressure = self.sensor.read_pressure()
        #self.altitude = sensor.read_altitude()
        #self.sealevel_pressure = sensor.read_sealevel_pressure()

    def get_json(self):
        self.read_sensors()
        res = {}
        res['pressure'] = self.pressure
        # res['temperature2'] = self.temperature
        # res['altitude'] = self.altitude
        # res['sealevel_pressure'] = self.sealevel_pressure
        return res 
