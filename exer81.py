def chop(mylist):
    del mylist[0]
    last_element = len(mylist) - 1
    del mylist[last_element]
  
def middle(mylist):
    last_element = len(mylist) - 1  
    return mylist[1:last_element]
  
my_list = [1,3,5,7,9,11,13,15]
print my_list
chop(my_list)
print my_list

my_next_list = [0,2,4,6,8,10,12,14]
print my_next_list
mid = middle(my_next_list)
print mid