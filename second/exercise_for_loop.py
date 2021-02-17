# we put """ at the start and end of a sentence if we want to change line

quote = """ Alright, but apart from the Sanitation, 
the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Frensh-Water System, 
and Public Health, what have the Romans ever done for us? """

# Use a for loop and and if statement to print just the capitals in the quote above.

for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char)

