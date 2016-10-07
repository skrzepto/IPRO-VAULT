import configparser
import json
import requests
import time
from datetime import datetime, timezone


class Monitor:
    def __init__(self):
        self.sensors = {}
        self.config = configparser.ConfigParser()
        self.config.read('ipro_vault.ini')
        self.read_config()

    def read_config(self):
        if self.config['sensors']['temperature'] == 1:
            from sensors.dht11 import DHT11
            self.sensors['temperature']= DHT11()
        if self.config['sensors']['humidity'] == 1:
            # DHT11     
            pass
        # add other sensors here

        self.server_ip = self.config['server']['ip']
        self.server_port = self.config['server']['port']
        self.location = self.config['information']['location']
        self.serial_number = self.config['information']['serial_number']
        self.interval_min = int(self.config['information']['interval_min'])

    def send_json_to_server(self, sensor_data):
        """
        call getSensorJson to get all the sensor data and relay it
        to the REST Server
        """
        #Notes: POST should we also do authentication with a secret key?
        url = str(self.server_ip + ":" + self.server_port)
        payload = {'location': self.location,
                  'serial_number': self.serial_number,
                  'datetime': datetime.now(timezone.utc).isoformat()}
        payload.update(sensor_data)
        print(payload)
        headers = {'content-type': 'application/json'}
        try:
            response = requests.post(url, data=json.dumps(payload), headers=headers)
        except:
            # we need to log this since there was an issue sending the data
            print("ERROR: Failed to send data")
            pass

    def get_sensor_data(self):
        """
        walk through the sensor object array
        and call getJson to get the values
        return
        """
        sensor_data = {}
        for key, value in self.sensors.items():
            sensor_data += {value.get_json()}

        return sensor_data

    def run(self):
        while True:
            time.sleep(self.interval_min*60)
            data = self.get_sensor_data()
            self.send_json_to_server(sensor_data=data)

if __name__ == "__main__":
    mon = Monitor()
    mon.run()
