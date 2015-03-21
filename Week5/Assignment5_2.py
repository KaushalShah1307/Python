# Program to get input of numbers from user and getting the min and the max

min = None
max = None
while True:
    num = raw_input("Please enter a no here: ")
    if num == "done": break
    
    try:
        num = float(num)
    except:
        print "Invalid input"
        continue
    
    if min is None or num < min:
        min = num
    elif max is None or num > max:
        max = num
        
print "Maximum", max
print "Minimum", min
    
    