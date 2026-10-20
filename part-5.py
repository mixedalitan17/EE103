import time

total_tickets = 1000

print("--- Running Single Loop (Optimized) ---")
start_single = time.time()

alyssa_single = None
for alyssa in range(20, total_tickets + 1):
    ben = alyssa - 20
    cindy = 2 * alyssa
    if alyssa + ben + cindy == total_tickets:
        alyssa_single = alyssa
        break

    end_single = time.time()
single_duration = end_single - start_single
print(f"Alyssa sold: {alyssa_single} tickets")
print(f"Single loop execution time: {single_duration:.6f} seconds")