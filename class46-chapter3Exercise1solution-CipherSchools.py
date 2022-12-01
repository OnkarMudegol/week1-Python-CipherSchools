# Exercise Solution
winning_number = 27
user_input = input("guess a number b/w 1 and 100 : ")
user_input = int(user_input)
if user_input == winning_number:
    print("YOU WIN !!!")
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")