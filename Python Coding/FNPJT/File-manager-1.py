#Name : ERIC AMOH ADJEI
#Date : 11/03/2023
#Assignment : Python File Manager


# Description: This is a file manager that can read, write, append and close a file
print(" \n \n \t\t\t Welcome to our file manager \n \n \t\t")
print(" \n \n \t\This is a file manager that can read, write, append and close a file \n \n \t\t")
name = input("What is your name? \n :")

print(" \n \n \t\t\t Nice to meet you\n " + name + " .\n\t")

# ------------------------------------------ #
# I can import a module as just import os
# or the whole library as from os import (*) with the asterisk
#os has function and everything that is in the os library like rename and remove
#from os import * if i want to use all the functions in the os library or
#name and rename the file as well as the directory
#rename("filemanager.txt", "Filemanager-Renamed.txt") - #renames the file
#remove("Filemanager-Renamed.txt") - #removes the file
#mkdir("make File Manager") - #creates a new folder or makes new directory
#chdir(" New File Manager Renamed") - #changes the directory to the new folder
# ---------------------------------------------------- #


# Description:Starting the code of a file manager that can read, write, append and close a file


#read file and automatically closes the file with WITH
with open("filemanager.txt", "r") as f:
    #Passing all my codes to the file
    context = f.read()

#writing to a file and automatically closes the file with WITH
with open("filemanager.txt", "w") as f:
    f.write("\t\t\t I AM A NEW FILE MANAGER\n \n")
    f.write(" \n Python is not only a powerful and versatile programming language \n  ")
    f.write("\n \n \n but also a fantastic choice for creating graphical user interfaces (GUIs). \n ")
    f.write("Python's simplicity and wide range of libraries make it a top choice for developers \n ")
    f.write("\n  looking to build user-friendly applications.\n \t \t \n" )
    f.flush()

#appending to a file
with open("filemanager.txt", "a") as f:
    f.write("\n \n \t\t\t I APPENDED A NEW FILE MANAGER\n \n \t\t")
    f.write(" \n \n \n What are GUIs? \n \n GUIs are graphic user interfaces that allow you to interact \n")
    f.write(" \n \n with your electronic devices ")
    f.write("\n \n using graphical elements typically using a pointing device such as a mouse, windows, buttons, and menus. \n ")

    f.flush()
    print(context)
    