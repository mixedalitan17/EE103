num = int(input("Enter an integer: "))
if num == 0:
    binary_str = "0"
else:
    is_negative = num < 0
    n = abs(num)
    
    remainders = ""
    while n > 0:
        remainder = n % 2
        remainders += str(remainder)
        n = n // 2
        binary_str = remainders[::-1]
    
    if is_negative:
        binary_str = "-" + binary_str

print(f"Decimal: {num}")
print(f"Binary: {binary_str}")