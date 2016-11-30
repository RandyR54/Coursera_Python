# This program will read mbox-short.txt and count the number of unique domain names.
# Look for lines that start with "From", then look for the 2nd word, and keep a running total.
# The second word must be modified to save everything after the @ character.
# Finally, print out the results
import string
# Start by entering the filename, use mbox-short.txt
file_name = raw_input('Enter a file name: ')
try:
    file_handle = open(file_name)
except:
    print 'File cannot be found:', file_name
    exit()
#
check_value = 'From'
my_dict = dict()
#
for line in file_handle:
    line = line.replace('@', ' ')
    words = line.split()
    if len(words) == 0 : continue
    if words[0] == check_value:
        if words[2] not in my_dict:
            my_dict[words[2]] = 1
        else:
            my_dict[words[2]] += 1
print my_dict
    