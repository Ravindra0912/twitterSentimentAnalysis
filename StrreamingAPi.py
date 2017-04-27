import projectWgui
from tkinter import *

p = projectWgui


class GUI(p.Listener, p.Search):
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.searchButton = Button(frame, text="Search",command=p.l1.on_data)
        self.searchButton.pack(side=LEFT)

root = Tk()
g = GUI(root)
root.mainloop()