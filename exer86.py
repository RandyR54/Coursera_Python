mylist = list()
while True:
    value = raw_input('Enter a number: ')
    if value == 'done': break
    value = int(value)
    mylist.append(value)
print 'Maximum:' ,max(mylist)
print 'Minimum:' ,min(mylist)
    

