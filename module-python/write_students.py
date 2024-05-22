print(f"Escribir en el archivo.... modo 'w' borra contenido existente")
with open('students.txt', 'w') as file:
    content = file.write('Hola soy Sergio! de Software\n')


print(f"Agregar lineas al achivo con modo 'a'")
with open('students.txt', 'a') as file:
    conten = file.write('Hola soy Sergio! =)\n')








# SERGIO
# ANDRES
# SANTIAGO
# NICOLAS
# PABLO
# DIEGO
# LUIS
# ANGEL
# JASON
# ERICK