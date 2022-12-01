# ask user for name
# Example - Ankit Diwakar
# print count of each other
# out put :
         # A : 2
         # n : 1
         # k : 2
         # i : 2
         # t : 1
         #   : 1
         # D : 1
         # i : 2
         # w : 1
    

name = input("please enter your name ")
# harshit vashisth
# harshit , len = 7 - 1 = 6
# name.count("h") , name.count(name[0]) = 2
# name.count("a") , name.count(name[1]) = 1
# name.count("r") , name.count(name[2]) = 1
# name.count("s") , name.count(name[3]) = 1
# name.count("h") , name.count(name[4]) = 2
# name.count("i") , name.count(name[5]) = 1
# name.count("t") , name.count(name[6]) = 1

# output
# h = 2
# a = 1
# r = 1
# s = 1
# h = 2
# i = 1
# t = 1
temp_var = "h" # for word whose show double
i = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1