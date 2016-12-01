#!/usr/bin/env python

#### import statements

#### constants

#### functions and classes
def func1():
    print "This is world.py func1"

class MyClass(object):
    '''My first class'''
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def hello(self):
        print "These words rhyme: "+ self.var1 + " " + self.var2 + " " + self.var3

    def not_hello(self):
        print "I wish these words didn't rhyme: "+ self.var1 + " " + self.var2 + " " + self.var3


# main function (this is the main execution code for your program)
def main():
     # I would define any variables that are specific to this script here
    print "\nMain program - world"

# Some test code
    my_obj = MyClass('lunch', 'bunch', 'munch')
    print
    print my_obj.var1, my_obj.var2, my_obj.var3
    my_obj.hello()
    my_obj.not_hello()
    print
     # any variables from main() that need passed into other functions would be passed as arguments


if __name__ == "__main__":                    # program execution starts here
    main()                                                   # first action is to call main function

