#main file
import tkinter
import ui
import debugwindow
import threading

#start the debug window in a new thread
db = debugwindow.DebugWindow()
threading.Thread(target=db.run, args=(1,))

#function run when a cell is clicked
def onclick(a, b):
    db.set_other("you clicked cell "+str(a)+" "+str(b))

#start the main game window
game_window = ui.GameWindow(onclick)
game_window.run()