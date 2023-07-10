from re import X
import numpy as np
from os import system
system("cls")

#CICLOS FOR PARA CREAR MATRIZ
matrizAsi=np.empty((10,10),dtype=object);
asientos=0
for f in range(10):
  for c in range(10):
        asientos=asientos+1
        matrizAsi[f,c]=asientos
affiliates=[]
matrizAsi[f,c]=asientos
#FUNCION PARA CREAR MENU
def menu():
     print("""
    ***********VENTA DE ASIENTOS CONCIERTO MICHAEL JAM**********
    1. COMPRAR ASIENTO
    2. MOSTRAR ASIENTOS DISPONIBLES
    3. VER LISTADO DE COMPRADORES
    4. MOSTRAR GANANCIAS TOTALES
    5. SALIR DEL PROGRAMA
    """)
#FUNCION PARA CREAR LA VENTA DE ASIENTO
def comprarAsiento():
  while True:
    try:
      rutAsiento=input("Ingrese rut: ")
      if len(rutAsiento) == 7 or len(rutAsiento)==8:
       break
      else:
        print("RUT NO VALIDO\nNO USAR PUNTOS NI GUIÓN.")
    except:
      print("Error de excepcion")
  while True:
   try:
    print("----- TIPOS DE ASIENTOS DISPONIBLES -----")
    print(matrizAsi)
    print("INGRESE LA FILA DEL ASIENTO VENDIDO \nTIPOS DE ASIENTOS \nFILA 1 Y 2 PLATINUM $120.000  \nFILA 3, 4 Y 5 GOLD $80.000 \nFILA 6, 7, 8, 9, Y 10 SILVER $50.000")
    fila=int(input("Ingrese la fila de su asiento:"))
    columna=int(input("Ingrese la columna de su asiento:"))
    if fila not in matrizAsi:
       fila=matrizAsi[fila]
       print("ASIENTO NO DISPONIBLE.\n****************************\nVOLVIENDO AL MENU PRINCIPAL.")
       break
   #NO SUPE COMO HACER LA VERIFICACION DE QUE SI ESTA VENDIDO O NO AUTOMATICAMENTE
    matrizAsi[fila-1,columna-1]='X'
    print(matrizAsi)
    print("----- RESERVA COMPLETADA -----")
    if fila==1:
     fila=str('PLATINUM')
    elif fila==2:
     fila=str('PLATINUM')
    elif fila==3:
     fila=str('GOLD')
    elif fila==4:
     fila=str('GOLD')
    elif fila==5:
     fila=str('GOLD')
    elif fila==6:
     fila=str('SILVER')
    elif fila==7:
     fila=str('SILVER')
    elif fila==8:
     fila=str('SILVER')
    elif fila==9:
     fila=str('SILVER')
    elif fila==10:
     fila=str('SILVER')
    affiliates.insert(0,fila)
    affiliates.insert(1,columna)
    affiliates.insert(2,rutAsiento)
    break
   except:
    print("Error de excepcion")
#FUNCION PARA MOSTRAR LOS ASIENTOS DISPONIBLES Y LOS QUE NO ESTAN MARCADOS CON X
def dispAsiento():
 print("----- ASIENTOS DISPONIBLES PARA RESERVAS -----")
 print("----- ASIENTOS MARCADOS CON UNA X NO ESTAN DISPONIBLES -----")
 print(matrizAsi)

#FUNCION PARA MOSTRAR A LOS AFILIADOS REGISTRADOS A LAS VENTAS
def listCompradores():
 print("----- AFILIADOS REGISTRADOS EN EL SISTEMA DE VENTAS -----")
 print(affiliates)

#FUNCION PARA SUMAR LAS GANANCIAS TOTALES
def sumagananciasTotales():
 cantAsp=0
 cantAsg=0
 cantAsi=0
 while True:
   try:
    print("PARA USAR ESTE MENU DE CÁLCULO SE DEBE DE INGRESAR PRIMERO LA FILA DEL ASIENTO.\n UNA VEZ INGRESADO LA FILA DEL ASIENTO INGRESAR LA CANTIDAD DE VENTAS ASOCIADAS A ESE TIPO.")
    print(matrizAsi)
    tipo=int(input("INGRESE LA FILA DEL ASIENTO VENDIDO \nTIPOS DE ASIENTOS \n1.-FILA 1 Y 2 PLATINUM $120.000  \n2.-FILA 3, 4 Y 5 GOLD $80.000 \n3.-FILA 6, 7, 8, 9, Y 10 SILVER $50.000\n4.-GANANCIAS TOTALES \n5.-SALIR AL MENU PRINCIPAL"))
    if (tipo==5):
     break
    if (tipo==1):
     cantAsp=int(input("¿Cuantos asientos se han comprado de tipo PLATINUM ?"))
     print("\n¿Desea agregar más asientoss?")
    elif (tipo==2):
     cantAsg=int(input("¿Cuantos asientos se han comprado de tipo GOLD ?"))
     print("\n¿Desea agregar más asientos?")
    elif (tipo==3):
     cantAsi=int(input("¿Cuantos asientos se han comprado de tipo SILVER ?"))
     print("\n¿Desea agregar más asientos?")
    elif (tipo==4):
     asitipoP=cantAsp*120000
     asitipoG=cantAsg*80000
     asitipoS=cantAsi*50000
     gananciasTot=asitipoP+asitipoG+asitipoS
     cantAsitot=cantAsp+cantAsg+cantAsi
     print(f"Las ganancias totales en asientos tipo PLATINUM son: ${asitipoP} con {cantAsp} asientos vendidos.")
     print(f"Las ganancias totales en asientos tipo GOLD son: ${asitipoG} con {cantAsg} asientos vendidos.")
     print(f"Las ganancias totales en asientos tipo SILVER son: ${asitipoS} con {cantAsi} asientos vendidos.")
     print(f"Las ganancias totales de asientos son: ${gananciasTot} con {cantAsitot} asientos vendidos.")
     break
    else:
     print("Error en tipo de asiento [1-3] y la cantidad tiene que ser mayor a 0")
   except:
    print("Error de excepcion")
#LLAMADO DE MENU PRINCIPAL    
while True:
    menu()
    op=input("Ingrese opción a ingresar en el menú: ")
    match op:
        case "1":
            comprarAsiento()
        case "2":
            dispAsiento()
        case "3":
            listCompradores()
        case "4":
            sumagananciasTotales()
        case "5":
          print("Has salido del programa, hasta pronto...")
          print("CARLOS_SOTO_004_A 10/07/2023")
          break
input("Presione ENTER para continuar...")

#https://github.com/Qvverty72/hola1

