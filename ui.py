import tkinter
import threading
import debugwindow as debug

#start the debug window in a new thread
db = debug.DebugWindow()
threading.Thread(target=db.run, args=(1,))

#create a window
root = tkinter.Tk()
root.geometry("900x900")
db.set_width("900")
db.set_height("900")
grid = tkinter.Frame(root)
grid.config(padx=0)

#configure column and row widths
grid.grid_columnconfigure(0, weight=1)
grid.grid_columnconfigure(1, weight=1)
grid.grid_columnconfigure(2, weight=1)
grid.grid_rowconfigure(0, weight=1)
grid.grid_rowconfigure(1, weight=1)
grid.grid_rowconfigure(2, weight=1)


#cell class. required because each cell needs a copy of its coordinates
class Cell:
    def __init__(self, x, y, grid):
        self.x = x
        self.y = y
        cell = tkinter.Button(grid, text=str(i+1), bg="#DDDDDD", command=lambda:db.set_other("clicked "+str(self.x+1)+" "+str(self.y+1)))
        cell.grid(row=y, column=x, sticky="nesw", padx=50, pady=50)


#configure cells
width  = 3
height = 3
for i in range(0, (width*height)):
    x = i%3
    y = i//3
    cell = Cell(x, y, grid)

grid.pack(expand=True, fill=tkinter.BOTH)


#called when the window resizes
#updates the debug window
def update_column_size(window):
    db.set_width(str(root.winfo_width()))
    db.set_height(str(root.winfo_height()))

root.bind("<Configure>", update_column_size)

#run main window
root.mainloop()