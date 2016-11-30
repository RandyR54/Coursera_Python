# This program will read either mbox.txt or mbox-short.txt and count the number of unique email addresses.
# Look for lines that start with "From", then look for the 2nd word, and keep a running total.
# Print out the email address of the person with the most messages, and the number of messages

# Start by entering the filename, use mbox.txt or mbox-short.txt
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
    words = line.split()
    if len(words) == 0 : continue
    if words[0] == check_value:
        if words[1] not in my_dict:
            my_dict[words[1]] = 1
        else:
            my_dict[words[1]] += 1
#
# Now determine the user with the most emails using a maximum loop
max_number = None
addresses = my_dict.keys()
for key in addresses :
    if max_number is None or my_dict[key] > max_number :
        max_number = my_dict[key]
        email_address = key
#
print email_address, max_number
    