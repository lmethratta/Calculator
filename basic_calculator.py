# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#
# Author: Leah Methratta
# Date Created: 2022 02 21
# Date Revised: 2022 02 21
# Purpose: Basic Calculator

from tkinter import *

root = Tk()
# How to change the title of the tab?
    # Use root.title!
root.title("Simple Calculator")

e = Entry(root, width = 35, borderwidth = 5)
# We want a column span of 5 because below this input, we have 4 buttons
e.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 10)


# This function allows for a button to be clicked and have its value
# appear in the empty box
def button_click(value):
     # Gets the current value
     current = e.get()
     # Delete whatever is in the box
     e.delete(0, END)
     # Insert whatever value was clicked
     e.insert(0, str(current) + str(value))

# This function allows for the clear button to clear the empty box
def button_clear():
    e.delete(0, END)
    
# This function allows for arithmetic operations
def button_arith(arith_in):
    first_value = e.get()
    # Want to create a global variable
    # Such that it can be accessed anywhere in this program
    global first_num
    first_num = float(first_value)
    # Want to store arithmetic as global
    global arith 
    arith = str(arith_in)
    # Want to empty the text box
    e.delete(0, END)
   
    

# This function allows for an equal operation
def button_equal():
    # Want to grab a second variable 
    second_value = e.get()
    # Want to delete in case anythig is in the box 
    e.delete(0, END)
    #Cases for different arithmetic cases
    if arith == "+":
        e.insert(0, first_num + float(second_value))
    elif arith == "-":
            e.insert(0, first_num - float(second_value))
    elif arith == "*":
            e.insert(0, first_num * float(second_value))
    elif arith == "/":
            e.insert(0, first_num / float(second_value))
    else:
        e.insert(0, "ERROR")

#This is a function for decimal point
def button_decimal():
    # Gets the current value
    current = e.get()
     # Delete whatever is in the box
    e.delete(0, END)
    #Insert number with decimal
    e.insert(0, str(current) + ".")
    
    
    
  
# Define buttons  
# Since the function button_click takes in a parameter, we have to use 
# lambda 
button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))

button_add = Button(root, text = "+", padx = 40, pady = 20, command = lambda: button_arith('+'))
button_sub = Button(root, text = "-", padx = 40, pady = 20, command = lambda: button_arith('-'))
button_mul = Button(root, text = "*", padx = 40, pady = 20, command = lambda: button_arith('*'))
button_div = Button(root, text = "/", padx = 40, pady = 20, command = lambda: button_arith('/'))
button_dot = Button(root, text = ".", padx = 40, pady = 20, command = button_decimal)
button_equal = Button(root, text = "=", padx = 40, pady = 20, command = button_equal)
button_clear = Button(root, text = "CE", padx = 180, pady = 20, command = button_clear)

# Putting buttons on the screen
button_1.grid(row = 3 , column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_0.grid(row = 4, column = 1)

button_dot.grid(row = 4, column = 0)

button_add.grid(row = 1, column = 4)
button_sub.grid(row = 2, column = 4)
button_mul.grid(row = 3, column = 4)
button_div.grid(row = 4, column = 4)
button_equal.grid(row = 4, column = 2)
button_clear.grid(row = 5, column = 0, columnspan  = 5)


root.mainloop();