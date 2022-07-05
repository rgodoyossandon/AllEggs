from getpass import getpass
from http import client
import os
from os import system
import sys


product={'gallina' : 0,
         'pato' : 0,
         'codorniz' : 0,
         'avestruz' : 0}


cont =0 




def login():
    
    while(True):
        print('Bienvenidos al sistema de despacho AllEggs')
        print('Favor de ingresar sus credenciales para acceder.')
        user = input('Ingrese su usuario: ')
        pas = getpass("Ingrese su clave: ")
        if (user != "admin" or pas != "admin"):
            print("El usuario o la contraseña es incorrecta, favor de verificar sus credenciales")
        else:
            print("Credenciales correctas")
            input("Presione alguna tecla para continuar . . .")
            system("cls")
            break
        
def menu():
    system('cls')
    print("1. Asignacion")
    print("2. Creacion")                                                
    print("3. Listar Huevos")
    print("4. Listar despacho") 
    print("5. Salir del programa")
    
   
def eggs():
    system("cls")
    print("1. huevo gallina")
    print("2. huevo pato")
    print("3. huevo codorniz")
    print("4. huevo avestruz")
    print("5. volver al menu")
    
def listeggs():
    print("El valor del Huevo de Gallina es de: ",  product["gallina"])
    print("El valor del Huevo de Pato es de: ",     product["pato"])
    print("El valor del Huevo de Avestruz es de: ", product["avestruz"])
    print("El valor del Huevo de Codorniz es de: ", product["codorniz"])
    input("Presione cualquier tecla para continuar")
    system("cls")
 