# weight converter 

Weight=float(input("Enter weight : "))
unit=input("Enter unit (K for Kilograms, L for Pounds): ")

while True: 

    if unit.upper() == "K":
        converted_weight = Weight * 2.20462
        print(f"{Weight} Kilograms is equal to {round(converted_weight, 3)} Pounds.")
    elif unit.upper() == "L":
        converted_weight = Weight /2.20462
        print(f'{Weight} Pounds is equal to {round(converted_weight, 3)} Kilograms.')
    else:
        print("Invalid unit. Please enter 'K' for Kilograms or 'L' for Pounds.")
        
    again = input("Do you want to convert another weight? (y/n): ")
    if again.lower() == "y":
        continue
    elif again.lower() == "n":
        print("Thank you for using the weight converter!")
        break
    else:
        print("Invalid input")
        break
    
