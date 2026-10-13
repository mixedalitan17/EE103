num = int(input("Enter a number: "))
total_sum = 0
sum_display = "sum = "

i = 1
while i <= num:
    total_sum += i
    if i == 1:
        sum_display += str(i)
    else:
        sum_display += f"+{i}"
    i += 1

sum_display += f"={total_sum}"
print(sum_display)
sum_gauss = num * (num + 1) / 2
if total_sum == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")