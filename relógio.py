import time
import tkinter as tk
from tkinter import *
import os
from time import strftime
# O tkinter serve para criar interfaces gráficas
#O root é a base da interface do relógio
root = tk.Tk()
root.title('Relógio Digital')
root.geometry('600x320')
root.configure(background ='#1d1d1d')
root.minsize(600, 320)
root.maxsize(600, 320)
#As defs a seguir são funções que executam em ordem
def get_name():
    name_usuário = os.getlogin()
    name.config(text ='Oi ' + name_usuário)

def get_data():
    data_atual = strftime('%a, %d %b %Y')#strftime dá formato à data
    data.config(text = data_atual)

def get_time():
    time_atual = strftime('%H:%M:%S')#strftime dá formato ao horário
    time.config(text = time_atual)
    time.after(1000, get_time)
#TK.Canvas permite configurar o style da tela interativa  
#Essas variáveis editam cada elemento escrito anteriormente   
tela = tk.Canvas(root, width=600, height=60, background='#1d1d1d', bd=0, relief= 'ridge')
tela.pack()
name = Label(root, bg='#1d1d1d', fg='lightblue', font=('Montserrat', 20))
name.pack()
data = Label(root, bg='#1d1d1d', fg='lightblue', font=('Montserrat', 20))
data.pack(pady=2)
time = Label(root, bg='#1d1d1d', fg='lightblue', font=('Montserrat', 64))
time.pack(pady=10)

#Colocar essas nomenclaturas no final garante a execução das variáveis criadas dentro das defs
get_name()
get_data()
get_time()
root.mainloop()