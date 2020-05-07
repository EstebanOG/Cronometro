from tkinter import *
from cronometro import cronometro
import time

class Interfaz:
    
    def __init__(self,root):
        root.title("Cronómetro")
        root.resizable(0,0)
        ventana = Frame(root)
        ventana.pack()

        texto = "00:00:00:00"
        label = Label(ventana, text= texto)
        label.config(font=("Verdana",20))
        label.grid(row=0, column=0,padx=100,pady=100)
        
        stop=None
        
        crm = cronometro()

        def codigo_inicia():
            stop = False
            while stop != True:
                print(crm.start())
                label.config(text=crm.start())
                root.update_idletasks ()
            
        def codigo_pausa():
            #stop = crm.cronometro.pause(stop)
            stop = crm.pause(stop)
        
        def codigo_reiniciar():
            stop = True
            #crm.cronometro.restart()
            label = Label(ventana, text= "00:00:00:00")
            label.config(font=("Verdana",20))
            label.grid(row=0, column=0,padx=100,pady=100)

        boton_inicia = Button(ventana, text = "Iniciar", command=codigo_inicia)
        boton_inicia.place(x=00, y=160)
        boton_inicia.config(font=("Verdana",20))

        boton_pausa = Button(ventana, text = "Pausar", command=codigo_pausa)
        boton_pausa.place(x=120, y=160)
        boton_pausa.config(font=("Verdana",20))

        boton_reinicia = Button(ventana, text = "Reiniciar", command=codigo_reiniciar)
        boton_reinicia.place(x=240, y=160)
        boton_reinicia.config(font=("Verdana",20))

