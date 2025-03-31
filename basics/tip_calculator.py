def tip_data():
    # User to enter total bill amount
    try:
        bill_amount = float(input("Enter the total bill amount: "))
    except ValueError:
        print("Invalid bill amount. Please try again.")
        return None

    # User to enter tip percentage
    try:
        tip = float(input("Enter the tip percentage (e.g., 5%, 10%, 15%): ").replace("%", ""))
    except ValueError:
        print("Tip amount must not include '%' sign.")
        return None

    # User to enter number of users to divide the bill among
    try:
        number_of_people = int(input("Enter the number of people splitting the bill: "))
    except ValueError:
        print("Invalid number of people. Please enter a whole number, e.g., '4'.")
        return None

    return bill_amount, tip, number_of_people


# Function to calculate the tip
def tip_calculation(bill_amount, tip, number_of_people):
    # Calculate total bill, including tip
    total_cost = bill_amount + (bill_amount * (tip / 100))

    # Calculate how much each person has to contribute to the bill
    split_bill_amount = total_cost / number_of_people

    return split_bill_amount

def tip_calculator():
    # Run the tip_data function
    bill_amount, tip, number_of_people = tip_data()
    # Run the tip_calculation function
    split_bill_amount = tip_calculation(bill_amount, tip, number_of_people)
    print(f"Each person must pay ${split_bill_amount:.2f}")


if __name__ == '__main__':
    # Start the tip_calculator app
    tip_calculator()