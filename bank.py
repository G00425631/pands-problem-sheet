# bank.py
# This program adds two sums of cents and converts into euros
# Author:Dorina Agache
#REF: FOR DECIMAL POINT https://www.w3schools.com/python/python_string_formatting.asp

cent1= int(input('Enter amount1 (in cent):'))
cent2= int(input('Enter amount2 (in cent):'))

sum= (cent1 +cent2)/100

print(f'The sum of these is €{sum:.2f}')