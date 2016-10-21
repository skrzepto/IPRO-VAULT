import Adafruit_BMP.BMP085 as BMP085

#BMP085 Temperature Pressure Sensor

class BMP085:

    sensor = BMP085.BMP085()
    def _init_(self):
        self.temperature
        self.pressure
        #self.altitude
        #self.sealevel_pressure

    def read_sensors(self):
        self.temperature = sensor.read_temperature()
        self.pressure = sensor.read_pressure()
        #self.altitude = sensor.read_altitude()
        #self.sealevel_pressure = sensor.read_sealevel_pressure()

    def get_json(self):
        self.read_sensors()
        return {#"temp": self.temperature,
                "pressure": self.pressure,
                #"Altitude": self.altitude,
                #"sealevel_pressure": self.sealevel_pressure}
