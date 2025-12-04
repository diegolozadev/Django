# Repetir una acción

my_list = [1, 2, 3, 4, 5]
add = 0

for number in my_list:
    print(number)
    add += number
    
print(add)


for index, number in enumerate(list(range(100))):
    print(index, number)
    