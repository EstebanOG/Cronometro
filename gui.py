from tkinter import *

root= Tk()
root.title("Cronómetro")
root.resizable(0,0)
ventana = Frame(root)
ventana.pack()

label = Label(ventana, text="00:00:00,00")
label.config(font=("Verdana",40))
label.grid(row=0, column=0,padx=100,pady=100)

def codigo_inicia():
    boton_inicia.grid_forget()
    boton_pausa.grid(row=1,column=0,padx=100,pady=100)
def codigo_pausa():
    boton_pausa.grid_forget()
    boton_reinicia.grid(row=1,column=0,padx=100,pady=100)
def codigo_reiniciar():
    boton_reinicia.grid_forget()
    boton_inicia.grid(row=1,column=0,padx=100,pady=100)

boton_inicia = Button(ventana, text = "Iniciar", command=codigo_inicia)
boton_inicia.config(font=("Verdana",20))
boton_inicia.grid(row=1,column=0,padx=100,pady=100)

boton_pausa = Button(ventana, text = "Pausar", command=codigo_pausa)
boton_pausa.config(font=("Verdana",20))

boton_reinicia = Button(ventana, text = "Reiniciar", command=codigo_reiniciar)
boton_reinicia.config(font=("Verdana",20))

root.mainloop()
