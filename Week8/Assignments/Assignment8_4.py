fname = raw_input("Please enter the file name here: ")
fhandle = open(fname)
lst = []
for line in fhandle:
    line = line.rstrip().split()
    for word in line:
        if word not in lst: 
            lst.append(word)
lst.sort()
print lst

        