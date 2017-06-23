import sys
import random

class Greenphire(object):

    loopIterate = int(input("How many people would you like to enter?\n"))

    width = 6               # Width of the lists, inside main list to take numbers
    height = loopIterate    # The number of times to iterate through the program is equal to the height of the matrix
    j = 0

    nameList = []           # List to store all user's names
    Matrix = []             # Corresponding matrix to store the numbers tha they input
    for y in range(height):
        Matrix.append([0 for x in range(width)])

    powerList = []          # List of the winning numbers
    tempList = []           # Temporary List to store numbers in the event of a tie in num frequency
    tempNum = 0
    maxFreq = 0

    for loop in range(loopIterate):

        firstName = input("\n\nPlease enter your first name:\n")
        lastName = input("Please enter your last name:\n")
        fullName = firstName + " " + lastName

        nameList.append(fullName)

        print("\nWhen picking your Powerball numbers, please make sure all of your picks are unique numbers.")

        for i in range(0, 6):
            tempNum = 0
            if i != 5:
                powerNum = input("Please enter ball number %d: (Between 1 and 69)" % (i + 1) + "\n")

                # Checks that a user doesn't enter a value already present in list
                for k in range(width):
                    while str(powerNum) in str(Matrix[j][k]):
                        powerNum = input("Looks like you already typed that. Try again!\n")

                # checks to see if the numbers entered are in the proper range, exits after 5 failed attempts
                powerCount = 0
                while int(powerNum) > 69 or int(powerNum) < 1:
                    powerCount += 1
                    if powerCount == 5:
                        # quits the program after too many invalid inputs
                        print("Sorry, I can't allow you to do that Dave. Goodbye.")
                        sys.exit()
                    print("Sorry, we aren't accepting of those numbers here.")
                    powerNum = input("Enter a ball number between 1 and 69:\n")
                    print(Matrix)
                Matrix[j][i] = powerNum

            # Gets the number for the Powerball from user
            elif i == 5:
                powerNum = input("Please enter ball number the Powerball number (Between 1 and 26): \n")
                while int(powerNum) > 26 or int(powerNum) < 1:
                    powerCount += 1
                    if powerCount == 5:
                        print("Sorry, I can't allow you to do that Dave. Goodbye.")
                        sys.exit()
                    print("Sorry, we aren't accepting of those numbers here.")
                    powerNum = input("Enter a ball number between 1 and 26:\n")
                Matrix[j][i] = powerNum

        # increments j, to move down to the next person in matrix
        j += 1

    print("\n\nThanks for playing!")

    # Transposes the matrix so that all corresponding indexes are grouped together
    Matrix2 = list(map(list, zip(*Matrix)))

    # Iterates through Matrix2, to find the highest number in each section of numbers
    for row in range(width):
        tempNum = 0
        for col in range(height):
            locationVal = Matrix2[row][col]    # find value of location
            numCount = Matrix2[row][0:height].count(locationVal)

            if row < width:
                if locationVal not in powerList[0:width]:
                    if numCount > tempNum:
                        tempNum = numCount
                        maxFreq = locationVal
                        tempList.append(locationVal)

                    elif numCount == tempNum:
                        maxFreq = 0
                        tempList.append(locationVal)

            # Checks if last row, then places numbers in a temp list for random num choice or picks maxFreq
            elif row == width:
                if numCount > tempNum:
                    tempNum = numCount
                    maxFreq = locationVal
                    tempList.append(locationVal)
                elif numCount == tempNum:
                    maxFreq = 0
                    tempList.append(locationVal)

        if maxFreq == 0:
            randVal = random.choice(tempList)
            powerList.append(randVal)
        else:
            powerList.append(maxFreq)

        tempList.clear()    # Clears tempList before the start of every row

    # Prints each name and Powerball Numbers
    for p in range(height):
        print('\n',nameList[p], Matrix[p][0:5], " Powerball: ", Matrix[p][5])

    print("\nDrum roll................")
    print("\nWinning numbers are: ", powerList[0:width-1], "Powerball: ", powerList[width-1])