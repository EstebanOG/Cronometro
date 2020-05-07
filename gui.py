from tkinter import *
from cronometro import cronometro
import time
from threading import Thread

class Interfaz:
    stop = False
    def __init__(self,root):
        root.title("Cronómetro")
        root.resizable(0,0)
        ventana = Frame(root)
        ventana.pack()

        texto = "0:0:0:0"
        label = Label(ventana, text= texto)
        label.config(font=("Verdana",20))
        label.grid(row=0, column=0,padx=100,pady=100)
                
        crm = cronometro()

        def button():
            Thread(target=codigo_inicia).start()

        def codigo_inicia():
            self.stop = False
            while self.stop != True:
                print(crm.start())
                label.config(text=crm.start())
                root.update_idletasks ()

            
        def codigo_pausa():
            self.stop = crm.pause(self.stop)
        
        def codigo_reiniciar():
            self.stop=True
            crm.restart()
            label.config(text="0:0:0:0")
            root.update_idletasks ()

        boton_inicia = Button(ventana, text = "Iniciar", command=button)
        boton_inicia.place(x=10, y=160)
        boton_inicia.config(font=("Verdana",12))

        boton_pausa = Button(ventana, text = "Pausar", command=codigo_pausa)
        boton_pausa.place(x=110, y=160)
        boton_pausa.config(font=("Verdana",12))

        boton_reinicia = Button(ventana, text = "Reiniciar", command=codigo_reiniciar)
        boton_reinicia.place(x=210, y=160)
        boton_reinicia.config(font=("Verdana",12))

