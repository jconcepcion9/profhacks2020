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
turn_label = tkinter.Label(root, text="your turn", foreground="blue") # the label for the current player
turn_label.pack()
game_window = ui.GameWindow(root)


# set the turn label to change then the turn changes
def turn_change(is_player_turn:bool):
    if is_player_turn:
        turn_label.config(text="your turn", foreground="blue")
    else:
        turn_label.config(text="opponent turn", foreground="red")

game_window.set_on_switch_turn(turn_change)

#function run when a cell is clicked
def onclick(clicked_cell:ui.Cell, game_window:debugwindow.DebugWindow):
    db.set_other("you clicked cell "+str(clicked_cell.x)+" "+str(clicked_cell.y))
    game_window.opponent_turn()
    turn_change(game_window.is_player_turn)
    clicked_cell.set_o()

game_window.set_on_click(onclick)

# click a cell for the opponent. this is a test
game_window.click_cell(0, 0, False)

# close app when escape is pressed
root.bind("<Escape>", exit)
#start the main game window
root.mainloop()

