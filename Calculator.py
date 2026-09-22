#Calculator With Menu 

def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b    
def division(a, b):
    if b==0:
        return "Denominator cannot be zero"
    else:
        return a / b
def modulus (a, b):
    if b==0:
        return "Denominator cannot be zero"
    else:
        return a % b
def power(a, b):
    return a ** b



while True:
    print("_____Calculator With Menu_______")
    print("1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Modulus\n 6. Power \n 7. Exit")
    
    function = int(input("Enter your function number: "))
    
    if function in [1,2,3,4,5,6,]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if function == 1:
            print("Result: ", addition(a, b))
        elif function == 2:
            print("Result: ", subtraction(a, b))
        elif function == 3:
            print("Result: ", multiplication(a, b))
        elif function == 4:
            print("Result: ", division(a, b))
        elif function == 5:
            print("Result: ", modulus(a, b))
        elif function == 6:
            print("Result: ", power(a, b))
    elif function == 7:
        print("Exiting.....")
        break
    else: 
        print(f'{function} is an invalid input. Please enter a valid function number.')
