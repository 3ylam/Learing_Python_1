  # Welcome to Python Course #                                # Date : 01/06/2022
                                                                                                        # Time : 11:40 Am 
                                                    # Secton -2-#
                                                    # Lesson -3-#
                                                    # String Methods part one #


# python provides a tones of built-in methods that can be useful and maniplate with string 
  
  #[1]- len():
      # It's used to return lengh of a string
      # it takes one argument which string would like to know it's len
      # argument can be either leriral or variable
      # syntax:
        # len(string)
     # Example:
print(len("Ibrahim"))  # 7     

#=======================================================================================

    #[2]- strip():
      # It's used to truncate "remove" spaces from string
      # you can pass  an argument or ignore
         # if no argument is passed the default option of this method is removig spaces 
         # if there is an argument it "char for example " it will that char
      # as we mentioned before string in python is an object 
      # string object has attributes called strip and it's own method 
      # can be invoced using dot notation
      # syntax:
        # len()
     # Example:
message = "     today is rainy"
print(message)   # 
print(message.strip())  # it's removes spaces form both sides of a string      
print(message.lstrip()) # it's removes spaces form left hand sides 
print(message.rstrip()) # it's removes spaces form right hand  sides 

# let's pass some args:
# remember if there is no arg passed it will remove spaces only 
message = "##### I like travilling #####"
print(message.strip())  #   ##### I like travilling ##### as it's
# so let's remove the hash sign from the left
print(message.lstrip("#"))
# so let's remove the hash sign from the left
print(message.rstrip("#"))
message = "**** I like travilling ****"
# so let's remove all star signs from the left as well as from the right
print(message.strip("*"))

# does it work with letters??
# yes why not 
message = "12345677789 Hi this is Cs50"
print(message.strip("i"))     # not working

#==================================================================================
  #[3]- title():
      # It's used to capitlize the first letter from each word 
      # no args
      # syntax:
        # string.title()
     # Example:
message = "Python is very easy to learn"
print(message.title())   # ython Is Very Easy To Learn

# =====================================================================================
  #[4]- capitlize():
      # It's used to capitlize the every first letter from each word 
      # if there is any number before it will skip it 
      # no args
      # syntax:
        # string.capitalize()
message = "5g mobile tech is better that 4g"
print(message.title())       #  5G Mobile Tech Is Better That 4G
print(message.capitalize())  # 5g mobile tech is better that 4g

#========================================================================================
  #[5]- zfill():
      #    
      #  
      #  
     


#=========================================================================================
  #[6]- upper():
      # It's used to convert letter from lower case to upper case
      # no args
      # syntax:
name_in_lower_case = "mohammed ibrahim"      
print(name_in_lower_case.upper()) 
name_in_upper_case = "MOHAMMED IBRAHIM"  
print(name_in_upper_case.lower())

#
#
#
#
#







