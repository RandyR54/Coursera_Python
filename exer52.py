smallest = None
largest = None

while True:
    user_input = raw_input('Enter a number:  ')
    if (user_input == 'done') or (len(user_input) < 1): break  # Also ends on empty input
    try:
        user_input_int = int(user_input)
    except:         
        print 'Invalid input'
        continue
    if (smallest is None) or (user_input_int < smallest):
        smallest = user_input_int
    if (largest is None) or (user_input_int > largest):
        largest = user_input_int
    
print "Maximum is", largest
print "Minimum is", smallest