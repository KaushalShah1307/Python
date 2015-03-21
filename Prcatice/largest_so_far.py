largest_so_far = -1
count = 0
found = False
print "Initial starting point no is: ", largest_so_far
for new_no in [12, 7, 19, 54, 42, 75]:
    count = count + 1
    if new_no > largest_so_far:
        largest_so_far = new_no
    print "The new largest no is: ", largest_so_far
    if largest_so_far == 75:
        found = True
    print "Yes the value is found and is correct", found
print "Final destination point no is: ", largest_so_far
print "Total no of loops for the execution of the program is: ", count