cube = int(input("Enter an integer number: ")) 
abs_cube = abs(cube)
guess = 0
while guess ** 3 < abs_cube:
    guess += 1
if guess ** 3 != abs_cube:
    print(f"{cube} is not a perfect cube.")
else:
    if cube < 0:
        guess = -guess
    print(f"Cube root of {cube} is {guess}.")