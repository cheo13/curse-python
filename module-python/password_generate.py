import random
import string

def generate_pass(longitud):
    if longitud < 4:  
        raise ValueError("La longitud debe ser al menos 4 caracteres.")

    mayus = string.ascii_uppercase
    minus = string.ascii_lowercase
    digit = string.digits
    character_spec = string.punctuation

    caracteres = [
        random.choice(mayus),
        random.choice(minus),
        random.choice(digit),
        random.choice(character_spec)
    ]

    todos_caracteres = mayus + minus + digit + character_spec
    caracteres += random.choices(todos_caracteres, k=longitud - 4)

    random.shuffle(caracteres)

    password = ''.join(caracteres)
    return password

longitud = int(input("Introduce la longitud de la password: "))

try:
    password = generate_pass(longitud)
    print("Contraseña generada:", password)
except ValueError as e:
    print(e)
