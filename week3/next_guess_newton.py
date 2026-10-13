x = float(input("What x to find the cube root of? "))
guess = float(input("What guess to start with? " ))
print("Current estimate cube:", guess ** 3)
next_guess = guess - ((guess**3 - x) / (3 * (guess**2)))    
print("Next guess:", next_guess)
    
