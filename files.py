import os

temporary_directory = 'tmp'
file_name = "example_file.txt"
file_path = f'{temporary_directory}/{file_name}'

if temporary_directory not in os.listdir():
    print("temp dir not exist")
    os.mkdir(temporary_directory)

try:
    print("Trying to open file")
    file = open(file_path, "r")
    print(file.read())
except FileNotFoundError as error:
    print(f"plik nie istnieje {error}")
    print("trying to create file")
    file = open(file_path, 'x')
    print(f'file exists? {os.path.exists(file_path)}')
    print(file)
    file.close()
    print(f'file exists? {os.path.exists(file_path)}')


