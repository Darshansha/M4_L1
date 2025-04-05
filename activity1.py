print("Hi, my name is Aran. I am 13 years old. What is your name?")

def hello(name, age):
    print("Hello", name, "("+age,"years old)!")
name = input("Enter your name: ")
age = int(input("Enter your age: "))

hello(name, age)