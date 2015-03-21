input1 = raw_input("Please enter the hours of your work: ")
Hours = float(input1)
input2 = raw_input("Please enter your hourly rate: ")
Rate = float(input2)
if (Hours <= 40) :
    Pay = (Hours * Rate)
else :
    Pay = (40 * Rate) + ((Hours - 40) * 1.5 * Rate)
print "Your Gross Pay is: ", Pay