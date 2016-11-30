def count(string,letter):
    count = 0
    for i in string:
        if i == letter:
            count = count + 1
    return(count)            

string = raw_input('Enter string:  ')
if len(string) == 0: 
    print 'No string entered.'
    quit()
letter = raw_input('Enter single character:  ')
if len(letter) != 1:
    print "Did not enter single character."
    quit()
letter_count = count(string,letter)
print 'The letter ' + str(letter) + ' appears ' + str(letter_count) + ' times.'


