import Tkinter


class simpleapp_tk(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        listbox = Tkinter.Listbox(self, height=5)
        listbox.grid(column=0, row=1)

        button = Tkinter.Button(self, text=u"Click me !")
        button.grid(column=1, row=0)

        self.grid_columnconfigure(0, weight=1)
        self.update()
        self.geometry(self.geometry())


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('BroadSign Player vpush Assistant.')
    app.minsize(width=500, height=300)
    app.mainloop()
