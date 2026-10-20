s = "abcabc"
unique_letters = ""

for char in s:
    if char not in unique_letters:
        unique_letters += char
print(len(unique_letters))
