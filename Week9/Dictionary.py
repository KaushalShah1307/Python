# count the no of occurrence of the words in the string

count = dict()
print "Enter the string here please: "
str = raw_input("")

for words in str:
    words = str.split()
#    print words
    
print "Counting...."
for word in words:
    count[word] = count.get(word,0) + 1

print words
print count

bigcount = None
bigword = None
for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
        
print "The word -", bigword, "is occuring", bigcount, "times in this string."
    