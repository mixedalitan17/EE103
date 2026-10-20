# EE 103 - Week 4
# Part 1: Recap

# 1) User Input, Type Casting, & String Formatting
raw_std = input("Enter your student number: ")
std_num = int(raw_std)
print(f"Hello, my student number is {std_num}!")

# 2) String Manipulation & Slicing
name_lower = 'name'
name_upper = name_lower.upper()
name_reversed = name_lower[::-1]
print(f"Uppercase: {name_upper}")
print(f"Reversed: {name_reversed}")

# 3) User Input with Floats & Basic Arithmetic
this_year = 2026
this_year_str = str(this_year)
first_two = float(this_year_str[:2])
last_two = float(this_year_str[2:])

mysum = first_two + last_two
print(f"{mysum:.2f}")

if mysum == 46:
    print("Correct")
else:
    print("Wrong")
    