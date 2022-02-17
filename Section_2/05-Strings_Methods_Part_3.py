  # Welcome to Python Course #          # Date : 01/06/2022
                                                                                                        # Time : 11:40 Am 
                                                    # Secton -2-#
                                                    # Lesson -3-#
                                                    # String methods part3 #



#[12]- index():
        # retruns the index of sub-string "the index of first letter"
        # if target was not found then it'll return 0 only
         # use cases :
           # with 3 args:
              # Target "sub-string"
              # start 
              # end 
             # syntax:
                # string.startWith('target',startFrom,endWith)
        # Example:
name = "Mohammed Ali Basha"
print(name.index('M')) # 0
print(name.index('o')) # 1
print(name.index('a')) # 3
# let's search within s certian scale
print("Line 25 output => ",name.index('m',3,8))   # search for m within 4->8 wich is ammed  m exist at the index 4 
# we can do a little bit tricky
name = name[9:12] # wich is Ali
print(name.index('l'))  # 1
print(name.index('z',0,)) # 3




# 
#
#
#
#
#