import tkinter

#cell class. required because each cell needs a copy of its coordinates
class Cell:
    #on click takes two ints as arguments
    def __init__(self, x:int, y:int, grid, onclick, i):
        self.x = x
        self.y = y
        self.cell = tkinter.Button(grid, text=str(i+1), bg="#DDDDDD", command=lambda:onclick(x, y))
        self.cell.grid(row=y, column=x, sticky="nesw", padx=30, pady=30)

    '''f arguments:
        x: int
        y: int
    '''
    def set_click_handler(self, f):
        def handler():
            #call the callback with x and y so the callback can use that information
            f(self.x, self.y)

        self.cell.config(command=handler)

    def get_cell(self) -> tkinter.Button:
        return self.cell


#the main game window. a grid of cells with clickable buttons
class GameWindow:
    def __init__(self, root, onclick = lambda a:a):
        #create a window
        
        self.grid = tkinter.Frame(root)

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
        self.cells = []
        for i in range(0, (width*height)):
            x = i%3
            y = i//3
            cell = Cell(x, y, self.grid, onclick, i)
            self.cells.append(cell)

        self.grid.pack(expand=True, fill=tkinter.BOTH)

        #true if player's turn. false if opponent's turn
        self.is_player_turn = True

    # enable and disable buttons
    def disable_buttons(self):
        for cell in self.cells:
            cell.cell.config(state=tkinter.DISABLED)

    def enable_buttons(self):
        for cell in self.cells:
            cell.cell.config(state=tkinter.ACTIVE)
    
    # set handlers
    def set_switch_turn(self, f):
        self.switch_turn = f

    '''f arguments:
        x: int  x position of clicked cell
        y: int  y position of clicked cell
        self    reference to this GameWindow object
    '''
    def set_on_click(self, f):
        for cell in self.cells:
            def handle(x, y):
                f(x, y, self)

            cell.set_click_handler(handle)

    # set turn

    def player_turn(self):
        self.is_player_turn = True
        self.switch_turn(self.is_player_turn)
        self.enable_buttons()

    def opponent_turn(self):
        self.is_player_turn = False
        self.switch_turn(self.is_player_turn)
        self.disable_buttons()

    