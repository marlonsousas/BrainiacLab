import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import (
FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import random
import math
import numpy as np
from tkinter import Tk
from tkinter import *


__author__ = "Francisco Marlon"
__version__ = 1.0


class Main:

    def __init__(self):
        pass





    def window(self):

        def calculator():
            class Calc():
                def __init__(self):
                    self.total = 0
                    self.current = ""
                    self.new_num = True
                    self.op_pending = False
                    self.op = ""
                    self.eq = False

                def num_press(self, num):
                    self.eq = False
                    temp = text_box.get()
                    temp2 = str(num)
                    if self.new_num:
                        self.current = temp2
                        self.new_num = False
                    else:
                        if temp2 == '.':
                            if temp2 in temp:
                                return
                        self.current = temp + temp2
                    self.display(self.current)


                def calc_total(self):
                    self.eq = True
                    self.current = float(self.current)
                    if self.op_pending == True:
                        self.do_sum()
                    else:
                        self.total = float(text_box.get())

                def display(self, value):
                    text_box.delete(0, END)
                    text_box.insert(0, value)

                def do_sum(self):
                    if self.op == "add":
                        self.total += self.current
                    if self.op == "minus":
                        self.total -= self.current
                    if self.op == "times":
                        self.total *= self.current
                    if self.op == "divide":
                        self.total /= self.current
                    if self.op == "raise":
                        self.total = self.total ** self.current
                    if self.op == "rootof":
                        self.total = self.total ** (1/self.current)
                    if self.op == "fact":
                        self.total=int(text_box.get())
                        self.total=math.factorial(self.total)
                    if self.op == "ln":
                        self.total = log(self.total)
                    if self.op == "log":
                        self.total=log(self.total,10)
                    if self.op == "sine":
                        self.total=math.sin(self.total)
                    if self.op == "cosine":
                        self.total = math.cos(self.total)
                    if self.op == "tangent":
                        self.total = math.tan(self.total)
                    if self.op == "exp":
                        self.total = math.exp(self.total)
                    if self.op == "inv":
                        self.total = 1/self.total
                    self.new_num = True
                    self.op_pending = False
                    self.display(self.total)

                def operation(self, op):
                    self.current = float(self.current)
                    if self.op_pending:
                        self.do_sum()
                    elif not self.eq:
                        self.total = self.current
                    self.new_num = True
                    self.op_pending = True
                    self.op = op
                    self.eq = False

                def clear(self):
                    self.eq = False
                    self.current = "0"
                    self.display(0)
                    self.new_num = True

                def all_clear(self):
                    self.clear()
                    self.total = 0

                def sign(self):
                    self.eq = False
                    self.current = -(float(text_box.get()))
                    self.display(self.current)

            sum1 = Calc()
            root = Tk()
            root['bg'] = "#222f3e"
            root.resizable(False, False)
            calc = Frame(root, background="#222f3e")
            calc.grid()

            root.title("Calculadora")
            text_box = Entry(calc, justify=RIGHT,width=30,font="Helvetica")
            text_box.grid(row = 0, column = 0,columnspan = 8,padx=30, pady = 30)
            text_box.insert(0, "0")


            numbers = "789456123"
            i = 0
            bttn = []
            for j in range(1,4):
                for k in range(3):
                    bttn.append(Button(calc,height =2,width=4,padx=10, pady = 10, text = numbers[i]))
                    bttn[i]["bg"]= "#2f3640"
                    bttn[i]['fg'] = "white"
                    bttn[i].grid(row = j, column = k,padx=1,pady=1)
                    bttn[i]["command"] = lambda x = numbers[i]: sum1.num_press(x)
                    i += 1

            bttn_0 = Button(calc,height =2,width=4,padx=10, pady = 10, text = "0",bg="#2f3640", fg="white")
            bttn_0["command"] = lambda: sum1.num_press(0)
            bttn_0.grid(row = 4, column = 0,  padx=1, pady = 1)

            div = Button(calc,height =2,width=4,padx=10, pady = 10, text = "/",bg="#10ac84", fg="white")
            div["command"] = lambda: sum1.operation("divide")
            div.grid(row = 1, column = 3, padx=1, pady = 1)

            mult = Button(calc,height =2,width=4,padx=10, pady = 10, text = "*",bg="#10ac84", fg="white")
            mult["command"] = lambda: sum1.operation("times")
            mult.grid(row = 2, column = 3,  padx=1, pady = 1)

            minus = Button(calc,height =2,width=4,padx=10, pady = 10, text = "-",bg="#10ac84", fg="white")
            minus["command"] = lambda: sum1.operation("minus")
            minus.grid(row = 3, column = 3, padx=1, pady = 1)

            add = Button(calc,height =2,width=4,padx=10, pady = 10, text = "+",bg="#10ac84", fg="white")
            add["command"] = lambda: sum1.operation("add")
            add.grid(row = 4, column = 3,  padx=1, pady = 1)

            power = Button(calc, height=2,width=4,padx=10,pady=10,text="x^y",bg="#ee5253", fg="white")
            power["command"] = lambda: sum1.operation("raise")
            power.grid(row=2,column = 4,padx=1,pady=1)

            rootof = Button(calc, height=2, width=4, padx=10, pady=10, text="y-\/x", bg = "#ee5253", fg="white")
            rootof["command"] = lambda: sum1.operation("rootof")
            rootof.grid(row=2, column=5, padx=1, pady=1)

            fact = Button(calc, height=2, width=4, padx=10, pady=10, text="!",bg="#ee5253", fg="white")
            fact["command"] = lambda: sum1.operation("fact")
            fact.grid(row=3,column=4, padx=1, pady=1)

            loge = Button(calc, height=2, width=4, padx=10, pady=10, text="ln",bg="#ee5253", fg="white")
            loge["command"] = lambda: sum1.operation("ln")
            loge.grid(row=3, column=5, padx=1, pady=1)

            log10 = Button(calc, height=2, width=4, padx=10, pady=10, text="log",bg="#ee5253", fg="white")
            log10["command"]= lambda: sum1.operation("log")
            log10.grid(row=4, column=4, padx=1 , pady=1)

            sine = Button(calc, height=2,width=4, padx=10,pady=10, text = "sin" , bg= "#ee5253", fg="white")
            sine["command"]=lambda: sum1.operation("sine")
            sine.grid(row=5,column=0,padx=1,pady=1)

            cosine = Button(calc, height=2,width=4, padx=10,pady=10, text = "cos" , bg= "#ee5253", fg="white")
            cosine["command"]=lambda: sum1.operation("cosine")
            cosine.grid(row=5,column=1,padx=1,pady=1)

            tangent = Button(calc, height=2,width=4, padx=10,pady=10, text = "tan" , bg= "#ee5253", fg="white")
            tangent["command"]=lambda: sum1.operation("tangent")
            tangent.grid(row=5,column=2,padx=1,pady=1)

            exponent = Button(calc, height=2, width=4, padx=10, pady=10, text='e^x', bg="#ee5253", fg="white")
            exponent["command"]=lambda: sum1.operation("exp")
            exponent.grid(row=5,column=3,padx=1,pady=1)

            inv = Button(calc, height=2, width=4, padx=10, pady=10, text="1/x", bg="#ee5253", fg="white")
            inv["command"] = lambda: sum1.operation("inv")
            inv.grid(row=5,column=4,padx=1,pady=1)

            point = Button(calc,height =2,width=4,padx=10, pady = 10, text = ".",bg="#10ac84", fg="white")
            point["command"] = lambda: sum1.num_press(".")
            point.grid(row = 4, column = 1, padx=1, pady = 1)

            neg= Button(calc,height =2,width=4,padx=10, pady = 10, text = "+/-",bg="#10ac84", fg="white")
            neg["command"] = sum1.sign
            neg.grid(row = 4, column = 2,  padx=1, pady = 1)


            clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "C",bg="#ff9f43", fg="white")
            clear["command"] = sum1.clear
            clear.grid(row = 1, column = 4,  padx=1, pady = 1)

            all_clear = Button(calc,height =2,width=4,padx=10, pady = 10, text = "AC",bg="#ff9f43", fg="white")
            all_clear["command"] = sum1.all_clear
            all_clear.grid(row = 1, column = 5, padx=1, pady = 1)

            equals = Button(calc,height =6,width=4,padx=10, pady = 10, text = "=",bg="#05c46b", fg="white")
            equals["command"] = sum1.calc_total
            equals.grid(row = 4, column = 5,columnspan=1,rowspan=2,padx=1, pady = 1)

            root.mainloop()
        def gerar2d():
            x = np.array(range(-20, 20))

            y = eval(f'{entrada1.get()}')
            plt.plot(x, y)

            plt.show()


        def gerar3d():
            def f(x, y):
                return np.sin(np.sqrt(x ** 2 + y ** 2))

            x = np.linspace(-6, 6, 30)
            y = np.linspace(-6, 6, 30)

            X, Y = np.meshgrid(x, y)
            Z = f(X, Y)
            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.contour3D(X, Y, Z, 50, cmap='binary')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z');







        tema = "Escuro"

        def dark_white():
            if root['bg'] == "#222f3e":
                root['bg'] = "#f5f6fa"
                array1['bg'] = "#f5f6fa"
                array1['fg'] = "#222f3e"
                graficoLabel['bg'] = "#f5f6fa"
                gerar['bg'] = "#222f3e"
                gerar2['bg'] = "#222f3e"
                calculadora['bg'] = "#222f3e"
                gerar['fg'] = "#f5f6fa"
                gerar2['fg'] = "#f5f6fa"
                calculadora['fg'] = "#f5f6fa"
                button["bg"] = "#222f3e"
                button["fg"] = "#f5f6fa"
                about["bg"] = "#222f3e"
                about["fg"] = "#f5f6fa"
                dark_bt["bg"] = "#222f3e"
                dark_bt["fg"] = "#f5f6fa"
                dark_bt['text'] = "Dark"

            else:
                root['bg'] = "#222f3e"
                array1['bg'] = "#222f3e"
                array1['fg'] = "#f5f6fa"
                graficoLabel['bg'] = "#222f3e"
                gerar['bg'] = "#f5f6fa"
                gerar2['bg'] = "#f5f6fa"
                calculadora['bg'] = "#f5f6fa"
                gerar['fg'] = "#222f3e"
                gerar2['fg'] = "#222f3e"
                calculadora['fg'] = "#222f3e"
                button["bg"] = "#f5f6fa"
                button["fg"] = "#222f3e"
                about["bg"] = "#f5f6fa"
                about["fg"] = "#222f3e"
                dark_bt["bg"] = "#f5f6fa"
                dark_bt["fg"] = "#222f3e"
                dark_bt['text'] = "White"


        def about():
            about_root = Tk()
            about_root["bg"] = "#222f3e"
            about_root.geometry("400x600")
            about_root.resizable(False, False)
            about_root.title("Sobre")


            nome = Label(about_root, text="Desenvolvido por Marlon Sousa\nBrainiac Corp", bg="#222f3e", fg="#f5f6fa", font=("", 15)).place(x=22, y=30)
            ano = Label(about_root, text="São Paulo\n2020", bg="#222f3e", fg="#f5f6fa", font=("", 15)).place(x=140, y=530)


            about_root.mainloop()
        import os
        import sys
        root = Tk()
        root.geometry("630x580")
        root.title("BrainiacLab")
        root.resizable(False, False)
        root.call('wm', 'iconphoto', root._w, PhotoImage(file='archives/logo/favicon.png'))
        root["bg"] = "#222f3e"

        button = Button(master=root, text="Quit", command=exit, bd=0,bg="#f5f6fa", fg="#222f3e")

        button.place(x=10, y=10)



        array1 = Label(root, text="Função", bg="#222f3e", fg="white", font=("", 15))
        array1.place(x=93, y=97)


        entrada1 = Entry(root, width=35)
        entrada1.place(x=180, y=100)


        filename = PhotoImage(file = "archives/logo/logo_transparent.png")


        graficoLabel = Label(root, image=filename, bg="#222f3e", width=500, height=500)
        graficoLabel.place(x=50, y=230)

        gerar = Button(root, text="Gerar Gráfico 2D",bd=0, command=gerar2d, width=15, bg="#f5f6fa", fg="#222f3e")
        gerar.place(x=60, y=270)
        gerar2 = Button(root, text="Gerar Gráfico 3D",bd=0, command=gerar3d, width=15, bg="#f5f6fa", fg="#222f3e")
        gerar2.place(x=230, y=270)
        calculadora = Button(root, text="Calculadora",bd=0, command=calculator, width=15, bg="#f5f6fa", fg="#222f3e")
        calculadora.place(x=400, y=270)

        dark_bt = Button(root, text="White", command=dark_white, bd=0, width=6, bg="#f5f6fa", fg="#222f3e")
        dark_bt.place(x=10, y=540)

        about = Button(root, text="About", command=about, bd=0, width=6, bg="#f5f6fa", fg="#222f3e" )
        about.place(x=10, y=500)

        #creditos = Label(root, text="By: Francisco Marlon\n Brainiac Corp", bg="#222f3e", fg="white", font=("", 15)).place(x=190, y=370)

        root.mainloop()



Main().window()


