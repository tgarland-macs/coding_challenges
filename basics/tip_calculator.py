def tip_data():
    # User to enter total bill amount
    bill_amount = input("Enter the total bill amount: ")

    # User to enter tip percentage
    tip = input("Enter the tip percentage (e.g., 5%, 10%, 15%): ")
    tip = tip.strip('%')

    # User to enter number of users to divide the bill among
    number_of_people = input("Enter the number of people splitting the bill: ")

    return bill_amount, tip, number_of_people

# Function to calculate the tip
def tip_calculator(bill_amount, tip, number_of_people):
    bill_amount = float(bill_amount)
    tip = "1." + tip
    tip = float(tip)
    number_of_people = int(number_of_people)

    split_bill = bill_amount * tip

    divide_by_number_of_people = split_bill / number_of_people

    return divide_by_number_of_people


if __name__ == '__main__':
    bill_amount, tip, number_of_people = tip_data()
    divide_by_number_of_people = tip_calculator(bill_amount, tip, number_of_people)
    final_amount = divide_by_number_of_people
    print(f"Each person should pay: ${final_amount:.2f}")