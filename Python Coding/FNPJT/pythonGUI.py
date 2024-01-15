#Name : ERIC AMOH ADJEI
#Date : 11/03/2023
#Assignment : Create a GUI in Python



from tkinter import messagebox
from tkinter import ttk
from turtle import color
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style

# Description: We will be Creating a GUI in Python 

#we will need to import the cgitb module to handle errors and text to display the error
from cgitb import text
#first we will need to import the tkinter module as tk
import tkinter as tk

#next we will need to create a variable that will hold the calculation
calculation = ""

# this is the function that will be called when the button is pressed
def add_to_calculation(symbol):
    #we will need to use the global keyword to access the global variable
    global calculation
    #we will need to add the symbol to the calculation variable
    calculation += str(symbol)
    #we will need to update the label with the calculation
    text_result.delete("1.0", tk.END)
    #text_result.config(text=calculation)
    text_result.insert("1.0", calculation)
    

#this is the function that will be called when the equal button is pressed
def evalute_calculation() :
    #we will need to use the global keyword to access the global variable
    global calculation
    
#we will need to use the try and except block to handle errors
    try:
        #we will need to use the eval function to evaluate the calculation
        calculation = str(eval(calculation))
        #we will need to update the label with the result
        text_result.delete("1.0", tk.END)
        text_result.insert("1.0", calculation)
    
        #we will need to use the except block to handle errors
    except:
        clear_field()
        text_result.insert("1.0", "Error")


#this is the function that will be called when the clear button is pressed
def clear_field():
    #we will need to use the global keyword to access the global variable
    global calculation
    #we will need to clear the calculation variable
    calculation = ""
    #we will need to update the label with the result
    text_result.delete("1.0", tk.END)
    

#next we will need to create a root window
root = tk.Tk()
style = ttk.Style("darkly")

#we will need to give it a title
root.title("Calculator")
#next we will need to set the minimum size of the window
root.minsize(width=290, height=360)
#next we will need to set the maximum size of the window
root.geometry("302x360")
#next we will need to create a text label,hieght,width,font.
text_result = tk.Text(root, height=2, width=16, font=("Open sans", 24))
#next we will need to create a grid frame
text_result.grid(row=0, column=0, columnspan=5)

#writing the code for the buttons
#we will need to create a button for each number
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), height=2, width=5, font=("Open sans", 14))
btn_1.grid(row=2, column=1, padx=3, pady=5 )

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), height=2, width=5, font=("Open sans", 14))
btn_2.grid(row=2, column=2, padx=3, pady=5)
                  
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), height=2, width=5, font=("Open sans", 14))
btn_3.grid(row=2, column=3, padx=3, pady=5)
                  
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), height=2, width=5, font=("Open sans", 14))
btn_4.grid(row=3, column=1, padx=3, pady=5)
                  
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), height=2, width=5, font=("Open sans", 14))
btn_5.grid(row=3, column=2, padx=3, pady=5)
                  
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), height=2, width=5, font=("Open sans", 14))
btn_6.grid(row=3, column=3, padx=3, pady=5)
                  
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), height=2, width=5, font=("Open sans", 14))
btn_7.grid(row=4, column=1, padx=3, pady=5)
                  
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), height=2, width=5, font=("Open sans", 14))
btn_8.grid(row=4, column=2, padx=3, pady=5)
                  
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), height=2, width=5, font=("Open sans", 14))
btn_9.grid(row=4, column=3, padx=3, pady=5)
                  
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), height=2, width=5, font=("Open sans", 14))
btn_0.grid(row=5, column=2, padx=3, pady=5)
                  
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), height=2, width=5, font=("Open sans", 14))
btn_plus.grid(row=2, column=4, padx=3, pady=5)
                     
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), height=2, width=5, font=("Open sans", 14))
btn_minus.grid(row=3, column=4, padx=3, pady=5)
                      
btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), height=2, width=5, font=("Open sans", 14))
btn_multiply.grid(row=4, column=4, padx=3, pady=5)
                      
btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), height=2, width=5, font=("Open sans", 14))
btn_divide.grid(row=5, column=4, padx=3, pady=5)
                  
btn_equal = tk.Button(root, text="=", command=lambda: evalute_calculation(), height=2, width=5, font=("Open sans", 14))
btn_equal.grid(row=5, column=3, padx=3, pady=5)
 
#we will need to create a button for the clear button
btn_clear = tk.Button(root, text="C", command=lambda: clear_field(), height=2, width=5, font=("Open sans", 14))
btn_clear.grid(row=5, column=1, padx=3, pady=5)                  

#rott.mainloop() will keep the window open
root.mainloop()