"""
login_system.py
A simple text-based login and file management program in Python.

Features:
- Secure password input using getpass
- Reads, writes, and clears text files
- Includes input validation and user menu
"""

import os
import getpass

print("Hi User")

keep_running = True
while keep_running:
    username = input("What is your username? ")
    password = getpass.getpass("What is your password? ")
    if username == "Ali" and password == "A234":
        keep_running = False
    else:
        print("Username or password incorrect")

print(f"Welcome to the system, {username}!")

while True:
    print("\n(1) Read the file")
    print("(2) Write to the file")
    print("(3) Clear the file")
    print("(4) Exit the system")

    try:
        choice = int(input("What do you want to do? "))
    except ValueError:
        print("That's not a number")
        continue

    if choice == 1:
        if not os.path.exists("file1.txt"):
            print("Creating file1.txt since it doesn't exist...")
            open("file1.txt", "w").close()

        with open("file1.txt", "r") as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("The file is empty.")

    elif choice == 2:
        add_text = input("What do you want to add? ")
        with open("file1.txt", "a") as file:
            file.write(add_text + "\n")
        print("Text added successfully!")

    elif choice == 3:
        open("file1.txt", "w").close()
        print("File has been cleared.")

    elif choice == 4:
        print("Exiting the system...")
        break

    else:
        print("Invalid option, please choose again.")
