import pandas as pd

customers = pd.DataFrame({
    'id':['1', '2', '3', '4', '5'],
    'name':['Joe', 'Henry', 'Sam', 'Max', 'Brett']
})

orders = pd.DataFrame({
    'id':['1', '2', '3'],
    'customerId':['2', '4', '5']
})

customers_with_no_orders = customers[~customers['id'].isin(orders['customerId'])]

# result = customers_with_no_orders['name'].rename('customers').to_frame()

print(customers_with_no_orders)