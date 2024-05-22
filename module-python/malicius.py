import os
import argparse

def list_files(directory, extensions):
    try:
        files = os.listdir(directory)
        print(f"Archivos en el directorio '{directory}' con las extensiones {extensions}:")
        
        for file in files:
            if file.endswith(tuple(extensions)):
                print(file)
    except FileNotFoundError:
        print(f"Error: El directorio '{directory}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permiso para acceder al directorio '{directory}'.")

def main():
    parser = argparse.ArgumentParser(description='Listar archivos en un directorio con extensiones específicas.')
    parser.add_argument('directory', type=str, help='Ruta del directorio que desea listar')
    parser.add_argument('--extensions', type=str, nargs='+', default=['.psl', '.dll', '.bat', '.vbs', '.scr'],
                        help='Extensiones de archivo a listar (por defecto: .psl .dll .bat .vbs .scr)')

    args = parser.parse_args()
    print(f"directory: {args.directory}")
    print(f"extensions: {args.extensions}")

    list_files(args.directory, args.extensions)

if __name__ == '__main__':
    main()
