import Tkinter


class simpleapp_tk(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        button = Tkinter.Button(self, text=u"Click me !")
        button.grid(column=1, row=0)


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.minsize(width=700, height=300)
    app.mainloop()
