#Listas estructuras de datos, almacenar mas datos dentro de una variable
list_numbers = [1, 2, 3, 4, 5]
list_letters = ['a', 'b', 'c']
list_mix = [2, 'z', True, [1, 2, 3], 5.5]

shopping_cart = ['Laptop', "Silla"]
print(type(shopping_cart))


# METODOS, superpoderes para hacer cambios en las listas

#  Append agrega un valor al final de la lista
list_numbers.append(100) 
print(list_numbers)

# remove elimina el valor que nosotros le pasemos
list_numbers.remove(4)
print(list_numbers)

# count cuenta cuantas veces aparece un valor dentro de una lista
print(list_numbers.count(2))