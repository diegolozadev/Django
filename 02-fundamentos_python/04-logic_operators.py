#AND Todo debe ser true
age = 25
licensed = False

if age >= 18 and licensed:
    print("Puedes manejar")
else:
    print("No puedes manejar")
    
#OR Con uno que sea true la condición true se ejecuta
is_student = False
membership = True

if is_student or membership:
    print("Obtiene precio especial")
    
#NOT Convierte True a False y False a True
is_admin = False
if not is_admin:
    print("Acceso denegado")
    

#Short Circuiting Se hace para evaluar la variable y si no cumple, se corta el programa.
name = "Diego"
print(name and name.upper())