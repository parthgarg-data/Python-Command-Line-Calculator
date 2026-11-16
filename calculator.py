import math
def addition(a,b):
    return a+b
  
def subtraction(a,b):
    return a-b
    
def multiplication(a,b):
    return a*b
    
def division(a,b):
    if b!=0:
         return a/b
    else:
         print("Can't divide by zero")
         return None

def modulus(a,b):
    if b!=0:
        return a%b
    else:
        print("Cannot calculate modulus with zero")
        return None

def power(a,b):
    return a**b

def sqrrt(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        print("Cannot calculate square root of negative number")
        return None

def percentage(a, b):
    return (a / 100) * b

def floor_division(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
        return None
    return a // b

def absolute_value(a):
    return abs(a)

def factorial(a):
    if a < 0 or not a.is_integer():
        print("Error: Factorial requires a non-negative integer")
        return None
    return math.factorial(int(a))

def square(a):
    return a ** 2

def cube(a):
    return a ** 3



while True:        
    print("\n========== SMART CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Percentage")
    print("9. Floor Division")
    print("10. Absolute Value")
    print("11. Factorial")
    print("12. Square")
    print("13. Cube")
    print("14. Exit")
    try:
        ch=int(input("Enter your choice : "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if ch==14:
        print("calculator closed")
        break
    
    elif ch < 1 or ch > 13:
        print("Invalid Choice")


    elif ch in (7, 10, 11, 12, 13):
        try:
            a = float(input("Enter number: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if ch == 7:
            result = sqrrt(a)
        elif ch == 10:
            result = absolute_value(a)
        elif ch == 11:
            result = factorial(a)
        elif ch == 12:
            result = square(a)
        elif ch == 13:
            result = cube(a)

        if result is not None:
            print("Result:", result)

    else:
        try:
            a=float(input("Enter First number : "))
            b=float(input("Enter Second Number : "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if ch==1:
            result=addition(a,b)
            
        elif ch==2:
            result=subtraction(a,b)

        elif ch==3:
            result=multiplication(a,b)

        elif ch==4:
            result=division(a,b)

        elif ch==5:
            result=modulus(a,b)
            
        elif ch==6:
            result=power(a,b)
            
        elif ch == 8:
            result = percentage(a, b)

        elif ch == 9:
            result = floor_division(a, b)

        if result is not None:
            print("Result:", result)




