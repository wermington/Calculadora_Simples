from tkinter import *
from tkinter import ttk
from turtle import width

cor1 = "#1e1f1e"  # Preta
cor2 = "#feffff"  # Branco
cor3 = "#38576b"  # Azul carregado
cor4 = "#ECEFF1"  # Cinzenta
cor5 = "#FFAB40"  # Laranja

janela = Tk()
janela.title('Calculadora')
janela.geometry("235x310")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

todos_valores = ''
# Criando a funcion

def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)


    # Criando a tela
    valor_label.set(todos_valores)

def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_label.set(str(resultado))


def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_label.set('')


# Criando Label
valor_label = StringVar()
app_label = Label(frame_tela, textvariable=valor_label, width=16, height=2, padx=7, relief=FLAT, anchor='e',
                  justify=RIGHT, font=('Ivy', 18), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

# Criando botoes

b_0_0 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_0_0.place(x=0, y=0)
b_0_1 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4,
               font=('Ivy', 13, 'bold'), relief='raised', overrelief='ridge')
b_0_1.place(x=118, y=0)
b_0_2 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_0_2.place(x=177, y=0)

b_1_0 = Button(frame_corpo, command=lambda: entrar_valores('7'),text="7", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_1_0.place(x=0, y=52)
b_1_1 = Button(frame_corpo, command=lambda: entrar_valores('8'),text="8", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_1_1.place(x=59, y=52)
b_1_2 = Button(frame_corpo, command=lambda: entrar_valores('9'),text="9", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_1_2.place(x=118, y=52)
b_1_3 = Button(frame_corpo, command=lambda: entrar_valores('*'),text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_1_3.place(x=177, y=52)

b_2_0 = Button(frame_corpo, command=lambda: entrar_valores('4'),text="4", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_2_0.place(x=0, y=104)
b_2_1 = Button(frame_corpo, command=lambda: entrar_valores('5'),text="5", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_2_1.place(x=59, y=104)
b_2_2 = Button(frame_corpo, command=lambda: entrar_valores('6'),text="6", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_2_2.place(x=118, y=104)
b_2_3 = Button(frame_corpo, command=lambda: entrar_valores('-'),text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_2_3.place(x=177, y=104)

b_3_0 = Button(frame_corpo, command=lambda: entrar_valores('1'),text="1", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_3_0.place(x=0, y=156)
b_3_1 = Button(frame_corpo, command=lambda: entrar_valores('2'),text="2", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_3_1.place(x=59, y=156)
b_3_2 = Button(frame_corpo, command=lambda: entrar_valores('3'),text="3", width=5, height=2, bg=cor4, fg=cor1, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_3_2.place(x=118, y=156)
b_3_3 = Button(frame_corpo, command=lambda: entrar_valores('+'),text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_3_3.place(x=177, y=156)

b_0_0 = Button(frame_corpo, command=lambda: entrar_valores('0'),text="0", width=11, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_0_0.place(x=0, y=208)
b_0_1 = Button(frame_corpo, command=lambda: entrar_valores('.'),text=".", width=5, height=2, bg=cor4, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_0_1.place(x=118, y=208)
b_0_2 = Button(frame_corpo, command= calcular,text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy', 13, 'bold'), relief='raised',
               overrelief='ridge')
b_0_2.place(x=177, y=208)

janela.mainloop()
