# This program will read mbox-short.txt or mbox.txt and print out the email address of the person with the most entries.

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
# Read all the data and store the email addresses and counts in the dictionary
for line in file_handle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] == check_value:
        if words[1] not in my_dict:
            my_dict[words[1]] = 1
        else:
            my_dict[words[1]] += 1
#
# After all the data has been read, print the person with the most entries by creating a list (count,email) tuples
# from the dictionary.  Sort the list in reverse order and print result.
#addresses = my_dict.keys()
lst = list()
for key in my_dict.keys() :
    lst.append ((my_dict[key], key))
# Sort they list based on value (count), largest count first
lst.sort(reverse=True)
res = lst[0]
print res[1], res[0]