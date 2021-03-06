#Importando as bibliotecas necessárias
from tkinter import *

#Definindo as funções para atribui-las aos botões
def adição():
    top = Toplevel()
    top.geometry("250x200")
    AdiçãoTítuloLabel = Label(top, text="Adição", font="Roboto 14 bold italic underline")
    AdiçãoTítuloLabel.place(rely=.1, relx=.5, anchor=CENTER)
    Entry1Adição = Entry(top)
    Entry2Adição = Entry(top)
    Entry1Adição.place(rely=.25, relx=.5, anchor=CENTER)
    Entry2Adição.place(rely=.35, relx=.5, anchor=CENTER)
    def calcular():
        num1 = int(Entry1Adição.get())
        num2 = int(Entry2Adição.get())
        soma = num1 + num2 
        soma = str(soma)
        SomaLabel = Label(top, text=soma, fg="red", font="roboto 10 bold")
        SomaLabel.place(rely=.65, relx=.5, anchor=CENTER)
    BotãoCalcular = Button(top, text="Calcular", command=calcular)
    BotãoCalcular.place(rely=.5, relx=.5, anchor=CENTER)
def subtração():
    top = Toplevel()
    top.geometry("250x200")
    SubtraçãoTítuloLabel = Label(top, text="Subtração", font="Roboto 14 bold italic underline")
    SubtraçãoTítuloLabel.place(rely=.1, relx=.5, anchor=CENTER)
    Entry1Subtração = Entry(top)
    Entry2Subtração = Entry(top)
    Entry1Subtração.place(rely=.25, relx=.5, anchor=CENTER)
    Entry2Subtração.place(rely=.35, relx=.5, anchor=CENTER)
    def calcular():
        num1 = int(Entry1Subtração.get())
        num2 = int(Entry2Subtração.get())
        subtração = num1 - num2
        subtração = str(subtração)
        SubtraçãoLabel = Label(top, text=subtração, fg="red", font="roboto 10 bold")
        SubtraçãoLabel.place(rely=.65, relx=.5, anchor=CENTER)
    BotãoCalcular = Button(top, text="Calcular", command=calcular)
    BotãoCalcular.place(rely=.5, relx=.5, anchor=CENTER)
def multiplicação():
    top = Toplevel()
    top.geometry("250x200")
    MultiplicaçãoTítuloLabel = Label(top, text="Multiplicação", font="Roboto 14 bold italic underline")
    MultiplicaçãoTítuloLabel.place(rely=.1, relx=.5, anchor=CENTER)
    Entry1Multiplicação = Entry(top)
    Entry2Multiplicação = Entry(top)
    Entry1Multiplicação.place(rely=.25, relx=.5, anchor=CENTER)
    Entry2Multiplicação.place(rely=.35, relx=.5, anchor=CENTER)
    def calcular():
        num1 = int(Entry1Multiplicação.get())
        num2 = int(Entry2Multiplicação.get())
        multiplicação = num1 * num2
        MultiplicaçãoLabel = Label(top, text=multiplicação, fg="red", font="roboto 10 bold")
        MultiplicaçãoLabel.place(rely=.65, relx=.5, anchor=CENTER)
    BotãoCalcular = Button(top, text="Calcular", command=calcular)
    BotãoCalcular.place(rely=.5, relx=.5, anchor=CENTER)
def divisão():
    top = Toplevel()
    top.geometry("250x200")
    DivisãoTítuloLabel = Label(top, text="Divisão", font="Roboto 14 bold italic underline")
    DivisãoTítuloLabel.place(rely=.1, relx=.5, anchor=CENTER)
    Entry1Divisão = Entry(top)
    Entry2Divisão = Entry(top)
    Entry1Divisão.place(rely=.25, relx=.5, anchor=CENTER)
    Entry2Divisão.place(rely=.35, relx=.5, anchor=CENTER)
    def calcular():
        num1 = int(Entry1Divisão.get())
        num2 = int(Entry2Divisão.get())
        divisão = num1 / num2
        DivisãoLabel = Label(top, text=divisão, fg="red", font="roboto 10 bold")
        DivisãoLabel.place(rely=.65, relx=.5, anchor=CENTER)
    BotãoCalcular = Button(top, text="Calcular", command=calcular)
    BotãoCalcular.place(rely=.5, relx=.5, anchor=CENTER)
    
def menu():
    pass
#Configurando a raiz da interface
root = Tk()
root.title(" Mini-calculadora")
root.geometry("500x300")

#Configurações do título
TítuloLabel = Label(root, text="Escolha uma das opções abaixo", font="Roboto 20 bold italic underline")
TítuloLabel.place(rely=.1, relx=.5, anchor=CENTER)

#Configuração dos botões
BotãoAdição = Button(root, text="Adição", font="Roboto 11 italic", width=50, command=adição)
BotãoSubtração = Button(root, text="Subtração", font="Roboto 11 italic", width=50, command=subtração)
BotãoMultiplicação = Button(root, text="Multiplicação", font="Roboto 11 italic", width=50, command=multiplicação)
BotãoDivisão = Button(root, text="Divisão", font="Roboto 11 italic", width=50, command=divisão)
BotãoMenu = Button(root, text="Retornar ao menu", font="Roboto 11 italic", width=50, command=menu)
BotãoAdição.place(rely=.25, relx=.5, anchor=CENTER)
BotãoSubtração.place(rely=.35, relx=.5, anchor=CENTER)
BotãoMultiplicação.place(rely=.45, relx=.5, anchor=CENTER)
BotãoDivisão.place(rely=.55, relx=.5, anchor=CENTER)

#Colocando em loop
root.mainloop()
