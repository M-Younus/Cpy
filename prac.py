


#in func def error is I am using DECL CFG for args thats why args must have same syntax as declaraion

from tkinter import *

root = Tk()

def yourFunction(event):
    print('left')

frame = Frame(root, width=100, height=100)

frame.bind("<F5>",yourFunction)   #Binds the "left" key to the frame and exexutes yourFunction if "left" key was pressed
frame.pack()

root.mainloop()