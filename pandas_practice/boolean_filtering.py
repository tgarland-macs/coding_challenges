import pandas as pd

# Let's create a simple Pandas DataFrame
df = pd.DataFrame({
    'film_stock': ['Kodak Porta', 'Kodak Ektar', 'Ilford HP5', 'CineStill Tungsten'],
    'film_iso': ['400', '100', '200', '400'],
    'film_type': ['Colour', 'Colour', 'Black & White', 'Colour']
}
)

# Now let's apply a filter that returns just black and white film
black_and_white = df[(df['film_type'] == 'Black & White')]
print("B&W Check:\n", black_and_white.head())

# And now only for colour
colour = df[(df['film_type'] == 'Colour')]
print("Colour film check:\n", colour.head())

# Finally, let's return film that is both colour and ISO 400
colour_and_iso_400 = df[(df['film_type'] == 'Colour') & (df['film_iso'] == '400')]
print("Final filtered DataFrame:\n", colour_and_iso_400.head())