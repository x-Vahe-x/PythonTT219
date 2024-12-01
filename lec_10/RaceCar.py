from VehiclesSubclasses import Car

class RaceCar(Car):
    def __init__(self, name, speed, fuel_type, max_speed):
        super().__init__(name, speed, fuel_type)
        self.max_speed = max_speed

    def describe(self):
        return f"A race car named {self.name} with a top speed of {self.max_speed} km/h and runs on {self.fuel_type}."
