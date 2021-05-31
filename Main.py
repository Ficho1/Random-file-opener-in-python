import tkinter
import random
import os
from random import choice
import webbrowser

#ENTER YOUR PATH HERE

path="YOUR PATH HERE"



root= tkinter.Tk()


#widget code

#random file picker

def photo():
    file = random.choice([x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))])
    print("Playing file {}...".format(file))
    webbrowser.open(os.path.join(path, file))    
()

#Button

Button = tkinter.Button (root,
                         activebackground="red", 
                         text="Click for random file",
                         padx=50,
                         pady=50,                         
                         command=photo,
                         )
Button.pack()

#window


root.mainloop()
