#base class
class Superhero:
    def __init__(self, name, power, origin, level):
        self.name = name
        self.power = power
        self.origin = origin
        self.level = level  # e.g., "Elite", "Rookie", "Legend"

    def introduce(self):
        return f"I am {self.name}, born of {self.origin}, wielding the power of {self.power}!"

    def upgrade_level(self, new_level):
        self.level = new_level
        return f"{self.name} has ascended to {self.level} status!"

    def use_power(self):
        return f"{self.name} uses {self.power} with dazzling force!"

  #subclass
  class TechHero(Superhero):
    def __init__(self, name, origin, level, gadget):
        super().__init__(name, "Technomastery", origin, level)
        self.gadget = gadget  # e.g., "Nano Suit", "AI Drone", "Quantum Blade"

    def use_power(self):
        return f"{self.name} deploys {self.gadget} to manipulate tech and outsmart enemies!"

    def upgrade_gadget(self, new_gadget):
        self.gadget = new_gadget
        return f"{self.name} now wields the upgraded {self.gadget}!"

    #inherits superhero
    class MysticHero(Superhero):
    def __init__(self, name, origin, level, spellbook):
        super().__init__(name, "Arcane Magic", origin, level)
        self.spellbook = spellbook  # e.g., "Book of Shadows", "Runes of Eternity"

    def use_power(self):
        return f"{self.name} chants from the {self.spellbook}, unleashing mystical energy!"


#polymorphism 
def hero_showdown(hero):
    print(hero.introduce())
    print(hero.use_power())

#ACTIVITY @

# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Function to demonstrate polymorphism
def travel(vehicle):
    print(f"{vehicle.__class__.__name__} is moving:")
    vehicle.move()

# Example usage
vehicles = [Car(), Plane(), Bicycle(), Boat()]

for v in vehicles:
    travel(v)
