#Task 1
import os

def list_directory_contents(path):
    try:
        contents = os.listdir(path)
        for file in contents:
            print(f'Path {path} contains: {file}')
    except FileNotFoundError:
        print(f"Directory {path} not found")
    except PermissionError:
        print(f"Permission denied for {path}")

path_input = input("Enter directory name/path: ")

list_directory_contents(path_input)


#Task 2
def report_file_size(directory):
    try:
        print(f"File sizes in directory '{directory}':")
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                print(f"{item}: {os.path.getsize(item_path)} bytes")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except PermissionError:
        print(f"Permission denied for directory '{directory}'")

file_size_input = input("Enter directory name/path: ")
report_file_size(file_size_input)


#Task 3
def count_file_extensions(directory):
    file_types = {}
    try:
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                name, extension = os.path.splitext(file)
                extension = extension.lower()
                if extension in file_types:
                    file_types[extension] += 1
                else:
                    file_types[extension] = 1
        for key, value in file_types.items():
            print(f"{key} - {value} files")
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
    except PermissionError:
        print(f"Permission denied for directory '{directory}'.")

file_ext_input = input("Enter directory name/path: ")

count_file_extensions(file_ext_input)