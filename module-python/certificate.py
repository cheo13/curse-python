def good_pass(password):
    if len(password) == 10:
        return True
    else:
        return False

def main():
    password = input("Por favor, ingresa tu password: ")
    if good_pass(password):
        print("¡Contraseña válida! Has ingresado correctamente.")
    else:
        print("Error: La password debe tener exactamente 10 caracteres.")

if __name__ == "__main__":
    main()
