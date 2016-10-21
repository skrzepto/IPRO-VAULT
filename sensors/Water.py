import RPi.GPIO as GPIO


class Water:

    def _init_(self, gpio_pin=18,pull_up_down=UP):
        PIO.setmode(GPIO.BCM)
        self.pull_up_down="GPIO.PUD_%s"(str(pull_up_down))
        GPIO.setup(gpio_pin, GPIO.IN, pull_up_down)
        self.wet

    def read_sensors(self):
        self.wet = GPIO.input(gpio_pin)
        print('wet=%s'(self.wet))

    def get_json(self):
        self.read_sensors()
        return {"wet": self.wet}
