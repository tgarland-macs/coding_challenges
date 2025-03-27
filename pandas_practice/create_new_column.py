import pandas as pd

# First let's create a new DataFrame
df = pd.DataFrame({
    'name':['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary':[4548, 28150, 1103, 6593, 74576, 2433]
})

# Now let's add a new column 'bonus', that calculates each person's bonus as 10% of their salary
df['bonus'] = df['salary'] * 0.10

# Round to nearest dollar by converting from a float to an integer
df['bonus'] = df['bonus'].astype(int)

# Now we can check the result to confirm it's accurate
print(df.head())