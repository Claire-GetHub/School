from tkinter import *


class TKBase:
    def __init__(self):
        self.root = Tk()

        self.main()

        self.root.mainloop()

    def main(self) -> None:
        pass

    @staticmethod
    def add(self, wids: list, side = TOP) -> None:
        for wid in wids:
            wid.pack(side= side)


# noinspection PyAttributeOutsideInit
class JoeAutomotive(TKBase):
    def main(self):
        self.top = Frame(self.root)
        self.bottom = Frame(self.root)

        #check vars
        self.Oil = IntVar()
        self.Lube = IntVar()
        self.Rad = IntVar()
        self.Tran = IntVar()
        self.Ins = IntVar()
        self.Muf = IntVar()
        self.Tire = IntVar()
        #top
        self.OilButton = Checkbutton(self.top, text= "Oil change",command= self.calculate, variable= self.Oil)
        self.LubeButton  = Checkbutton(self.top,text= "Lube job", command= self.calculate, variable= self.Lube)
        self.RadButton = Checkbutton(self.top, text= "Radiator flush",command= self.calculate, variable= self.Rad)
        self.TranButton  = Checkbutton(self.top,text= "Transmission flush", command= self.calculate, variable= self.Tran)
        self.InsButton = Checkbutton(self.top, text= "Inspection",command= self.calculate, variable= self.Ins)
        self.MufButton = Checkbutton(self.top, text= "Muffler replacement",command= self.calculate, variable= self.Muf)
        self.TireButton  = Checkbutton(self.top,text= "Tire rotation", command= self.calculate, variable= self.Tire)

        #bottom
        self.value = StringVar()
        self.label = Label(self.bottom, textvariable= self.value)


        self.add(self,[self.top, self.bottom, self.label, self.OilButton, self.LubeButton, self.RadButton, self.TranButton, self.InsButton, self.MufButton, self.TireButton])


    def calculate(self) -> None:
        checks = [[self.Oil, 30],
               [self.Lube, 20],
               [self.Rad, 40],
               [self.Tran, 100],
               [self.Ins, 35],
               [self.Muf, 200],
               [self.Tire, 20]]

        total = 0

        for check in checks:
            if check[0].get() == 1:
                total += check[1]
        self.value.set(total)

# noinspection PyAttributeOutsideInit
class LatinTranslator(TKBase):

    def main(self) -> None:
        self.top = Frame(self.root)
        self.bottom = Frame(self.root)

        self.sinister = Button(self.top, text= "sinister", command= lambda: self.show("left"))
        self.dexter = Button(self.top, text= "dexter", command= lambda: self.show("right"))
        self.medium = Button(self.top, text= "medium", command= lambda: self.show("center"))

        self.text = StringVar()
        self.label = Label(self.bottom, textvariable= self.text)

        self.add(self, [self.top, self.bottom, self.sinister, self.dexter, self.medium, self.label])

    def show(self, message: str):
        self.text.set(message)

# noinspection PyAttributeOutsideInit
class PropertyTax(TKBase):
    def main(self):
        self.top = Frame(self.root)


        self.value = Entry(self.top, width=10)

        self.button = Button(self.top, text= "calculate", command=self.calculate)
        self.text = StringVar()
        self.label = Label(self.top, textvariable= self.text)

        self.add(self, [self.top, self.value, self.button, self.label])

    def calculate(self):
        self.aValue = float(self.value.get()) * .60
        self.text.set((self.aValue /100) * .75)


if __name__ == "__main__":
    tk = PropertyTax()