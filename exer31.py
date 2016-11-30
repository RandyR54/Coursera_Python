overtime_hours = 0
hours = raw_input('Enter hours:  ')
rate = raw_input('Enter Rate:  ')

if (float(hours) <= 40.0) :
  pay = float(hours) * float(rate)
else :
  overtime_hours = float(hours) - 40.0 
  overtime_rate = float(rate) * 1.5
  pay = (40.0 * float(rate)) + (overtime_hours * float(rate) * 1.5)

print ('Pay:  '), pay

