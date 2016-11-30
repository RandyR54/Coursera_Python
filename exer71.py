file_name = raw_input('Enter a file name: ')
try:
    file_handle = open(file_name)
except:
    print 'File cannot be found:', file_name
    exit()

file_handle = open('mbox-short.txt')
for line in file_handle:
    line = line.upper()
    print line