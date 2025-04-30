from tkinter import *
from tkinter import messagebox

# class MyGui:
#     def __init__(self):
#         self.mainWindow = Tk()
#         self.mainWindow.title("My not first GUI")

#         self.myButton = Button(self.mainWindow, text= 'click me...', command=self.doSomething)
#         self.quitButton = Button(self.mainWindow, text= 'quit', command=self.mainWindow.destroy)
#         self.myButton.pack()
#         self.quitButton.pack()
#         mainloop()

#     def doSomething(self):
#         messagebox.showinfo('Respoonse', "ewww")



#         # self.topFrame = Frame(self.mainWindow)
#         # self.bottomFrame = Frame(self.mainWindow)


#         # #ipad: internal padding
#         # #pad: external padding
#         # self.label1 = Label(self.topFrame, text= "How are you?", borderwidth=1, relief= "ridge")
#         # self.label1.pack(side="left", ipadx= 10, ipady=10, padx= 10, pady=10)
#         # self.label2 = Label(self.bottomFrame, text= "Doing alright", borderwidth=10, relief= "sunken")
#         # self.label2.pack(side="left", ipadx= 20, ipady=20, pady= (10, 20))

#         # self.topFrame.pack()
#         # self.bottomFrame.pack()



#         mainloop()

class KiloCovertGui:
    def __init__(self):
        self.mainWindow = Tk()

        self.topFrame = Frame(self.mainWindow)
        self.midFrame = Frame(self.mainWindow)
        self.bottomFrame = Frame(self.mainWindow)

        #top frame
        self.promptLabel = Label(self.topFrame, text= "Enter a distance in kilometers:")
        self.kiloEntry = Entry(self.topFrame, width= 10)

        #mid frame
        self.descrLabel = Label(self.midFrame, text= "kilos in miles:")
        self.value = StringVar()
        self.valueLabel = Label(self.midFrame, textvariable= self.value)

        #bottom frame
        self.calcButon = Button(self.bottomFrame, text="Convert", command=self.convert)
        self.quitButton = Button(self.bottomFrame, text= "Quit", command=self.mainWindow.destroy)

        #top frame packing
        self.promptLabel.pack(side="left")
        self.kiloEntry.pack(side="left")
        #mid frame packing
        self.descrLabel.pack(side="left")
        self.valueLabel.pack(side="left")
        #bottom frame packing
        self.calcButon.pack(side="left")
        self.quitButton.pack(side="left")

        #frame packing
        self.topFrame.pack()
        self.midFrame.pack()
        self.bottomFrame.pack()

        mainloop()

    def convert(self):
        kilo = float(self.kiloEntry.get())
        miles = kilo * 0.6214
        
        self.value.set(miles)


class GradeAverage:

    def __init__(self):
        self.main = Tk()

        self.top = Frame(self.main)
        self.bottom = Frame(self.main)

        #top frame
        self.label1 = Label(self.top, text= "Enter score for test 1:")
        self.entry1 = Entry(self.top, width= 10)
        self.label2 = Label(self.top, text= "Enter score for test 2:")
        self.entry2 = Entry(self.top, width= 10)
        self.label3 = Label(self.top, text= "Enter score for test 3:")
        self.entry3 = Entry(self.top, width= 10)

        #bottom frame
        self.desc = Label(self.bottom, text= "Average:")
        self.value = StringVar()
        self.average = Label(self.bottom, textvariable= self.value)
        self.calculate = Button(self.bottom, text= "Average", command= self.calAverage)
        self.quitButton = Button(self.bottom, text= "Quit", command=self.main.destroy)


        #top frame
        self.label1.grid(row=1, column=1)
        self.entry1.grid(row=1, column=2)
        self.label2.grid(row=2, column=1)
        self.entry2.grid(row=2, column=2)
        self.label3.grid(row=3, column=1)
        self.entry3.grid(row=3, column=2)

        #bottom frame
        self.desc.grid(row= 1, column= 1)
        self.average.grid(row= 1, column= 2)
        self.calculate.grid(row= 2, column= 1, padx= 10, pady= 10)
        self.quitButton.grid(row= 2, column= 2, padx= 10, pady= 10)

        self.top.pack()
        self.bottom.pack()

        mainloop()

    def calAverage (self):
        num1, num2, num3 = float(self.entry1.get()), float(self.entry2.get()), float(self.entry3.get())
        self.value.set((num1 + num2 + num3)/3)

#7
class distantCalls:
    def __init__(self):
        self.main = Tk()

        self.left = Frame(self.main)
        self.right = Frame(self.main)

        self.rVar = IntVar()

        #left frame
        self.r1 = Radiobutton(self.left, text= "Daytime (6:00AM - 5:59PM)", variable= self.rVar, value= 1)
        self.r2 = Radiobutton(self.left, text= "Evening (6:00PM - 11:59PM)", variable= self.rVar, value= 2)
        self.r3 = Radiobutton(self.left, text= "Off peak (12:00PM - 5:59AM)", variable= self.rVar, value= 3)
        #right frame
        self.min = Entry(self.right, width= 10)
        self.calculate = Button(self.right, text= "Calculate", command= self.calAmount)
        self.value = StringVar()
        self.amount = Label(self.right, textvariable= self.value)

        #radio buttons
        self.r1.pack()
        self.r2.pack()
        self.r3.pack()
        #right frame
        self.min.pack()
        self.calculate.pack()
        self.amount.pack()

        #frames
        self.left.pack(side= "left")
        self.right.pack(side= "left")

        mainloop()

    def calAmount(self):
        #get radio button
        rate = 0
        match self.rVar.get():
            case 1:
                rate = .07
            case 2:
                rate = .12
            case 3:
                rate = .05

                
        self.value.set(rate * float(self.min.get()))

#4
class CToF:
    def __init__(self):
        self.mainWindow = Tk()

        self.topFrame = Frame(self.mainWindow)
        self.midFrame = Frame(self.mainWindow)
        self.bottomFrame = Frame(self.mainWindow)

        #top frame
        self.promptLabel = Label(self.topFrame, text= "celsius:")
        self.kiloEntry = Entry(self.topFrame, width= 10)

        #mid frame
        self.descrLabel = Label(self.midFrame, text= "fahrenheit: ")
        self.value = StringVar()
        self.valueLabel = Label(self.midFrame, textvariable= self.value)

        #bottom frame
        self.calcButon = Button(self.bottomFrame, text="Convert", command=self.convert)
        self.quitButton = Button(self.bottomFrame, text= "Quit", command=self.mainWindow.destroy)

        #top frame packing
        self.promptLabel.pack(side="left")
        self.kiloEntry.pack(side="left")
        #mid frame packing
        self.descrLabel.pack(side="left")
        self.valueLabel.pack(side="left")
        #bottom frame packing
        self.calcButon.pack(side="left")
        self.quitButton.pack(side="left")

        #frame packing
        self.topFrame.pack()
        self.midFrame.pack()
        self.bottomFrame.pack()

        mainloop()

    def convert(self):
        cel = float(self.kiloEntry.get())
        fahr = (9/5) * cel + 32
        
        self.value.set(fahr)

class MPerG:
    def __init__(self):
        self.mainWindow = Tk()

        self.topFrame = Frame(self.mainWindow)
        self.midFrame = Frame(self.mainWindow)
        self.bottomFrame = Frame(self.mainWindow)

        #top frame
        self.promptLabel = Label(self.topFrame, text= "miles:")
        self.mile = Entry(self.topFrame, width= 10)
        self.promptLabel2 = Label(self.topFrame, text= "gallon:")
        self.gallon = Entry(self.topFrame, width= 10)

        #mid frame
        self.descrLabel = Label(self.midFrame, text= "miles per gallon: ")
        self.value = StringVar()
        self.valueLabel = Label(self.midFrame, textvariable= self.value)

        #bottom frame
        self.calcButon = Button(self.bottomFrame, text="Convert", command=self.convert)
        self.quitButton = Button(self.bottomFrame, text= "Quit", command=self.mainWindow.destroy)

        #top frame packing
        self.promptLabel.pack(side="left")
        self.mile.pack(side="left")
        self.promptLabel2.pack(side="left")
        self.gallon.pack(side="left")
        #mid frame packing
        self.descrLabel.pack(side="left")
        self.valueLabel.pack(side="left")
        #bottom frame packing
        self.calcButon.pack(side="left")
        self.quitButton.pack(side="left")

        #frame packing
        self.topFrame.pack()
        self.midFrame.pack()
        self.bottomFrame.pack()

        mainloop()

    def convert(self):
        cel = float(self.mile.get())
        gal = float(self.gallon.get())
        fahr = cel / gal
        
        self.value.set(fahr)

if __name__ == '__main__':
    myGui = MPerG()