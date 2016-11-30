file_name = raw_input('Enter the file name: ')
try:
    file_handle = open(file_name)
except:
    if file_name == 'na na boo boo' :
        print "NA NA BOO BOO TO YOU - You have been punk'd!"
        exit()
    print 'File cannot be opened:', file_name
    exit()

if file_name == 'na na boo boo' :
    print "NA NA BOO BOO TO YOU - You have been punk'd!"
    exit()
    
count = 0
for line in file_handle:
    if line.startswith('Subject:') :
        count = count + 1
print 'There are', count, 'subject lines in', file_name