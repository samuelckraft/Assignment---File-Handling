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

list_directory_contents('')