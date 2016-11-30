count = 0
total = 0
average = 0
while True:
    user_input = raw_input('Enter a number:  ')
    if (user_input == 'done'):
        break
    try:
        user_input_int = int(user_input)
    except:         
        print 'Invalid input'
        continue
    count = count + 1
    total = total + user_input_int
average = float(total) / count
print total, count, average