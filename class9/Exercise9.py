#!/usr/bin/env python

#### import statements
from mytest import *

#### constants
#### functions and classes

# main function (this is the main execution code for your program)
def main():
    my_obj = MyClass('banana', 'red', 'scorpion')
    print my_obj.var1, my_obj.var2, my_obj.var2
    print my_obj.hello()
    print my_obj.not_hello()
    
     # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function
