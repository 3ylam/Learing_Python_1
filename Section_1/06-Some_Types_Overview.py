  # Welcome to Python Course #                                # Date : 01/06/2022
                                                                                                        # Time : 11:40 Am 
                                                    # Secton -1-#
                                                    # Lesson -6-#
                                                    # Data type in python #


# Everything in python is Object 
  # each object has it't own attributes and Operations  
# python is intellijence enough to detetct the type of var from content
# Numrical type we've:
    #[1]- integer
num1 = 40
print(num1)  #
print(type(num1)) # <class 'int'>
    #[2]- flaot:
        # number with decimal point
flaot_num = 5.5
print(flaot_num)
print(type(flaot_num))  # <class 'float'>
    # String:
        # sequence of chars
name = "Omer"
print(name) #  Omer
print(type(name))  # <class 'String'>

print("-------------------------------------------------------------------------------")

# python has it's own data structure which make it unique:
  # List:
     # is a collection of hetregenous data item
     # these data items are contigueos in memory
     # each item can be accessed by it's index
     # list elements surrounded within squar brackers []
     # list is zero index
     # last item = index - 1
     # list is mutable
my_list = [1,"Omer" ,2,'#',"three",False,34.4]
print(my_list)
print(type(my_list))  # 
print(my_list[0]) # 1
print(my_list[1]) # Omer
print(my_list[4]) # three

print("-------------------------------------------------------------------------------")
# we can perfrom some operations on list ..Like:
  # index:
print(my_list[-1]) # last item   34.4
  # slicing:
print(my_list[0:3]) # [1, 'Omer', 2]
print(my_list[1:])  # ['Omer', 2, '#', 'three', False, 34.4]
print(my_list[:-1]) # [1, 'Omer', 2, '#', 'three', False]
print(my_list[1:2:])# 'Omer']
# we can multiply list :
print("Line 54 output => ",my_list*2) # will repeat list element 2 times
nested_list = [1,2,3,["One","two","three"],"good bye"]
print(nested_list) 
print(nested_list[2:4]) # 4 not included [3, ['One', 'two', 'three']]
# also compairing :
list_one = [1,2,3,4]
list_Two = [1,2,3,4]
print("Line 62 output => ",list_Two == list_one)  # True 
list_one = [ 1,2,"Omer",4,5]
list_Two = [1,2,"Ahemd",4,5]
if list_one[2] == list_Two[2]:
  print("Yes the middle elelemts are the same ")
else:
  print("No the middle elements are not same")
  print(f"because The middle elelemt of list one is {list_one[2]} and the middle elemet of list tow is {list_Two[2]}")
# here is little ticky
# what if I want to print only the second element of outer list and the fist two elements of sub-list
# How to dealing with nested list
#print("Line 61 output => ",nested_list[3:[:2]])  # [1,2,["One","two"]] 

# loop with list:

print("-------------------------------------------------------------------------------")

# we've also Tuple:
    # is a collection of data item which is hemogenous type
    # tupe surrounded within parenthesis ()
    # these data items are contigueos in memory
    # each item can be accessed by it's index
    # tuple is mutable 

my_tuple =(1,"Ali",2,"Omer",False,"the weather is cool ",'%')
print(my_tuple)  #  (1, 'Ali', 2, 'Omer', False, 'the weather is cool ', '%')
print(type(my_tuple))


# Loop with Tuple:



# also we can convert list to tuple 
names = ["Omer","Ahemd","Ali"]
print("Line 97 output => ",names)
print("Line 98 output => ",type(names))
List_to_tuble  = tuple(names)
print("Line 100 output => ",List_to_tuble)
print("Line 101 output => ",type(List_to_tuble))
print("-------------------------------------------------------------------------------")
# Dictionary:
my_dic = {1:"Ali",2:"Ahemd",3:"Ibrahim"}
print(my_dic)
print(type(my_dic))    
print("Line 90 output => ",my_dic,)
print("#########################################-#########################################") # 

