#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    print ("Even or Odd")
    try:
        user_num = int(input("Please enter an Integer: "))
    except: 
        print("Number entered is not an Integer")
        return "NA"
    if (user_num % 2 == 0):
        return "Entered Number is Even"
    else: 
        return "Entered Number is Odd"



    


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for count_x in range (100):
        if (count_x + 1) % 10 == 0 :
            print (repr(count_x + 1).rjust(4))
        else:
            print (repr(count_x + 1).rjust(4), end = "")




def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    sum = 0
    count = 0
    while True:
        
        user_imp = input("Please enter a number or 'done': ")
        if user_imp == "done":
            if count == 0:
                return 0
            else: 
                return sum/count
        else: 
            try: 
                user_num = float(user_imp)
            except: 
                print("Invalid input. Please try again")
                continue
        sum += user_num
        count += 1







##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    print(even_odd())
    ten_by_ten()
    print(find_average())
    

if __name__ == '__main__':
    main()