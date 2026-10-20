f = float(input("Enter a fraction between 0 and 1 (e.g., 0.375): "))
binary_fraction = "0."
max_bits = 32
bit_count = 0

while f > 0 and bit_count < max_bits:
    f = f * 2
    integer_part = int(f)
    binary_fraction += str(integer_part)
    f = f - integer_part
    bit_count += 1

print(f"Binary representation: {binary_fraction}")