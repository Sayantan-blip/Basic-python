def calculate_bill(units):
    if units <= 0:
        print("Invalid input! Units cannot be negative.")
        return

    if units <= 100:
        bill = units * 5

    elif units <= 300:
        bill = (100 * 5) + (units - 100) * 7

    else:
        bill = (100 * 5) + (200 * 7) + (units - 300) * 10

    bill = bill + 100  # Fixed charge

    print("Total electricity bill: ₹", bill)


units = float(input("Enter units consumed: "))

calculate_bill(units)
