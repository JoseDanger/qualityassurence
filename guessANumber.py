from Library import generateANumber, stillHaveChance, win, isValidInput, tryTimesLeft, feedback

myNum = generateANumber()

tryTime = 0
totalTime = 10
guessNum = 0
while stillHaveChance(tryTime, totalTime) and (not win(guessNum, myNum)):
    print("you have " + str(tryTimesLeft(tryTime, totalTime)) +" chances left")
    guessNum = input("Please guess a new number")
    if isValidInput(guessNum):
        guessNum = int(guessNum)
        print(feedback(guessNum, myNum))
    else:
        print("You should input a number between 0 and 100")
    tryTime = tryTime + 1

if not stillHaveChance(tryTime, totalTime):
    print("YOU LOOOOOOOOOOOOOSE!")
