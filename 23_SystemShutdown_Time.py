# Program to shutdown system
#Input: minute

import os

minute = int(input("Enter in how many minute you want to shutdown your system"))

os.system(f"shutdown -s -t {minute*60}")
print('To cancel shutdown type "shutdown -a" ')