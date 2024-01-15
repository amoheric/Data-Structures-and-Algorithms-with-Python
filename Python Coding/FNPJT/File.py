import random
# For this code, we need to create a file with lots of pieces of information (data)
# We will then read that file and display the contents

# create a function to test whether or not the value passed in to the function was a number
def isNumber(theString):
    try:
        float(theString)
        return True
    except ValueError:
        return False

#create a function to create and write a file
def writeToFile(fileNameToWrite):
    #define a variable to hold the total amount of numbers I want to generate
    numDataPoints = 10000

    # array that is going to hold my large amount of numbers
    largeDataset = []

    #Create a for loop to generate random numbers and add them to the dataset
    for _ in range(numDataPoints):
        #generate a random number between 1 and 10000
        aRandomNumber = random.randint(1, 10000)
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
def readFromFile(fileNameToRead):
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
theFileName = "exampledata.txt"

#call the function to create the file
writeToFile(theFileName)

#loop through the data, and format it
dataRead = readFromFile("exampledata.txt")

# I only want to loop through the numbers if there was data in the file
if dataRead is not None:
    #take the #,#,#,#, data in put it into an array
    for amount in dataRead.split(','):
        # check if the amount is a number
        if isNumber(amount):
            # print out the number with currency formatting, example: $9,243.03
            print(f"${int(amount):,.2f}")


#print("The data in the file", dataRead)
