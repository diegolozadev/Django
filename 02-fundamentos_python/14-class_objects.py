class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def work(self):
        return f"{self.name} esta trabajando duro y su edad es {self.age}"
    
person1 = Person("Mafe", 28)
person2 = Person("Julian", 15)

print(person1.work())
print(person2.work())