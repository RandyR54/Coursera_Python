# Open file
file_handle = open('words.txt')

# Create empty dictionary and initialize blank line counter
my_words = dict()
blank_line_count = 0

# Read each line, get rid of spaces.  If two blank lines are encountered, stop reading.
# Assign each word as a key to the dictionary, all values will be 'qqq'

for line in file_handle :
    words = line.split()
    if len(words) == 0 : 
        blank_line_count = blank_line_count + 1
        if blank_line_count == 2: exit
    for word in words: 
        my_words[word] = 'qqq'
        
# Finally, print out the result
print my_words
  

