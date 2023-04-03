# collatz.py

# In this program the user inputs any positive integer 
# and outputs the successive values of the following calculation:
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one.

#Authour: Dorina Agache

number = int(input("Please enter a positive number: "))
sequence = [number] # creating a list 

while number != 1:
    if number % 2 == 0: #checking if number is even
            number = number // 2 #dividing by 2
            
    else: #if number not even
            number = number * 3 + 1 # multiplying by 3 and adding 1
    sequence.append(number)

print(sequence)