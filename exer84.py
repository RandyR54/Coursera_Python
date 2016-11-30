file_name = raw_input('Enter file name: ')
file_handle = open(file_name)
final_list = list()

for line in file_handle:
    words = line.split()
    for i in range (len(words)):
        if (final_list.count(words[i]) != 0): continue
        final_list.append(words[i]) 
        
final_list.sort()        
print final_list
        
        