from random import randint
#ask computer to generate a random number
myNum= randint(1,99)

# because we have
i = 0
while i <= 9:
    #set ten times for guessing, because the first time has already been input so 9 left starting from 1
    #ask a player to input a number
    print("you have " + str(10 - i) + " chances")
    # ask player to input number
    guessNum = input("please guess a number")
    # varify input number
    try:
        int(guessNum)
        if int(guessNum) < 1 or int(guessNum) > 99:
            print("you should input a number between 1 to 99")
        #number is valid
        else:
            if int(guessNum) > myNum:
                print("The number is lower")
            elif int(guessNum) < myNum:
                print("your number is higher")
            else:
                print("YOU WIN!")
                break
    except:
        print("please input a valid number")
    i = i + 1

if i == 10:
    print("you have no chances left")
    print("you lost :'(")




