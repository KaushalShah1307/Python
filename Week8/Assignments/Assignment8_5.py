file = raw_input("Please enter your file here: ")
if len(file) < 1 : file = "mbox-short.txt"
filehand = open(file)
count = 0

for line in filehand:
    if "From" not in line: continue
    if "From:" in line: continue
    line = line.rstrip().split()
    email = line[1]
    print email
    count = count + 1    
print "There were", count, "lines in the file with From as the first word"
   