bill_amount = input("Enter the total bill amount: ")
print(round(int(bill_amount, 2)))

tip = input("Enter the tip percentage (e.g., 5%, 10%, 15%): ")
print(round(int(tip, 2)))

number_of_people = input("Enter the number of people splitting the bill: ")

tip_multiplier = 100 + int(tip)

calculated_bill = bill_amount * round(int(tip_multiplier), 2)) / number_of_people

print(f"Each person has to pay ${calculated_bill}")

