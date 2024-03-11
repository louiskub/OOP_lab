import random
import string
from datetime import datetime, timedelta
import time


# Get the current time in seconds since the epoch
start_time = time.time()

def check_password(password):
        for char in password:
            if char.isnumeric() or char.isalpha() or char == '_' or char == '.':
                continue
            return False
        
# a = input()
# print(check_password(a))

# Generate a random character from A-Z or 0-9
random_char = random.choice(string.ascii_uppercase + string.digits)

print(f"Random character: {random_char}")


# Set the desired length of the random string
length = 12

# Generate a random string of 12 characters from A-Z and 0-9
random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

print(f"Random string: {random_string}")

# Define the start and end dates
start_date = datetime(2022, 12, 31)
end_date = datetime(2023, 2, 1)

# Generate a list of dates within the specified range
date_list = [start_date + timedelta(days = x) for x in range((end_date - start_date).days + 1)]

# Print the list of dates
for date in date_list:
    print(date.strftime('%Y-%m-%d'))


# Your code or task to be timed
# ...

# Calculate the elapsed time
elapsed_time = time.time() - start_time

print(f"Elapsed time: {elapsed_time:.10f} seconds")

