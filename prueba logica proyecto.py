# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 10:12:28 2022

@author: Incubadora
"""

"""alumno =[["Juan", "Alumno1","96058311", 100.50, 0, 0, 0],
    ["Luciana", "Alumno2", "45723607", 0.25, 0, 0, 0],
    ["Fausto", "Fulbo", "46328270", 2.5, 0, 0, 0]]"""


# def ():
#     user1 = input()
#     pass1 =
saldo = 40.5
def cargaSaldo(saldo):
    monto = float(input("Ingrese monto de carga: "))
    saldo = saldo + monto
    print("Tu saldo es de ${}".format(saldo))
    compra(saldo)
    
def compra(saldo):
    monto = float(input("\nIngrese monto: "))
    if(saldo > monto):
        saldo = saldo - monto
        print("Te quedan ${}".format(saldo))
     
    elif(saldo < monto):
        print("Tu saldo no es suficiente.\n¿ Deseas cargar saldo?") 
        print("1. Si, cargar saldo. \n2. No realizar compra.")
        opc = 0
        while opc != "1" and opc != "2":
            print("Ingrese una opción.\n")
            opc = input()
            if (opc != "1" and opc != "2"):
                print("Opción no válida, inténtalo otra vez.\n.\n")
                break
        if(opc == "1"):
            cargaSaldo(saldo)
        else:
            compra(saldo)
 
    
            
compra(saldo)
cargaSaldo(saldo)