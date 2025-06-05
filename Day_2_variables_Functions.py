import math  # Import math module to use mathematical functions like pi and power

# String variables
first_name = 'Hayden'             # User's first name
last_name = 'Williamson'          # User's last name
full_name = 'Hayden Williamson'  # Full name, combining first and last
country = 'United States of America'  # Country of residence
city = 'New York'                 # City of residence

# Integer variables
age = 300                        # User's age 
current_year = 2025              # Current year

# Boolean variables
is_married = False              # Marital status
is_true = True                  # Arbitrary true value
is_light_on = True              # Light switch status (on)

# Multiple variable assignments on one line
birth_year, is_not_married, pet_name, is_light_off = 2006, True, 'Blue', False  
# birth_year: user's birth year
# is_not_married: marital status
# pet_name: name of user's pet
# is_light_off: light switch status (off)

# Level two of the challenge: Display data types of variables (excluding multiple assignments)
print(type(first_name))          # string
print(type(last_name))           # string
print(type(full_name))           # string
print(type(country))             # string
print(type(city))                # string
print(type(age))                 # int
print(type(current_year))        # int
print(type(is_married))          # boolean
print(type(is_true))             # boolean
print(type(is_light_on))         # boolean


# Finding the length of first_name and last_name variables 
print(len(first_name))           # Length of first_name 
print(len(last_name))            # Length of last_name 

# Comparing lengths of first_name and last_name and printing the difference
print(len(first_name) - len(last_name))  # Difference in length between first and last names

# Arithmetic operations
num_1 = 5
num_2 = 4

total = num_1 + num_2            # Addition
diff = num_2 - num_1             # Subtraction
product = num_2 * num_1          # Multiplication
division = num_1 / num_2         # Division (float result)
remainder = num_1 % num_2        # Modulus (remainder of division)
exp = num_1 ** num_2             # Exponentiation (num_1 raised to num_2)
floor_division = num_1 // num_2  # Floor division (quotient without remainder)

# Calculating the area and circumference of a circle with a radius of 30 meters
area_of_circle = math.pi * pow(30, 2)         # Area = πr²
circum_of_circle = 2 * math.pi * 30            # Circumference = 2πr

# Calculating the area of a circle based on user input radius
user_radius = int(input('Give a whole number for a new radius: '))  # Ask user for radius as integer
area_of_circle = math.pi * pow(user_radius, 2)                    # Calculate area using user input

print('The aSrea of the circle using the radius ', user_radius, ': ', area_of_circle)

# Prompting user for personal details
# Prompt the user to enter their first name and store it in a variable
user_first_name = input('Enter your first name: ')

# Prompt the user to enter their last name and store it in a variable
user_last_name = input('Enter your last name: ')

# Prompt the user to enter their country of residence and store it
user_country = input('Enter your country: ')

# Prompt the user to enter their age as a string
user_age = input('Enter your age: ')
