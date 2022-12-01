# take two comma seperated input from user
# 1.) user's name
# 1.)a single charecter

# output - 2 print lines
# 1.) user's name lenght
# 2.) count the charecter that user inputed(case insensetive count)
name,char=input("Enter name and char here: ").split(",")
print(f"{len(name)}")
print(f"{name.lower().count(char.lower())}")

