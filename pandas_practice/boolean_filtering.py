import pandas as pd

# Let's create a simple Pandas DataFrame
df = pd.DataFrame({
    'film_stock': ['Kodak Porta', 'Kodak Ektar', 'Ilford HP5', 'CineStill Tungsten'],
    'film_iso': ['400', '100', '200', '400'],
    'film_type': ['Colour', 'Colour', 'Black & White', 'Colour']
}
)

# Return the DataFrame to check
# print(df.head())

# Now let's apply a filter that returns just black and white film
black_and_white = df[(df['film_type'] == 'Black & White')]
print(black_and_white.head())

# And now only for colour
colour = df[(df['film_type'] == 'Colour')]
print(colour.head())

# Now let's return film that is both colour and ISO 400
colour_and_iso_400 = df[(df['film_type'] == 'Colour') & (df['film_iso'] == '400')]
print(colour_and_iso_400.head())