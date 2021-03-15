print("Hello World!")
name = input("what is your name?")
print("my name is " + name)
print("your name should not be a number")

age = input("how old are you? ")
print(" your age is " + age)
try:
    int(age)

    if int(age) <0 or int(age) >111:
        print("your age is not real")
    else:
        print("your age is " + age)
except:
    print("Age must be an integer")
