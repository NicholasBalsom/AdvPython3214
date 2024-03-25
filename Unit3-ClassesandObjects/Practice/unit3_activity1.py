from dataclasses import dataclass

@dataclass
class Animal():
    name:str
    species:str
    age:int
    color:str
    gender:str

    def describe(self):
        return f"{self.name} is a {self.age}--year old {self.species}. {self.gender} is {self.color}"


dog = Animal("Sadie", "Dog", "11", "Brown", "She")
dragon = Animal("Gus", "Bearded Dragon", "2", "Beige", "He")

print(dog.describe())
print(dragon.describe())