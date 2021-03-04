#Importing the necessary libraries
from tkinter import *

#Defining the functions
def sum_count():
    top = Toplevel()
    top.geometry("250x200")
    SumTitleLabel = Label(top, text="Sum", font="Roboto 14 bold italic underline")
    SumTitleLabel.place(rely=.1, relx=.5, anchor=CENTER)
    Entry1Sum = Entry(top)
    Entry2Sum = Entry(top)
    Entry1Sum.place(rely=.25, relx=.5, anchor=CENTER)
    Entry2Sum.place(rely=.35, relx=.5, anchor=CENTER)
    def calculate():
        num1 = int(Entry1Sum.get())
        num2 = int(Entry2Sum.get())
        suM = num1 + num2 
        suM = str(suM)
        SomaLabel = Label(top, text=suM, fg="red", font="roboto 10 bold")
        SomaLabel.place(rely=.65, relx=.5, anchor=CENTER)
    BttonCalculate = Button(top, text="Calculate", command=calculate)
    BttonCalculate.place(rely=.5, relx=.5, anchor=CENTER)
def subtraction():
    top = Toplevel()
    top.geometry("250x200")
    SubtractionTítuloLabel = Label(top, text="Subtraction", font="Roboto 14 bold italic underline")
    SubtractionTítuloLabel.place(rely=.1, relx=.5, anchor=CENTER)
    Entry1Subtraction = Entry(top)
    Entry2Subtraction = Entry(top)
    Entry1Subtraction.place(rely=.25, relx=.5, anchor=CENTER)
    Entry2Subtraction.place(rely=.35, relx=.5, anchor=CENTER)
    def calculate():
        num1 = int(Entry1Subtraction.get())
        num2 = int(Entry2Subtraction.get())
        subtraction = num1 - num2
        subtraction = str(subtraction)
        SubtractionLabel = Label(top, text=subtraction, fg="red", font="roboto 10 bold")
        SubtractionLabel.place(rely=.65, relx=.5, anchor=CENTER)
    BttonCalculate = Button(top, text="Calculate", command=calculate)
    BttonCalculate.place(rely=.5, relx=.5, anchor=CENTER)
def multiplication():
    top = Toplevel()
    top.geometry("250x200")
    MultiplicationTítuloLabel = Label(top, text="Multiplication", font="Roboto 14 bold italic underline")
    MultiplicationTítuloLabel.place(rely=.1, relx=.5, anchor=CENTER)
    Entry1Multiplication = Entry(top)
    Entry2Multiplication= Entry(top)
    Entry1Multiplication.place(rely=.25, relx=.5, anchor=CENTER)
    Entry2Multiplication.place(rely=.35, relx=.5, anchor=CENTER)
    def calculate():
        num1 = int(Entry1Multiplication.get())
        num2 = int(Entry2Multiplication.get())
        multiplication = num1 * num2
        MultiplicationLabel = Label(top, text=multiplication, fg="red", font="roboto 10 bold")
        MultiplicationLabel.place(rely=.65, relx=.5, anchor=CENTER)
    BttonCalculate = Button(top, text="Calcular", command=calculate)
    BttonCalculate.place(rely=.5, relx=.5, anchor=CENTER)
def division():
    top = Toplevel()
    top.geometry("250x200")
    DivisionTitleLabel = Label(top, text="Division", font="Roboto 14 bold italic underline")
    DivisionTitleLabel.place(rely=.1, relx=.5, anchor=CENTER)
    Entry1Division = Entry(top)
    Entry2Division = Entry(top)
    Entry1Division.place(rely=.25, relx=.5, anchor=CENTER)
    Entry2Division.place(rely=.35, relx=.5, anchor=CENTER)
    def calculate():
        num1 = int(Entry1Division.get())
        num2 = int(Entry2Division.get())
        division = num1 / num2
        DivisionLabel = Label(top, text=division, fg="red", font="roboto 10 bold")
        DivisionLabel.place(rely=.65, relx=.5, anchor=CENTER)
    BttonCalculate = Button(top, text="Calcular", command=calculate)
    BttonCalculate.place(rely=.5, relx=.5, anchor=CENTER)
    
#Configuring the root of the interface
root = Tk()
root.title(" Mini-Calculator")
root.geometry("500x300")

#Title configs
TitleLabel = Label(root, text="Choose one of the options below", font="Roboto 20 bold italic underline")
TitleLabel.place(rely=.1, relx=.5, anchor=CENTER)

#Buttons Config
ButtonSum = Button(root, text="Sum", font="Roboto 11 italic", width=50, command=sum_count)
ButtonSubtraction = Button(root, text="Subtraction", font="Roboto 11 italic", width=50, command=subtraction)
ButtonMultiplication = Button(root, text="Multiplication", font="Roboto 11 italic", width=50, command=multiplication)
ButtonDivision = Button(root, text="Division", font="Roboto 11 italic", width=50, command=division)
ButtonSum.place(rely=.25, relx=.5, anchor=CENTER)
ButtonSubtraction.place(rely=.35, relx=.5, anchor=CENTER)
ButtonMultiplication.place(rely=.45, relx=.5, anchor=CENTER)
ButtonDivision.place(rely=.55, relx=.5, anchor=CENTER)

#Looping it
root.mainloop()
