num = int(input("Enter a number to calculate factorial (for loop): "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} (using for) is: {factorial}")