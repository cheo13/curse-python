import random

def guess_number():
    secret_number = random.randint(0,999)
    print("Adivinar hasta 3 digitos!")
    
    while True:
        guess = input("Ingrese el numero: ")
        
        if not guess.isdigit() or len(guess) != 3:
            print("Ingresa 6 digitos!...")
            continue
        
        guess = int(guess)
        
        if guess < secret_number:
            print("Demasiado Bajo!")
        elif guess > secret_number:
            print("Demasiado Alto")
        else:
            print("El numeros secreto es: ", secret_number)
            break

guess_number()