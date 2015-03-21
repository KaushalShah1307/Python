minimum = None
maximum = None

while True:
    inp = raw_input('Enter a number: ')
    if inp == 'done': 
        break

    try:
        num = float(inp)
    except:
        print 'Invalid input'
        continue                            

    if minimum is None or num < minimum:
        minimum = num

    if maximum is None or num > maximum:
        maximum = num

print 'Maximum:', maximum
print 'Minimum:', minimum