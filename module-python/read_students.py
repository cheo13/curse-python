print(f"Mostrar lista de students...")
with open('students.txt', 'r') as file:
    content = file.read()

print(content)


print(f"Mostrar 3 students...")

with open('students.txt', 'r') as file:
    content = file.readlines()[:3]

for student in content:
    print(student.strip()) 

    
def view_students(quantity):
    if quantity > 10:
        print("Error: ¡La cantidad de estudiantes no puede superar los 10!")
    else:
        with open('students.txt', 'r') as file:
            students = file.readlines()[:quantity]

        print("Los estudiantes son:")
        for student in students:
            print(student.strip())

try:
    quantity = int(input("Ingrese la cantidad de estudiantes que desea mostrar: "))
    view_students(quantity)
except ValueError:
    print("Error: ¡Por favor, ingrese un número entero válido!")
