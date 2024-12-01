from Vehicle import Vehicle
from VehiclesSubclasses import Car, Plane, Boat
from RaceCar import RaceCar

def main():
    car = Car("Sedan", 180, "gasoline")
    plane = Plane("Boeing 747", 900, 416)
    boat = Boat("Yacht", 80, "luxury")
    race_car = RaceCar("Formula 1", 300, "high-octane fuel", 350)

    print(car.describe())
    print(plane.describe())
    print(boat.describe())
    print(race_car.describe())

if __name__ == "__main__":
    main()
