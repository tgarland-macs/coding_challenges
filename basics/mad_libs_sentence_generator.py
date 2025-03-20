import random

"""
The following is designed to demonstrate an understanding of string variables,
f-strings and creating a basic list.

It also includes the random package for a little extra fun.
"""

# Add variable for noun, and add hint.
noun: str = input("Name your favourite animal: ")
# Add variable for verb, and add hint.
verb: str = input("Please explain what the main character does in the story (verb): ")
# Add variable for adjective, and add hint.
adjective: str = input("Describe the main character in one word (adjective): ")
# Add variable for place, and add hint.
place: str = input("Where is your main character (place)? ")

# Create a list of stories to use.
stories = [
    f"The {adjective} {noun} {verb} over the fence at the {place}.",
    f"One day, a {adjective} {noun} {verb} into a {place}. They were never seen again.",
    f"You can never let a {adjective} {noun} {verb} into a {place}."
]

# Once all inputs have been created, populate a random story and print the story to the terminal.
print("Here's your Mad Libs story! Enjoy 😊")
print(random.choice(stories))

