                                               # Welcome to Python Course #          # Date : 01/06/2022
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
  #[2]- rsplit():
      # It split a string and return it as a list
      # only the different with split .. it's split strig form the right hand side  
     # Example:
my_tip = "you suppose to write your english letter form the left"
# rsplit with no agrument it will split normallu "no side prefered"
print(my_tip.rsplit())  # ['you', 'suppose', 'to', 'write', 'your', 'english', 'letter', 'form', 'the', 'left']
# rsplit with arg will split from the 
print(my_tip.rsplit("u"))  # ['yo', ' s', 'ppose to write yo', 'r english letter form the left']

#=====================================================================================================================
  #[3]- center():
      # centreralize element between a specific char  
      # center method at least it takes to  args 
          # fist one is the returen value "string"
          # seconde one is the char or sub-string to be srruonded among string
          # result = arg - original_string_digits 
          # syntax:
            # string.center(10,"*")
      # 
     # Example:
goolKeeper = "Kasillas"
print(goolKeeper.center(10,"a")) # kasillas has 8 chars so 10-8 = 2 chars .. so the rest of 2 chars will surround orirginal string
# if one arg is passed then it will be spaces between element
print(goolKeeper.center(12,"#")) # ##Kasillas##
# what if I passed more than one char to surround my element
print(goolKeeper.center(20,'#')) # ######Kasillas######

#=====================================================================================================================
  #[4]- count():
        # count for a spesific element within string
        # element may be a single char or sub-stirng
        # use cases :
          #[i] with one arg which is target
          # [ii]- with three agrs [target , start , end]
          # count() method is case sensitive 
text = "My friends and I love to travle by Plane Plane Plane"
print(text.count('o'))  #  1
print(text.count("r"))  # 2
print(text.count("R"))  # 0
print(text.count("Plane"))  # 3
print(text.count("plane"))  # 0 cuz plane agrument starts with small p
# if the target was not found it will retrun zero
print(text.count("z"))  #  0
# with args
# so let's search for o letter but from index 3 to 10
# indecis =  0 1 2 3 4 5 6 7 8 9 0 10 11 12 13
# text    = "M y f r i e n d s   a n  d  I  l o v e t o t r a v l e b y P l a n e P l a n e P l a n e"
# remember our original string consists of ?? Hhahaaha let's see the size
# print(text.len())   #  
truncate_target = text[3:10]  # friends
print(truncate_target)  # friends
#print(text.count("o",3,10)) # means from 

#=========================================================================================================
    #[5]- swapcase():
        # swap and return capital letter to small and small to capital in a string
         # use cases :
          #[i] no agrs
        # Example:
mobile_name = "MotoRolla"
print(mobile_name.swapcase()) # mOTOrOLLA

#================================================================================================================

  #[6]- startswith():
        # retruns true if string starts with a specfic letter otherwise retrun False
        # if target was not found then it'll return 0 only
         # use cases :
           # with 3 args:
              # Target char
              # start from
              # end with
          # this methos is case Sensitve with letters
            # syntax:
                # string.startWith('target',startFrom,endWith)
        # Example:
print(mobile_name.startswith('M')) # True
# startswith() with agrs
mobile_name = "Samsung Galaxy Note 10"
mobile_name = mobile_name[7:19]  # grapping only  "Galaxy Note" from the entire string
print("Line 143 outpute => ",mobile_name) # remember that our rest of string is Galaxy Note
print("Line 144 outpute => ",mobile_name.startswith('g'7,19)) # False
print("Line 145 outpute => ",mobile_name.startswith('G'7,19)) # True

# we've also endswith()




