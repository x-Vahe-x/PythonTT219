from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type

    def describe(self):
        return f"A car named {self.name} that can go up to {self.speed} km/h and runs on {self.fuel_type}."

class Plane(Vehicle):
    def __init__(self, name, speed, capacity):
        super().__init__(name, speed)
        self.capacity = capacity

    def describe(self):
        return f"A plane named {self.name} that can go up to {self.speed} km/h and has a capacity of {self.capacity} passengers."

class Boat(Vehicle):
    def __init__(self, name, speed, type_of_boat):
        super().__init__(name, speed)
        self.type_of_boat = type_of_boat

    def describe(self):
        return f"A {self.type_of_boat} boat named {self.name} that can go up to {self.speed} km/h."
