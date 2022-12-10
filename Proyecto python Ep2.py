# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:32:13 2022

@author: Incubadora
"""

from tkinter import * 
from tkinter import messagebox 
from tkinter import ttk 

"""Shir. 
No se si esta bien pero es algo, queria hacer la parte de añadir y descontar saldo pero primero necesitamos hacer la base de datos""" 

def guardarDatos(): 
    masterUser = "a" 
    masterPass = "b" 
    user = usuario.get() 
    pas = contra.get() 
    if (user == masterUser and pas == masterPass): 
        pagina1.destroy() 
        page2()
    else:
        messagebox.showinfo(message="Contraseña o usuario incorrectos", title="ERROR")
def guardarDatos1():
    pagina2.destroy()
    page3()
def page2():
    global pagina2
    pagina2 = Tk()
    pagina2.title("Cliente")
    pagina2.geometry("520x520")
    global dni
    dni = ttk.Entry()
    dni.place(x=270, y=270)
    global alias
    alias = ttk.Entry()
    alias.place(x=270, y=300)
    boton1 = ttk.Button(text="Valida", command=guardarDatos1) 
    boton1.place(x=270, y=330)
    lbltext1 = Label(text="Cliente:")
    lbltext1.place(x=270, y=248.58)
    lblusuario = Label(text="DNI:")
    lblusuario.place(x=240, y=270)
    global lblcontra
    lblcontra = Label(text="ALIAS:")
    lblcontra.place(x=230, y=300)
def page3():
    global pagina3 
    pagina3 = Tk() 
    pagina3.config(width=300, height=200) 
    pagina3.title("Botón en Tk") 
    boton1 = ttk.Button(text="cargar_saldo", command=page5) 
    boton1.place(x=10, y=40) 
    boton2 = ttk.Button(text="realizar_compra", command=page4) 
    boton2.place(x=10, y=70) 
def addCombo(precio, strUpdate): 
    global precioAPagar 
    precioAPagar = strUpdate.get() # toma el texto en el label que almacena el total precioAPagar = precioAPagar.split(": ") # lo separa en 2 mitades ["Precio", valor] (`valor` es el numero correspondiete al total q se debe pagar o "???" si aun no se define precioAPagar = precioAPagar[1] # toma el valor de la separacion anterior [0, 1] = ["Precio", valor] (1 es el valor del array en 2da posision 
# try: 
#     precioAPagar = int(precioAPagar) # intenta convertir el valor de `precioAPagar` a int except: 
#     precioAPagar = 0 # si no se puede pone el valor de `precioAPagar` a 0 
#     precioAPagar += precio # aumentas el total al precio a pagar 
#     strUpdate.set("Precio: {}".format(precioAPagar)) 
# pagina de compras 
def page4(): 
    pagina4 
    pagina3.destroy() 
    pagina4 = Tk() 
    pagina4.config(width=300, height=200)
    pagina4.title("Botón en Tk")
    precio = StringVar() # Variable q se utiliza para el cambio dinamico del texto del label `mtpagar` 
    precio.set("Precio: ???")
    mtpagar = ttk.Label(textvariable=precio) # Etiqueta q muestra el precio mtpagar.place(x=100, y=170) 
    TextMain = ttk.Label(text="REALIZAR COMPRA") # Etoqieta en la parte superior pa q luzca mas bonito :3 
    TextMain.place(x=50, y=10)
    boton3 = ttk.Button(text="combo1", command=lambda: addCombo(100, precio)) # lambda es una declaracion a una funcion privada, la use xq los button no permiten pasar parametros a su funcion command asi puedo pasarselos 
# lambda: addCombo(100, precio) 
# es igual q decir 
# def lambda(): 
# addCombo(100, precio) 
    boton3.place(x=10, y=80-50) 
    boton4 = ttk.Button(text="combo2",command=lambda: addCombo(200, precio)) 
    boton4.place(x=10, y=110-50) 
    boton5 = ttk.Button(text="combo4",command=lambda: addCombo(300, precio)) 
    boton5.place(x=10, y=140-50) 
    boton6 = ttk.Button(text="PAGAR") 
    boton6.place(x=10, y=170-50) 
def page5(): 
    pagina3.destroy() 
    page5 = Tk() 
    page5.config(width=300, height=200) 
    page5.title("Botón en Tk") 
    cargar = ttk.Entry() 
    cargar.place(x=10, y=50) 
    saldo = ttk.Entry() 
    saldo.place(x=10, y=110) 
    boton = ttk.Button(text="MONTO A CARGAR") 
    boton.place(x=10, y=20) 
    boton2 = ttk.Button(text="SALDO ACTUAL") 
    boton2.place(x=10, y=80) 
pagina1 = Tk() 
pagina1.title("Inicio de sesión") 
pagina1.geometry("540x540") 
usuario = ttk.Entry() 
usuario.place(x=270, y=270) 
contra = ttk.Entry() 
contra.place(x=270, y=300) 
boton = ttk.Button(text="Acceder", command=guardarDatos) 
boton.place(x=270, y=330) 
lbltext1 = Label(text="Iniciar sesión:")
lbltext1.place(x=270, y=248.58) 
lblusuario = Label(text="Usuario:") 
lblusuario.place(x=220, y=270) 
lblcontra = Label(text="Contraseña:") 
lblcontra.place(x=200, y=300) 
pagina1.mainloop()
