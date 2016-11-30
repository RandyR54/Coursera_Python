str = 'X-DSPAM-Confidence: 0.8475'
num_pos = str.find('0')
end_pos = len(str)
number = str[num_pos:end_pos]
#print number
float_num = float(number)
print float_num
#add_one = float_num + 1
#print add_one
