#Brandon Gordon - Student Number: 10447737
################ Information on the zip() function was found here: http://stackoverflow.com/questions/3471999/how-do-i-merge-two-lists-into-a-single-list ################

transactionAmounts = []    #tracks the amounts added to or subtracted from the balance. Requirement #1
transactionTypes = []    #tracks whether the transactions made were add or subtract. 

def showInfo(valueList, typeList, desiredType):    #Defining the showInfo function to be called later in [I]nformation
    total = 0    #Initialise the total variable
    print (desiredType, "count:", typeList.count(desiredType))    #Retreive the desired type (either "Additon or "Subtraction") and count how many times it appears in our typeList
    for typ, num in zip(typeList, valueList):    #For everything in ValueList, assign the corresponding value from valueList
        if typ == desiredType:    #For every time the desired type is found in the lists
            total = total + num    #Add the corresponding value from valueList to the total variable
    print (desiredType, "total: $" + format(total, '.2f'))    #print the total for the desired type, formatted to 2 decimal places


print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print ("\n \t \tWelcome to Balance Tracker!")
print ("\n \t \tA Program by Brandon Gordon")
print ("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-(*)-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

balance = float(input (">>> Enter starting balance: $"))    #Assigning a float value to 'balance' through the input function, parsed through the float function
startingBalance = balance   #We refer to this balance later in the History menu option

while True:   #Enter an endless loop. Requirement #2
    print ("\nCurrent balance is: $" + format(balance, '.2f'))    #Requirement #2.1
    print ("Choose from the following options: ")
    menuChoice = input ("\t[A]ddition \n \t[S]ubtraction \n \t[H]istory \n \t[I]nformation \n \t[Q]uit \n >").upper() #The output required for users to choose options and STORES AS CAPITAL LETTER

    if menuChoice == "A":    #If the user chooses [A]ddition. Requirement #2.2
        changedAmount = float(input("Add to balance: $"))    #Stores the changed amount so that it can be appended to the transactionAmounts list
        balance = balance + changedAmount    #add the float input from the user to the balance
        transactionAmounts.append(changedAmount)    #appends the changed amount to the transactionAmounts list
        transactionTypes.append("Addition")    #appends the transaction type to the transactionTypes list

        
    elif menuChoice == "S":    #If the user chooses [S]ubtraction. Requirement #2.3
        changedAmount = float(input("Subtract from balance: $"))    #Stores the changed amount so that it can be appended to the transactionAmounts list
        balance = balance - changedAmount    #subtract the float input from the user from the balance
        transactionAmounts.append(changedAmount)    #appends the changed amount to the transactionAmounts list
        transactionTypes.append("Subtraction")    #appends the transaction type to the transactionTypes list


    elif menuChoice == "H":    #If user chooses [H]istory. Requirement #2.4
        if len(transactionAmounts) == 0:    #check if user has made any transactions yet, if they haven't then it prints the following statement
            print ("You have not made any transactions yet!")
        else:    #If the user has made transactions, go ahead and display them!
            print ("Starting balance was $" + format(startingBalance, '.2f'))
            for transnum, (num, typ) in enumerate(zip(transactionAmounts, transactionTypes), 1):    #enumerate the zip of the two lists to give "transnum", and pull variables typ and num from the lists
                print("Transaction", transnum, "-", typ, "of $" + format(num,'.2f'))    #print them in a pretty looking way
            


    elif menuChoice == "I":    #If the user chooses [I]nformation. Requirement #2.5
        print ("Transaction Information: ")
        showInfo(transactionAmounts, transactionTypes, 'Addition')    #Call the showInfo function and pass list names with either "Additon" or "Subtraction" to determine desired information
        showInfo(transactionAmounts, transactionTypes, 'Subtraction')


    elif menuChoice == "Q":    #If the user chooses [Q]uit. Requirement #2.6
        print ("Goodbye!")
        break   #Break out of the while loop



    else:
        print ("PLEASE ENTER A VALID COMMAND :)")    #Requirement #2.7

