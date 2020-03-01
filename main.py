#main file
import tkinter
import ui
import debugwindow
import threading

#start the debug window in a new thread
db = debugwindow.DebugWindow()
threading.Thread(target=db.run, args=(1,))


# set up window
root = tkinter.Tk()
root.geometry("900x900")
top_label = tkinter.Label(root, text="your turn", foreground="blue") # the label for the current player
top_label.pack()
game_window = ui.GameWindow(root)

# set the top label to change then the turn changes
def turn_change(is_player_turn:bool):
    if is_player_turn:
        top_label.config(text="your turn", foreground="blue")
    else:
        top_label.config(text="opponent turn", foreground="red")

game_window.set_switch_turn(turn_change)

#function run when a cell is clicked
def onclick(x:int, y:int, game_window:debugwindow.DebugWindow):
    db.set_other("you clicked cell "+str(x)+" "+str(y))
    game_window.disable_buttons()
    game_window.opponent_turn()
    turn_change(game_window.is_player_turn)

game_window.set_on_click(onclick)

#start the main game window
root.mainloop()