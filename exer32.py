hours = raw_input('Enter hours:  ')
try:
  hours = float(hours)
  rate = raw_input('Enter Rate:  ')
  rate = float(rate) 

  if (hours <= 40.0) :
    pay = hours * rate
  else :
    overtime_hours = hours - 40.0 
    overtime_rate = rate * 1.5 
    pay = (40.0 * rate) + (overtime_hours * overtime_rate)

  print ('Pay:  '), pay

except:
  print ('Error, please enter numeric input')