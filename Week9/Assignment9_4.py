# User prompt for the file
fname = raw_input("Please enter the file name here: ")
if len(fname) < 1: fname = "mbox-short.txt"

fhandle = open(fname)       #Open the file entered by the user

senders = list()        #Create a list to store the emails

for line in fhandle:
    if "From" not in line: continue
    if "From:" in line: continue
    line = line.split()
    email = line[1]
    senders.append(email)
print senders       #Prints emails in a list form

count = dict()      #Define a dictionary named count
for sender in senders:
    count[sender] = count.get(sender, 0) + 1
print count

maxsender = None
maxcount = None
for sender,count in count.items():
    if maxcount is None or count > maxcount:
        maxcount = count
        maxsender = sender
    
print maxsender, maxcount
 
