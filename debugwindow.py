import tkinter

###         Debug window. used to keep track of changing variables in the system for debugging
class DebugWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("debug")
        self.window.geometry("200x100")

        self.width  = tkinter.Label(self.window)
        self.height = tkinter.Label(self.window)
        self.other  = tkinter.Label(self.window)
        self.width.pack(expand=True)
        self.height.pack(expand=True)
        self.other.pack(expand=True)

    def run(self):
        self.window.mainloop()

    def set_width(self, width:str):
        self.width.configure(text="width: "+width)

    def set_height(self, height:str):
        self.height.configure(text="height: "+height)

    def set_other(self, text:str):
        self.other.configure(text=text)