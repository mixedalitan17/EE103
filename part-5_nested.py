import time

total_tickets = 1000
print("--- Running Nested Loops (Guess & Check) ---")
start_nested = time.time()

alyssa_nested = None
found = False
for alyssa in range(20, total_tickets + 1):
    for ben in range(total_tickets + 1):
        for cindy in range(total_tickets + 1):
            if (alyssa + ben + cindy == total_tickets) and (ben == alyssa - 20) and (cindy == 2 * alyssa):
                alyssa_nested = alyssa
                found = True
                break
        if found:
            break
    if found:
        break
    end_nested = time.time()
nested_duration = end_nested - start_nested
print(f"Alyssa sold: {alyssa_nested} tickets")
print(f"Nested loops execution time: {nested_duration:.4f} seconds\n")