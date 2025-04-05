def add(P, Q):
    return P+Q
def subtract(P,Q):
    return P-Q
def multiply(P, Q):
    return P*Q
def divide(P,Q):
    return P/Q

print("Welcome to the calculator! Choose your operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1/2/3/4): "))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == 1:
    result = add(num1, num2)
    print(num1," + ",num2," = ",result)
elif choice == 2:
    result = subtract(num1, num2)
    print(num1," - ",num2," = ",result)
elif choice == 3:
    result = multiply(num1, num2)
    print(num1," * ",num2," = ",result)
elif choice == 4:
    result = divide(num1, num2)
    print(num1," / ",num2," = ",result)
else:
    print("Invalid option selected!")