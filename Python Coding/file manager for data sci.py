#Name : ERIC AMOH ADJEI
#Date : 11/03/2023
#Assignment : Python File Manager


import random
import time

# setting loading time for application to run smooth.
load_time = 2 # seconds
load_time2= 4#seconds

# loading screen for 3 seconds
print("\t \t \n Loading app...\t \n")
time.sleep(load_time)
print("\t \n   ...\n")
time.sleep(load_time)
print(f"App loaded after {load_time2}seconds")


# Description: This is a file manager that can read, write, append and close a file
print(" \n \n \t\t\t Welcome to our file manager \n \n \t\t")

print(" \n \n \tThis is a file manager that can read, write, append and close a file \n \n \t\t")

time.sleep(load_time)
name = input("What is your name? \n :")
print(" \n \n \t\t\t Nice to meet you\n " + name + " .\n\t")

time.sleep(load_time)
print("\n \t From here we will be importing large data sets, do you have any question? \n \t Please, if you have any query, write it down and ask later: \n")

time.sleep(load_time2)

# For this code, we need to create a file with lots of pieces of information (data)
# We will then read that file and display the contents

# creaing function to test whether or not the value passed in to the function was a number
def isNumber(theString):
    try:
        float(theString)
        return True
    except ValueError:
        return False

#creating function to create and write a file
def writeToFile(fileNameToWrite):
    #define a variable to hold the total amount of numbers I want to generate
    numDataPoints = 20
    time.sleep(load_time)
    
    # array that is going to hold my large amount of numbers
    largeDataset = []
    time.sleep(load_time)

    #Create a for loop to generate random numbers and add them to the dataset
    for _ in range(numDataPoints):
        #generate a random number between 1 and 500
        aRandomNumber = random.randint(1, 9500)
       
        #add the random number to the largeDataset array
        largeDataset.append(aRandomNumber)

# Write the dataset to a text file
    try:
        # open the file in write mode
        with open(fileNameToWrite, 'w') as file:
            #loop through each number in the array and write that number to the file
            for dataPoint in largeDataset:
                #write this text to the file
                file.write(str(dataPoint) + ',')
    except Exception as e:
        print("An error occurred while writing to the file:", str(e))

#create a function to read the contents of the file
def readmyFile(fileNameToRead):
    try:
        # open the file in read mode
        with open(fileNameToRead, 'r') as file:
            # read the contents of the file we just opened
            data = file.read()
            #return the contents of the file to the code that called this function
            return data
    except FileNotFoundError as e:
        print("The file was not found:", str(e))
        return None
    except Exception as e:
        print("An error occurred while reading from the file:", str(e))
        return None





# the name of the file
theFileName = "filemanager.txt"

#call the function to create the file
writeToFile(theFileName)

#loop through the data, and format it
dataRead = readmyFile("filemanager.txt")

# I only want to loop through the numbers if there was data in the file
if dataRead is not None:
    #take the #,#,#,#, data in put it into an array
    for amount in dataRead.split(','):
        # check if the amount is a number
        if isNumber(amount):
            # print out the number with currency formatting, example: $9,243.03
            print(f"${int(amount):,.3f}")

time.sleep(load_time)
print( "\n  The data in the file", dataRead)
print(" \n Python is not only a powerful and versatile programming language \n \t THE END") 
print("\t\t\t Thank You\n \n")
