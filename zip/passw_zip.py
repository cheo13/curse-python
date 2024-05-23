import zipfile

zip_file = 'data.zip'
file_to_compress = 'hola.txt'
password = 'pass1234'

with zipfile.ZipFile(zip_file, 'w') as zf:
    zf.setpassword(password.encode())
    zf.write(file_to_compress, compress_type=zipfile.ZIP_DEFLATED)

print(f"Archivo ZIP '{zip_file}' creado con la contraseña '{password}'")
