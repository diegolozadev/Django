class Person:
    species = "Humano"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._energy = 100 # El _ protege la variable (viene por convención, nos dice que esto es un atributo protegido)
        self.__password = "12345" # El __ privatiza la variable
    
    def work(self):
        return f"{self.name} esta trabajando duro y su edad es {self.age}"
    
    def _waste_energy(self, quantity):
        self._energy -= quantity
        return self._energy
    
    def __generate_password(self): # Esto es un metodo privado
        return f"$${self.name}{self.age}$$"
    
    
    
person1 = Person("Mafe", 28)
person2 = Person("Julian", 15)

print(person1.work())
print(person2.work())
print(person1._waste_energy(10))
print(person2._Person__password) # Para ingresar a la variable privada se coloca un _ y se llama a la Class (esto no es lo ideal)
print(person2._Person__generate_password()) # Para ingresar al metodo privado se coloca un _ y se llama a la Class (esto no es lo ideal)

