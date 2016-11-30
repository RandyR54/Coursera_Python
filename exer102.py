# This program will read mbox-short.txt or mbox.txt and print out the distribution of the hours found on the From line.

import string
# Start by entering the filename, use mbox-short.txt or mbox-txt
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
# Read all the data and store the hours (5th field is time) and counts in the dictionary
for line in file_handle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] == check_value:
        time = words[5]
        hms = time.split(':')
        hour = hms[0]
        if hour not in my_dict:
            my_dict[hour] = 1
        else:
            my_dict[hour] += 1
#
# Create a list of hour / count values and sort by hour, smallest first  
lst = list()
for key in my_dict.keys() :
    lst.append ((key, my_dict[key]))
lst.sort()

# Print the counts, one per line, sorted by hours
for hr, count in lst :
    print hr, count
