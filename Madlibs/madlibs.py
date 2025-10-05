print("Welcome to the Mad Libs!")
print("Please provide the following words.")

adjective1 = input("Adjective: ")
adjective2 = input("Adjective: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
animal = input("Animal: ")
verb = input("Verb: ")
place = input("Place: ")

madlib = f"Today I went to the {place}. I saw a {adjective1} {animal} jump over a {noun1}.\
Then it started to {verb} near a {adjective2} {noun2}. It was the most exciting day ever!"

print(madlib)