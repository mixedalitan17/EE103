num = int(input("Enter a number to calculate factorial (while loop): "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
    print(f"The factorial of {num} (using while) is: {factorial}")