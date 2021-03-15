print("Hello World!")
name = input("what is your name?")
print("my name is " + name)
age = input("how old are you? ")
print(" your age is " + age)
try:
    int(age)
    print("your age is " + age)
except:
    print("Age must be an integer")
