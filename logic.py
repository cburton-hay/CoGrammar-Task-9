# Weather app that tells you what to wear given the current temperature outside
temp = input("What is the current temperature outside?")
try:
    temp = int(temp)
except:
    temp = input("Error. Please enter the temperature as a whole number.")
    temp = int(temp)
if temp > 8: # Should be less than symbol as cold temps mean you need additional layers of clothing to keep warm.
    print("Make sure you have a cosy coat on.")
elif temp < 19: # Should be greater than symbol as warm and sunny weather means you should wear UV protection.
    print("Don't foret to have UV protection.")
else:
    print("Best to take a light jacket just in case!")
# The code runs but thhe output does not make sense for the temperatures provided.