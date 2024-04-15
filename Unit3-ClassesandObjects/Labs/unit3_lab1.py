# Unit 3 Lab 1 - Creating a Vehicle Hierarchy


# Vehicle parent class (Base class)
class Vehicle:
    # Initalize the attributes
    def __init__(self, make: str, model: str, year: int, speed=0.0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    # Increases the speed of the Vehicle by a given amount
    def accelerate(self, amount):
        self.speed += amount

    # Decrases the speed of the Vehicle by a given amount
    def brake(self, amount):
        self.speed -= amount

    def display(self):
        print(
            f"\n{self.make} {self.model}: \n"
            f"--{('-' * (len(self.make)+ len(self.model)))}--\n"
            f"Year: {self.year}\n"
            f"Speed: {self.speed:.1f} km/h"
        )


# Car subclass (parent class Vehicle)
class Car(Vehicle):
    def __init__(self, *args, speed=0.0, fuel_level=0.0):
        # Let the parent class handle the initalization of make, model and year
        super().__init__(*args, speed)
        self.fuel_level = fuel_level

    # Refuels the car to 100% capacity
    def refuel(self):
        self.fuel_level = 1.0

    def display(self):
        super().display()
        print(f"Fuel Level: {self.fuel_level:.0%}")


# Bicycle subclass of Vehicle
class Bicycle(Vehicle):
    def __init__(self, *args, speed=0.0, pedal_cadence=0):
        # Let the parent class handle the initalization of make, model and year
        super().__init__(*args, speed)
        self.pedal_cadence = pedal_cadence

    # Changes the pedal cadence to a specified integer
    def change_cadence(self, new_cadence: int):
        if new_cadence >= 0:
            if self.pedal_cadence < new_cadence:
                # Increases the speed according to cadence (Note: NOT ACCURATE)
                self.accelerate(new_cadence / 3)
            else:
                # Decreases speed according to cadence
                self.brake(new_cadence / 3)
            self.pedal_cadence = new_cadence
        else:
            print("Pedal cadence must be a positive integer")

    # Displays details about the bicycle
    def display(self):
        # Calls parent class display method first
        super().display()
        print(f"Pedal Cadence: {self.pedal_cadence} RPM")


# Creating instances of both subclasses
camry = Car("Toyota", "Camry", 2014)
mtb = Bicycle("Rocky Mountain", "Thunderbolt 770", 2017)
# Using the methods
camry.refuel()
camry.accelerate(50)
camry.brake(10)

mtb.change_cadence(80)
mtb.change_cadence(60)

# Displays the information
camry.display()
mtb.display()
