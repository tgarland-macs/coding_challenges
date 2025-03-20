import pandas as pd

# Create Pandas DataFrame
df = pd.DataFrame({
    'product_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'low_fat': pd.Series(['Y', 'N', 'Y', 'Y', 'N', 'Y', 'N', 'N'], dtype='category'),
    'recyclable': pd.Series(['N', 'N', 'Y', 'N', 'N', 'Y', 'Y', 'N'], dtype='category')
})

# Check DataFrame and confirm data types
print(df.head())
print(df.dtypes)

def filtered_products():
    """
    Create a function that filters the DataFrame for products that are both low fat and recyclable, and returns their
    Product ID
    """
    filtered = df[(df['low_fat'] == 'Y') & (df['recyclable'] == 'Y')]

    return filtered[['product_id']]

# Call the function
if __name__ == '__main__':
    # Store the result in a new variable
    result = filtered_products()

    # Print the DataFrame head to confirm the result
    print(result.head())



