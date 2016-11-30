# input file is mbox-short.txt
file_name = raw_input('Enter file name: ')
file_handle = open(file_name)
count = 0

for line in file_handle:
    words = line.split()
    if len(words) < 2: continue
    if words[0] != 'From': continue
    count = count + 1
    address = words[1] 
    print address
print 'There were', count, 'lines in the file with From as the first word'
        
        