# Calculator 
a=float(input("enter a number:"))
b=float(input("enter another number:"))
fn=input("enter fn (+ , - ,*,/,%,**): ")


if fn== "+":
    print(a+b)
elif fn == "-":
    print(a-b)
elif fn== "*":
    print(a*b)
elif fn=="/":
    print(a/b)
elif fn=="%":
    print(a%b)
elif fn=="**":
    print(a**b)
else:
    print("invalid function")