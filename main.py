import sys, subprocess

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

input("Welcome to Andrei's Calculator")

subprocess.run("clear", shell=True)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
 
def square(x, y):
    return x ** y
   
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

print("Operation Selection.")
print("")
print("use;")
print("(+) for Addition")
print("(-) for Subtraction")
print("(*)for Multiplication")
print("(%)for Division")
print("(^)for Square")

print("")
print("")
print("")
print("")
print("")
print("")
print("")


input("press enter to continue")

subprocess.run("clear", shell=True)

print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

while True:
    choice = input("input the symbol of the chosen operation: ")
   
   
    if choice in ('+', '-', '*', '%', '^'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))
           
        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))
           
        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '%':
            print(num1, "/", num2, "=", divide(num1, num2))
         
        elif choice == '^':
            print(num1, "**", num2, "=", square(num1, num2))
               
           
       
        next_calculation = input("Gusto mo pa ba? (oo/ayoko): ")
       

        if next_calculation == "ayoko":
          break
    else:
        print("Invalid Input")


