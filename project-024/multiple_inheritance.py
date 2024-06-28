class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def turn_on(self):
        return f"{self.make} {self.model} on"

    def turn_off(self):
        return f"{self.make} {self.model} off"

class Flyer:
    def __init__(self, maximum_altitude):
        self.maximum_altitude = maximum_altitude

    def take_off(self):
        return f"Taking off until {self.maximum_altitude} meters"

    def land(self):
        return "Landing"

class Airplane(Vehicle, Flyer):
    def __init__(self, make, model, maximum_altitude):
        Vehicle.__init__(self, make, model)
        Flyer.__init__(self, maximum_altitude)

    def fly(self):
        return f"{self.make} {self.model} flying at {self.maximum_altitude} meters"


airplane1 = Airplane("Boeing", "747", 10000)
print(airplane1.turn_on()) # Vehicle method
print(airplane1.take_off()) # Flyer method
print(airplane1.fly()) # Airplane method
print(airplane1.land()) # Flyer method
print(airplane1.turn_off()) # Vehicle method

print(Airplane.mro())
