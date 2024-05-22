import os
import shutil
from datetime import datetime

def create_backup(source_directory, backup_directory, extension=".log"):
    if not os.path.exists(source_directory):
        print(f"Error: El directorio de origen '{source_directory}' no existe.")
        return

    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)
        print(f"Directorio de backup '{backup_directory}' creado.")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_subdirectory = os.path.join(backup_directory, f"backup_{timestamp}")

    os.makedirs(backup_subdirectory)
    print(f"Subdirectorio de backup '{backup_subdirectory}' creado.")

    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                shutil.copy(file_path, backup_subdirectory)
                print(f"Archivo '{file}' copiado a '{backup_subdirectory}'.")

    print("Backup completado.")

source_directory = input("Ingrese la ruta del directorio de origen: ")
backup_directory = input("Ingrese la ruta del directorio de backup: ")

create_backup(source_directory, backup_directory)
if __name__ == '__main__':
    main()
