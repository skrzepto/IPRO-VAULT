import configparser
import sensors
import json
import requests
import time
from datetime import datetime, timezone

class Monitor:
    def __init__(self):
        self.config.read('ipro_vault.ini')
        self.read_config()

    def read_config():
        if self.config['sensors']['temperature']:
            self.sensors.append(sensors.DHT11.get_json())

        self.server_ip = self.config['server']['ip']
        self.server_port = self.config['server']['port']
        self.location = self.config['information']['location']
        self.serial_number = self.config['information']['serial_number']
        self.interval_min = self.config['information']['interval_min']

    def send_json_to_server(self, json_data):
        """
        call getSensorJson to get all the sensor data and relay it
        to the REST Server
        """
        #Notes: POST should we also do authentication with a secret key?
        url = str(self.server_ip + ":" + self.server_port)
        payload = {'sensors': json_data,
                  'location': self.location,
                  'serial_number': self.serial_number,
                  'datetime': datetime.now(timezone.utc).isoformat()}
        print(payload)
        headers = {'content-type': 'application/json'}
        try:
            response = requests.post(url, data=json.dumps(payload), headers=headers)
        except:
            # we need to log this since there was an issue sending the data
            pass

    def get_sensor_data(self):
        """
        walk through the sensor object array
        and call getJson to get the values
        return
        """
        data = {}
        for sensor in self.sensors:
            data[sensor.name] = sensor.getJson()

        return data

    def run():
        while True:
            time.sleep(self.interval_min*60)
            data = self.get_sensor_data()
            self.send_json_to_server(json_data=data)

if __name__ == "__main__":
    mon = Monitor()
    mon.run()
