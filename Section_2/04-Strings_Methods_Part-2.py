  # Welcome to Python Course #                                # Date : 01/06/2022
                                                                                                        # Time : 11:40 Am 
                                                    # Secton -2-#
                                                    # Lesson -4-#
                                                    # String methods part2 #



  #[1]- split():
      # It split a string and return it as a list
      # it works based on white spaces and considered it as end of string
      # it takes two args first separator "knife" the second maxsplit "how may to split"
      # syntax:
        # split(string)
     # Example:
menu = "salad chicken fool a fish"
list_menu = menu.split()
print(list_menu) # ['salad', 'chicken', 'fool', 'a', 'fish']
print(type(list_menu))  # calss list
#what if i don't want spliting be based on white spaces
# then you can make string as one block by using either under score or dash
menu = "salad-chicken-fool-a-fish"
print(menu.split())   # ['salad-chicken-fool-a-fish']
# let's try with separator
message = "I love to teach people programming"
# split based on p
print("line 27 outpute => ",message.split("p"))    # ['I love to teach ', 'eo', 'le ', 'rogramming']
# split based on o
print("line 29 outpute => ",message.split("o"))    # ['I l', 've t', ' teach pe', 'ple pr', 'gramming']
# split based on e
print("line 31 outpute => ",message.split("e"))    # ['I lov', ' to t', 'ach p', 'opl', ' programming']

# Notece:
  # put that on your mind when you deal with split with separator the char "separator" is not included "will disappear"
  # if separator was not found it will return the original string in list but "as it's "  
  # split method os case sensitive
fullName = "Baha aldin mohammed"
print(fullName.split("z"))  # there is no separator found like z to perform task ['Baha aldin mohammed']

# let's try split with to args:
print("line 40 outpute => ",fullName.split("a",3))  #  ['B', 'h', ' ', 'ldin mohammed']  what's going on here?!
# the split method in code above it's seem when you pass both separator and maxsplit it working only with the two default options which is separator 
# and spaces .. so it ignorring maxsplit arg
# so we can say that about split method
# the priority of split method is :
  # [1]- no args => will based on spaces 

my_tip = "First Learn How to Learn"
print("Line 49 outpute => ",my_tip.split()) # ['First', 'Learn', 'How', 'to', 'Learn']

  # [2]- if there is :
      #[i]    - separator only => then it will split base on it
print("Line 53 outpute => ",my_tip.split("L")) #  ['First ', 'earn How to ', 'earn']
      #[ii]   - separator + maxsplit + spaces founded => then it will work only on separator and spaces 
print("Line 55 outpute => ",my_tip.split("L",4))  # ['First ', 'earn How to ', 'earn'] # 3 lists only    
      # [iii] - separtor + maxsplit  + nos spaces founded => then it will work on separator and maxsplit
my_tip = "First_Learn_How_to_Learn"
print("Line 58 outpute => ",my_tip.split("L",4)) # ['First_', 'earn_How_to_', 'earn']

# I need more info about split(separator,maxSplit) .. who does it work!
#=========================================================================================================
  #[1]- rsplit():
      # It split a string and return it as a list
      # it works based on white spaces and considered it as end of string
      # it takes arg which separator "knife"
      # syntax:
        # split(string)
     # Example:
#
#
#
#
