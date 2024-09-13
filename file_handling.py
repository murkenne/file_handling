'''
1. Exploring Python's OS Module
Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

Task 1: Directory Inspector:

Problem Statement: Create a Python script that lists all files and subdirectories in a given directory.
Your script should prompt the user for the directory path and then display the contents.
'''

import os


def list_directory_contents(path):
    try:
        # List all files and subdirectories in the given path
        contents = os.listdir(path)
        print(f"Contents of {path}")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Error: The specified directory does not exist.")
    except PermissionError:
          print("Error: You do not have permission to access this directory.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        
if __name__ == "__main__":
    directory_path = input("Enter directory path: ")
    list_directory_contents(directory_path)
