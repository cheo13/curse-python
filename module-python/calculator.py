def init():
    number1 = int(input("Introduce el # 1: "))
    number2 = int(input("Introduce el # 2: "))
 
    sum = number1 + number2
    rest = number1 - number2
    
    try:
        div = number1 / number2
    except ZeroDivisionError as error:
        div = None
        print(f"Error: No se puede dividir entre cero. {error}")
    
    print(f"La suma de {number1} y {number2} es: {sum}")
    print(f"La resta de {number1} y {number2} es: {rest}")
    if div is not None:
        print(f"La división de {number1} y {number2} es: {div}")


