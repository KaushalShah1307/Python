# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fhandle = open(fname)
    for line in fhandle:
        line = line.rstrip().upper()
        print line
    
except IOError as err:
    print str(err)