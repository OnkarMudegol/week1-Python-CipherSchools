# problem
# example - 1256
# calculate 1+2+3+4+5 and print

number = input("enter a number ")
# "1256" # len = 4 
 
total = 0
i = 0
while i<len(number):
    total += int(number[i])
    i += 1
print(total)