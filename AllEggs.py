from msilib.schema import AdminExecuteSequence
from multiprocessing.connection import Client
from function import *

client={}
cont =0 



login()

while(True):
    try:
        menu() 
        opc = int(input("Seleccionar opcion: "))
        if (opc == 1):
            os.system('cls')
            while(True):
                print("1. Huevo Gallina")
                print("2. Huevo Pato")
                print("3. Huevo Codorniz")
                print("4. Huevo Avestruz")
                print("5. Volver al menu")
                try:
                    opc1 = int(input("Seleccionar una opcion: ")) 
                    if (opc1 == 1):
                        try:
                            gallina = int(input("Ingrese el valor del huevo (valor minimo $50 pesos):"))
                            if gallina < 50: 
                                print ('El valor del huevo es inferior a $50 pesos. Se dejara automaticamente el valor en $50.')
                                gallina = 50                              
                            else:
                                product.update({'gallina':gallina})
                        except:
                            print("Volviendo al menu principal")
                    elif (opc1 == 2):
                        os.system('cls')
                        try:
                            pato = int(input("Ingrese el valor del huevo (valor minimo $150 pesos):"))
                            if pato < 150: 
                                print ('El valor del huevo es inferior a $150 pesos. Se dejara automaticamente el valor en $150.')
                                pato = 150                              
                            else:
                                product.update({'pato':pato})
                        except: 
                            print("Volviendo al menu principal")
                    elif (opc1 == 3):
                        os.system('cls')
                        try:
                            codorniz = int(input("Ingrese el valor del huevo (valor minimo $50 pesos):"))
                            if codorniz < 50: 
                               print ('El valor del huevo es inferior a $50 pesos. Se dejara automaticamente el valor en $50.')
                               codorniz = 50                              
                            else:
                                product.update({'codorniz':codorniz})
                        except:
                            print("Volviendo al menu principal")
                    elif (opc1 == 4):
                        os.system('cls')
                        try:
                            avestruz = int(input("Ingrese el valor del huevo (valor minimo $800 pesos):"))
                            if avestruz < 800: 
                                print ('El valor del huevo es inferior a $800 pesos. Se dejara automaticamente el valor en $800.')
                                avestruz = 800                              
                            else:
                                product.update({'avestruz':avestruz})
                        except:
                            print("Volviendo al menu principal")        
                    elif (opc1 == 5):
                        print ("Datos guardados")
                        os.system('cls')
                        break
                except:
                    print("Volviendo al menu principal")            
        elif (opc == 2):
            os.system('cls')
            cont +=1
            nombre = input("Ingresar Nombre o Razon Social: ")
            rut = input("Ingrese el Rut: ")
            tipo = input("Indique el tipo de huevo: Gallina, Pato, Codorniz o Avestruz: ")
            convenio = input("Idicar si cliente posee convenio: 1. Si 2. No: ")
            direccion =input("Ingrese direccion de envio: ")
            fecha = input('Indicar fecha de compromiso: ')
            cantidad = int(input("Ingrese la cantidad de huevos (venta minima 50 - venta maxima 10000): "))
            if (cantidad < 50 or cantidad > 10000):
                print("El valor ingresado no corresponde a los parametros solicitados. Se asigna 50 unidades de huevos al cliente.")
                cantidad = 50
            tipe = tipo.lower()
            conve = convenio.lower()    
            if(convenio.lower() == "si"):
                total = (int(product[tipo.lower()])*cantidad)*0.9
                client ['idkey'+str(cont)] = nombre, rut, tipo, convenio, direccion, fecha, cantidad, total
            else:
               total = (int(product[tipo.lower()])*int(cantidad))
               client ['idkey'+str(cont)] = nombre, rut, tipo, convenio, direccion, fecha, cantidad, total
            print ("Registor completado con exito")
            input("Favor presiene una tecla para continuar")
        elif (opc == 3):
            system('cls')
            listeggs()
        elif (opc == 4):
            print(client)
            input('Presione una tecla para continuar')
        elif (opc == 5):
            print("Gracia, vuelva pronto")
            break
        else:
            print("Opcion ingresada no valida")
    except:
        print("Volviendo al menu principal")