input1 = raw_input("Please enter your score here to evaluate the corresponding grade: ")
try:
    score = float(input1)
    if (score >= 0.9):
        print "A"
    elif (score >= 0.8):
        print "B"
    elif (score >= 0.7):
        print "C"
    elif (score >= 0.6):
        print "D"
    elif (score < 0.6):
        print "F"
        
except:
    print "Please enter a score in the proper range i.e. less than 1.0"
    quit()
    