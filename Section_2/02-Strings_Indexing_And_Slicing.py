  # Welcome to Python Course #                                # Date : 01/06/2022
                                                                                                        # Time : 11:40 Am 
                                                    # Secton -2-#
                                                    # Lesson -2-#
                                                    # Indexing and Slicing in String #

# What is indexing:
   # is a process of accessing a specific char of a string
   # we can use squar brackets to perform indecing
message = "Today is rainy"
print(message[0]) # first char  T
print(message[4]) # y
print(message[6]) # i
print(message[-1]) # last char y

# What Sliciing:
    # a process of accessing multiple chars "sub-string" of a original string
    # also we use square brackets to access
print("============================================================================")
print(message[:4])  #Toda
print(message[1:7]) # oday i
print(message[3:])  # ay is rainy
print(message[:-1]) # Today is rain
print(message[:2:]) # entir string but skip letter and print other  in each letter To
print(message[:])

# Notice:
    # In indecing when we said element[-1] this will grap last element
    # but in Slicing will grab last_element -1
    # let's see that in action
    # suppose we've:
message = "12345"
# let's print "index" of last element
print(message[-1])
# let's slic and and print sub-string form some where to the end:
# first of all let's see the indexes of our string message
# indecing =  0 1 2 3 4
# message  = "1 2 3 4 5"
# message[2:-1] means form 2-3  [3 4] cuz last element not included
# let's see
print(message[2:-1]) # 3 4

# so be care in slicing 


#
#