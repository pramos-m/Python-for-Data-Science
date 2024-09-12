import time
from datetime import datetime

# time.time gives seconds since 1 of january of 1970
seconds_since_epoch = time.time();

# f"{seconds_since_epoch:.4f}" ensures seconds are shown with 4 decimals
# format(seconds_since_epoch, '.2e') convert the number to scientific notation
print(f"Seconds since January 1, 1970: {seconds_since_epoch:,.4f} or {format(seconds_since_epoch, '.2e')} in scientific notation")

# datetime.now() obtains current date and time
current_time = datetime.now()

# strftime("%b %d %Y") formats date as:
# %b : abbreviation of the name of the month
# %d : Day of the month (with digits)
# %Y : year with four digits
formatted_date = current_time.strftime("%b %d %Y")

print(formatted_date)
