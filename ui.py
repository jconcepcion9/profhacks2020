import tkinter

#cell class. required because each cell needs a copy of its coordinates
class Cell:
    #on click takes two ints as arguments
    def __init__(self, x:int, y:int, grid, onclick, i):
        self.x = x
        self.y = y
        cell = tkinter.Button(grid, text=str(i+1), bg="#DDDDDD", command=lambda:onclick(x, y))
        cell.grid(row=y, column=x, sticky="nesw", padx=50, pady=50)


#the main game window. a grid of cells with clickable buttons
class GameWindow:
    def __init__(self, onclick):
        #create a window
        self.root = tkinter.Tk()
        self.root.geometry("900x900")
        self.grid = tkinter.Frame(self.root)

        #configure column and row widths
        self.grid.grid_columnconfigure(0, weight=1)
        self.grid.grid_columnconfigure(1, weight=1)
        self.grid.grid_columnconfigure(2, weight=1)
        self.grid.grid_rowconfigure(0, weight=1)
        self.grid.grid_rowconfigure(1, weight=1)
        self.grid.grid_rowconfigure(2, weight=1)

        #configure cells
        width  = 3
        height = 3
        for i in range(0, (width*height)):
            x = i%3
            y = i//3
            cell = Cell(x, y, self.grid, onclick, i)

        self.grid.pack(expand=True, fill=tkinter.BOTH)

    def run(self):
        self.root.mainloop()
