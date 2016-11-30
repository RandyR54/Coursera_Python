file_name = raw_input('Enter a file name: ')
try:
    file_handle = open(file_name)
except:
    print 'File cannot be found:', file_name
    exit()

total = 0.0
count = 0
check_value = 'X-DSPAM-Confidence:'
check_value_length = len(check_value)   
 
for line in file_handle:
    if line.startswith(check_value) :
        count = count + 1
        line = line.rstrip()
        line_length = len(line)
        number = line[check_value_length:]
        number = float(number)
        total = total + number

average = total / count
print 'Average spam confidence:', average
        
        