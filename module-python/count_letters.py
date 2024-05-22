def count_letters(text):
   
    words = text.split()
    
    number_words = len(words)
    
    return number_words

text = input("Introduce una cadena de texto: ")

words_quantity = count_letters(text)
print(f"El número de palabras en la cadena de texto es: {words_quantity}")

# try:
#     z=a+b
# except Exception as error:
#     print(f"Error: {error}")
