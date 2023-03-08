# accounts.py
# This program that reads in a 10 character account number 
# and outputs the account number with only the last 4 digits showing 
# Author: Dorina Agache

accountNo = input("Please enter you account number:")

#this syntax slices a string from the specified index until the end
print(f"XXXXXX{accountNo[6:]}")
