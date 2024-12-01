class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def describe(self):
        return f"A {self.name} that can go up to {self.speed} km/h."
