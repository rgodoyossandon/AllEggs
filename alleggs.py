from msilib.schema import AdminExecuteSequence


gallina = 0
pato = 0 
codorniz = 0 
aveztrus  = 0

print("Favor ingresar usuario")
user = input("Usuario:")
clave = input("Clave:")
if (user == "admin" and clave == "admin"):
    print ("-----------------------------------------")
    print ("Bienvenidos al Sistema de Reparto AllEggs")
    print ("-----------------------------------------")