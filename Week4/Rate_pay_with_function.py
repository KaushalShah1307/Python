def computepay(Hours, Rate) :
    print "The computepay function starts here!!"
    if (Hours <= 40) :
        Pay = (Hours * Rate)
    else :
        Pay = (40 * Rate) + ((Hours - 40) * 1.5 * Rate)
    return Pay

input1 = raw_input("Please enter the hours of your work: ")
Hours = float(input1)
input2 = raw_input("Please enter your hourly rate: ")
Rate = float(input2)
print "Your Hours of work and Rate is ", Hours, "&", Rate, "respectively"
Pay = computepay(Hours, Rate)
print "Your Gross Pay is: ", Pay
