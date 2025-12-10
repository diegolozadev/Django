class Person:
    species = "Humano"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod # Con este decorador cambia globalmente la clase en este caso la variable species
    def change_species(cls, new_species):
        cls.species = new_species
        
    @staticmethod # Con este staticmethod es para acceder a metodos directos de la clase sin tener que crear un objeto
    def is_older(age):
        return age >= 18
        
        
person1 = Person("Diego", 28)
person2 = Person("Mafe", 30)

print(person1.species)
print(person2.species)

Person.change_species("Reptiliano")

print(person1.species)
print(person2.species)

print(Person.is_older(15)) # Probamos este staticmethod llamando a la clase directamente
print(person2.is_older(person2.age)) # Aca llamamos el objeto ya creado anteriormente