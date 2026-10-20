target = float(input("Enter a fraction between 0 and 1 (e.g., 0.1): "))
epsilon = 0.00001

f = target
result = 0.0
binary_fraction = "0."
power = 1
while abs(result - target) >= epsilon:
    f = f * 2
    integer_part = int(f)
    binary_fraction += str(integer_part)
    result += integer_part * (2 ** (-power))
    f = f - integer_part
    power += 1
print(f"Target decimal: {target}")
print(f"Binary representation: {binary_fraction}")
print(f"Approximated decimal value: {result}")
print(f"Absolute error: {abs(result - target):.8f}")
