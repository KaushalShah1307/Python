inp = raw_input("PLease enter the file name here: ")
if len(inp) < 1: inp = "mbox-short.txt"
fhandle = open(inp)
timestamp = dict() 

for line in fhandle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        time.split()
        hour = time[:2]
        timestamp[hour] = timestamp.get(hour,0)+1

tuplist = list()
for [key, val] in timestamp.items():
    tuplist.append((key,val))
    tuplist.sort()

for key, val in tuplist:
    print key, val