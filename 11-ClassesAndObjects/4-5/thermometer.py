import random

class Thermometer:
    def __init__(self):
        self.is_on = False
        self.temperature = None

    def turn_on(self):
        self.is_on = True
        print("Thermometer is ON.")

    def turn_off(self):
        self.is_on = False
        self.temperature = None
        print("Thermometer is OFF.")

    def measure(self):
        if not self.is_on:
            print("Cannot measure: thermometer is turned off.")
            return

        # Generate a random integer between 340 and 420 and divide by 10 for 0.1 accuracy
        self.temperature = random.randint(340, 420) / 10.0

    def display(self):
        if not self.is_on:
            print("Cannot display: thermometer is turned off.")
            return

        if self.temperature is None:
            print("No temperature measured yet.")
            return

        message = f"Temperature: {self.temperature:.1f}C"

        if self.temperature >= 41.0:
            message += " (fever) CRITICAL TEMPERATURE!!"
        elif self.temperature >= 37.0:
            message += " (fever)"

        print(message)