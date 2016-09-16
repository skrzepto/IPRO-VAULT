import configparser
import sensors
import json
import requests

class Monitor
    def __init__(self):
        self.config.read('ipro_vault.ini')
        self.read_config()

    def read_config():
        if self.config['sensors']['temperature']:
            self.sensors.append(sensors.DHT11.DHT11.getJSON())

        self.server_ip = self.config['server']['ip']
        self.server_port = self.config['server']['port']
        self.location = self.config['information']['location']
        self.serial_number = self.config['information']['serial_number']

    def send_json_to_server(self, json):
        """
        call getSensorJson to get all the sensor data and relay it
        to the REST Server
        """
        #Notes: POST should we also do authentication with a secret key?
        url = str(self.server_ip + ":" + self.server_port)
        payload = {'sensors': json
                  'location': self.location,
                  'serial_number': self.serial_number}

        headers = {'content-type': 'application/json'}

        response = requests.post(url, data=json.dumps(payload), headers=headers)

    def getSensorData(self):
        """
        walk through the sensor object array
        and call getJson to get the values
        return
        """
        data = {}
        for sensor in self.sensors:
            data[sensor.name] = sensor.getJson()

        return data


