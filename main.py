#main file
import lib
import tkinter

#create a window
top = tkinter.Tk()
#create a label in the 'top' window
w = tkinter.Label(top, text="Hello, world!")
#?
w.pack()
#run the window. this line will not finish until the window closes
top.mainloop()

lib.hello("A team")