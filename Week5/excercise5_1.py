# Program to get input of numbers and getting their sums and average

sum = 0
count = 0
while True:
    inp = raw_input("Please enter a no here: ")
    
    if inp == "done": break
    if len(inp) < 1: break
    
    try:
        num = float(inp)
    except:
        print "ERROR!! Please enter a valid no and not a text"
        continue
                
    sum = sum + num
    count = count + 1    
    print "The no you have entered is: ", num
    print "The sum of the no you have entered is: ", sum
    print "The total count on the no of loops for the program is: ", count
    print "The Average of the sum of the no you have entered is: ", (sum/count)