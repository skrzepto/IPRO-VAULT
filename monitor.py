
class Monitor
    def __init__(self):
        self.sensors = []
        # call function that initializes the sensor objects
        self.server_ip
        self.server_port
        # call function that reads a config file and sets these values up

    def send_json_to_server(self, json):
        """
        call getSensorJson to get all the sensor data and relay it to the REST Server
        """
        #Notes: POST should we also do authentication with a secret key?
    def getSensorJson(self,):
        """
        walk through the sensor object array
        and call getJson to get the values
        return
        """
        data = {}
        for sensor in self.sensors:
            data[sensor.name] = sensor.getJson()

        return data
        
        
