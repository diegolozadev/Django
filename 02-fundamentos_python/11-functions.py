
# PARÁMETROS, los que vayan en la función.
def hello(greet = "Buenas", name = "amigo"): # Se puede utilizar DEFAULT parámetros
    print(f"{greet}, {name}")

# ARGUMENTOS, se llaman cuando llamamos la función.
hello("Hola", "Diego")
hello()

def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs
    
print(big_function(1, 2, 3, 4, 5, num1 = 77, num2 = 100 ))
