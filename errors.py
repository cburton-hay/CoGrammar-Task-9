# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # Missing brackets as syntax error
print("\n") # Indented when shouldn't have been - syntax error.

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #Unexpected indent (syntax error) as well as variable not properly assigned. deleted one for the =
age = int(age_Str) # "years old can't be converted into an integer as they have no numerical value."
print("I'm " + str(age) + "-years-old.") # to concatinate must be string + string so converted age back to a string. Needed additional " " to separate theh words.

# Variables declaring additional years and printing the total years of age
years_from_now = 3 # Indented when shouldn't be. Changed from string to int so it has numerical value.
total_years = age + years_from_now

print("The total number of years: " + str(total_years)) # Missing brackets around the print statement - syntax error. Added space at the end of the string to have space between characters. Changed the variable name to total_years to match previous statement. Converted total_years to string to be concatinated.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # correct variable name is total_years
print("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old") # brackets around print statement. Added 6 to the total_months to given correct calculation for the extra half year. Convert total_months to string to concatinate. 

#HINT, 330 months is the correct answer

