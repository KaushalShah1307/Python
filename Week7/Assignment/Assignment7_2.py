filename = raw_input("Please type the file name here: ")
count = 0
total = 0.0
Avg = 0.0
filehandle = open(filename)
for line in filehandle:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    line = line[20:].rstrip()
    total = total + float(line)
    Avg = total / count
#    print line 
print "Average spam confidence: ", Avg