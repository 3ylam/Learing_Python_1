  # Welcome to Python Course #                                # Date : 01/06/2022
                                                                                                        # Time : 11:40 Am 
                                                    # Secton --#
                                                    # Lesson -1-#
                                                    # Intro #


# When you dealing with string ..  "Escape Sequence" escape char w'll come accross to you  
# Special chars are a unique samples specified by python and most programming languages
# Escape chars tells the compiler that "please do not take care about this sample .. just skip it and print it as it's"
# Escape sequence are useful to formating output
# Here is some of python's Escape Sequences:
  
    #[1]- Back-slash:
        # it comes with:
           #[i] \b :
              # Ommites "remove" the previous char
              # Example:
print("Today\bis\bgood\bday")   # Todayisgoodday      
            #[ii] \n:
                # down to new line
                # Example:
print("Today\nis\ngood\nday")  # 
# or we can skipp to printing at the same line :
print("Today \
           is \
        good \
          day") # Once you put \ python will terminate the line and will not allow to write any thing after \

    #[2]- Back slash with single quaote \' :
           # used to skipp the single quoate
           # Example:
print(" \'Python\' is a aweasome programming langaug") # 'Python' is a aweasome programming langaug
    
    #[3]- Back slash with double quaote  \" :
          # used to skipp the single quoat
          # Example:
print(" \"Python\" is a aweasome programming langaug") # 'Python' is a aweasome programming langaug

    #[4]- Back slash r  \r :

        # Replace n char from the right hand side with n from left hand side 
        # Example: 
print("ABCDEfG\rabcdefg")        
    #[5]- Back slash with t "Horizontal tab" :
        # Provides horizontal space "tab" 
        # Example:
print("I love to travel by \t bus ") # I love to travel by   bus     

    #[6]- \xhh :
        # print hexadecimal value of achar
        # syntax:
            # \xChar_hexadecimal_value
        # Example:
print("Line 55 output => ","\x76")  # V
print("Line 56 output => ","\x73")  # V
# let's print by name  :
print("Line 55 output => ","\x42 \x41 \x48 \x41 ")  # BAHA       













                                                    