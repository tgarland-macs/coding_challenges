import pandas as pd

# Let's create a DataFrame for customers where the Primary Key is 'id'
customers = pd.DataFrame({
    'id':['1', '2', '3', '4', '5'],
    'name':['Joe', 'Henry', 'Sam', 'Max', 'Brett']
})

# Then we create a DaraFrame for orders with a Foreign Key of 'customerId'
orders = pd.DataFrame({
    'id':['1', '2', '3'],
    'customerId':['2', '4', '5']
})

"""
Finally, we can create a new DataFrame that only returns 'id' and 'name' from customers where the 'id' from
customers matches the 'customerId' in order using the isin() function from Pandas.
"""
customers_with_no_orders = customers[~customers['id'].isin(orders['customerId'])]

# Print the result to check our work.
print(customers_with_no_orders)