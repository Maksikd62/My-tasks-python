from abc import ABC, abstractmethod

#Ships
class Ship(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def ship_type(self):
        pass

    def update_description(self, new_description):
        self.description = new_description

    def delete_description(self):
        self.description = None

    def delete_ship(self):
        del self

class Frigate(Ship):
    def ship_type(self):
        return "Frigate"

class Destroyer(Ship):
    def ship_type(self):
        return "Destroyer"

class Cruiser(Ship):
    def ship_type(self):
        return "Cruiser"

frigate = Frigate("Frigate", "A warship with a mixed armament, generally lighter than a destroyer.")
destroyer = Destroyer("Destroyer", "A fast, maneuverable long-endurance warship intended to escort larger vessels.")
cruiser = Cruiser("Cruiser", "A large warship capable of engaging multiple targets and providing fleet air defense.")

print(f"{frigate.name} is a {frigate.ship_type()} - {frigate.description}")
print(f"{destroyer.name} is a {destroyer.ship_type()} - {destroyer.description}")
print(f"{cruiser.name} is a {cruiser.ship_type()} - {cruiser.description}")
cruiser.update_description("Cruisers are generally larger than destroyers and smaller than battleships.")
print(f"{cruiser.name} is a {cruiser.ship_type()} - {cruiser.description}")
cruiser.delete_description()
print(f"{cruiser.name} is a {cruiser.ship_type()} - {cruiser.description}")

#Airplanes
class Airplane:
    def __init__(self, model, max_passengers):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = 0

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.model == other.model
        return False

    def __add__(self, passengers):
        if isinstance(passengers, int):
            if self.current_passengers + passengers <= self.max_passengers:
                self.current_passengers += passengers
            else:
                self.current_passengers = self.max_passengers
        return self

    def __sub__(self, passengers):
        if isinstance(passengers, int):
            if self.current_passengers - passengers >= 0:
                self.current_passengers -= passengers
            else:
                self.current_passengers = 0
        return self

    def __iadd__(self, passengers):
        return self.__add__(passengers)

    def __isub__(self, passengers):
        return self.__sub__(passengers)

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return False

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return False

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return False

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return False

    def __int__(self):
        return self.current_passengers

    def __str__(self):
        return self.model

airplane1 = Airplane("Boeing 747", 416)
airplane2 = Airplane("An-225 Dream", 1000)

print(airplane1 == airplane2) 
airplane1 += 100
print(int(airplane1)) 
airplane1 -= 50
print(int(airplane1)) 
print(airplane1 > airplane2)
print(airplane1 < airplane2)
print(str(airplane2))