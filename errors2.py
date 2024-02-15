# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "lion" # Needs "" to show that it is a string. Does not need a capital as it appears in the middle of a sentence or can use the lower function within full_spec
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # Requires f to use f-string formatting. The variables were written in the wrong position.

print(full_spec) # Required brackets around the print statement