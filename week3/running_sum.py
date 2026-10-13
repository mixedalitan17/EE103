n = int(input("Enter a number to calculate the running sum: "))
running_sum = 0
for i in range(1, n + 1):
    running_sum += i

print(f"The running sum up to {n} is: {running_sum}")