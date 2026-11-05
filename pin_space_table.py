# pin_space_table.py
# Estimate the time needed to try every PIN from 4 to 8 digits.
GUESSES_PER_SECOND = 10
SECONDS_PER_MINUTE = 60
SECONDS_PER_DAY = 24 * 60 * 60

for digits in range(4, 9):
    combinations = 10 ** digits
    seconds = combinations // GUESSES_PER_SECOND
    minutes = seconds // SECONDS_PER_MINUTE
    days = seconds // SECONDS_PER_DAY
    print(f"{digits} digits: {combinations} PINs, {minutes} minutes, {days} days")
