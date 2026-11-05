# fix_the_stats.py
# Count failed logins and calculate the average session length.
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Fix 1: Initialize the counter before the loop.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1
print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# Fix 2: Print the average after the loop.
# Fix 3: Use / to calculate the exact average.
print(f"Average session: {total / count} minutes")

# Fix 4: The stop value is not included, so use 5 to print Level 4.
for level in range(1, 5):
    print(f"Level {level}")
