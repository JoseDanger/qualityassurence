def sum(start, end):
    sum = 0
    for item in range(start, end):
        sum = addTwoNumber(sum, item)
        return sum
        def addTwoNumber(num1, num2):
            return num1 + num2
            print(sum(0,10))
