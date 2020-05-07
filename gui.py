from tkinter import *
import cronometro as crm
import time

root= Tk()
root.title("Cronómetro")
root.resizable(0,0)
ventana = Frame(root)
ventana.pack()

texto = "00:00:00:00"
label = Label(ventana, text=texto)
label.config(font=("Verdana",20))
label.grid(row=0, column=0,padx=100,pady=100)

stop=None

def codigo_inicia():
    """boton_inicia.grid_forget()
    boton_pausa.grid(row=1,column=0,padx=100,pady=100)"""
    iniciarConteo()

def codigo_pausa():
    stop = crm.cronometro.pause(stop)
    """boton_pausa.grid_forget()
    boton_reinicia.grid(row=1,column=0,padx=100,pady=100)"""

def codigo_reiniciar():
    stop = True
    crm.cronometro.restart()
    label = Label(ventana, text= "00:00:00:00")
    label.config(font=("Verdana",20))
    label.grid(row=0, column=0,padx=100,pady=100)
    """boton_reinicia.grid_forget()
    boton_inicia.grid(row=1,column=0,padx=100,pady=100)"""


def iniciarConteo():
    stop = False
    cont =0
    while cont<=100: #Recordar modificar conteo
        time.sleep(0.1)
        label = Label(ventana, text=crm.cronometro.start())
        label.config(font=("Verdana",20))
        label.grid(row=0, column=0,padx=100,pady=100)
        cont=+1

boton_inicia = Button(ventana, text = "Iniciar", command=codigo_inicia)
boton_inicia.place(x=00, y=160)
boton_inicia.config(font=("Verdana",20))
#boton_inicia.grid(row=1,column=0,padx=100,pady=100)

boton_pausa = Button(ventana, text = "Pausar", command=codigo_pausa)
boton_pausa.place(x=120, y=160)
boton_pausa.config(font=("Verdana",20))
#boton_inicia.grid(row=4,column=4,padx=100,pady=100)

boton_reinicia = Button(ventana, text = "Reiniciar", command=codigo_reiniciar)
boton_reinicia.place(x=240, y=160)
boton_reinicia.config(font=("Verdana",20))
#boton_inicia.grid(row=8,column=8,padx=100,pady=100)

root.mainloop()
