def computepay(hours,rate):
    try:
        hours = float(hours)
        rate = float(rate)
    except:
        print ('Error, please enter numeric input') 
        quit()        

#    print ('Enter Hours:  '), hours
#    print ('Enter Rate:  '), rate
    if (hours <= 40.0) :
        pay = hours * rate
    else :
        overtime_hours = hours - 40.0 
        overtime_rate = rate * 1.5 
        pay = (40.0 * rate) + (overtime_hours * overtime_rate)
    return pay

hours = raw_input('Enter hours:  ')
hours = float(hours)
rate = raw_input('Enter Rate:  ')
rate = float(rate)
x = computepay(hours,rate)
print x

