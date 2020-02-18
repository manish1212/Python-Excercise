# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)

# # re-declaring the variable works


# # ERROR: variables of different types cannot be combined
print("this is a string" + str(123))

# Global vs. local variables in functions
def someFunction():
    global f
    f="def"
    print(f)

someFunction()
print(f)


#delete the vatiable
del f
print(f)