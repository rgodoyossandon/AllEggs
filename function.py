from getpass import getpass
from http import client
import os
import sys


def login():
    print('Bienvenidos al sistema de despacho AllEggs')
    print('Favor de ingresar sus credenciales para acceder.')
    user = input('Ingrese su usuario:')
    pas = getpass("Ingrese su clave:")
    if (user != "admin" or pas != "admin"):
        sys.exit("El usuario o la contraseña es incorrecta, favor de verificar sus credenciales")
    os.system('cls')
        
