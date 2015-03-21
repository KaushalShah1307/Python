# Program to learn to use Try & Except

input1 = raw_input("Please enter the hours your have worked: ")

try: 
    Hours = int(input1)
    print Hours
    
except: 
    Hours = -1
    print "There is an error here"