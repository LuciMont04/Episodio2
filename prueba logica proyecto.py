# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 10:12:28 2022

@author: Incubadora
"""

"""alumno =[["Juan", "Alumno1","96058311", 100.50, 0, 0, 0],
    ["Luciana", "Alumno2", "45723607", 0.25, 0, 0, 0],
    ["Fausto", "Fulbo", "46328270", 2.5, 0, 0, 0]]"""



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
            comprarCombo(combo)

 
    
            
compra(saldo)
cargaSaldo(saldo)
def cargarCombo2(combo):
    cantidad = int(input("Ingrese cantidad de combos: "))
    combo = combo + cantidad
    print("Tienes {} combos.".format(combo))
    comprarCombo(combo)
def cargarCombo3(combo):
    cantidad = int(input("Ingrese cantidad de combos: "))
    combo = combo + cantidad
    print("Tienes {} combos.".format(combo))
    comprarCombo(combo)
def cargarCombo(combo):
    cantidad = int(input("Ingrese cantidad de combos: "))
    combo = combo + cantidad
    print("Tienes {} combos.".format(combo))
    comprarCombo(combo)
        
def comprarCombo(combo):
    monto = input("\nIngrese monto: ")
    if(combo > monto):
        combo = combo - monto
        print("Te quedan {} combos".format(combo))
     
    elif(combo < monto):
        print("No tienes combos.\n¿ Deseas cargar combos?") 
        print("1. Si, cargar combos. \n2. No realizar compra.")
        opc = 0
        while opc != "1" and opc != "2" and opc != "3":
            print("Ingrese una opción.\n")
            opc = input()
            if (opc != "1" and opc != "2" and opc !="3"):
                print("Opción no válida, inténtalo otra vez.\n.\n")
                break
        if(opc == "1"):
            cargarCombo(combo)
        else:
            comprarCombo(combo)

combo = 0
print("Ingrese una opcion: \nCombo 1. \nCombo 2. \nCombo 3. \nRealizar compra.")
opc=0
while opc != "1" and opc != "2" and opc != "3" and opc != "4":
    print("Ingrese una opción.\n")
    opc = input()
    if (opc != "1" and opc != "2" and opc !="3" and opc !="4"):
        print("Opción no válida, inténtalo otra vez.\n.\n")
        
    if(opc == "1"):
        cargarCombo(combo)
        if(opc =="2"):
            cargarCombo2(combo)
        else:
            cargarCombo3(combo)
    elif(opc == "4"):
        comprarCombo(combo)
    break


    
cargarCombo(combo)
comprarCombo(combo)
cargarCombo2(combo)
cargarCombo3(combo)

