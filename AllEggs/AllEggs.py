product={'gallina' : 0,
         'pato' : 0,
         'codorniz' : 0,
         'avestruz' : 0}
client={}
cont =0 
while(True):
    print("1. Asignacion")
    print("2. Creacion")
    print("3. Listar Huevos")
    print("4. Listar despacho")
    try:
        opc = int(input("Seleccionar opcion:"))
        if (opc == 1):
            while(True):
                print("1. Huevo Gallina")
                print("2. Creacion")
                print("3. Listar Huevos")
                print("4. Listar despacho")
                try:
                    opc1 = int(input("Seleccionar una opcion:")) 
                    if (opc1 == 1):
                        try:
                            gallina = int(input("Ingrese el valor del huevo (valor minimo $50 pesos):"))
                            if gallina < 50: print ('El valor del huevo es inferior a $50 pesos. Se dejara automaticamente el valor en $50.')                               
                            else:
                                product.update({'gallina':gallina})
                        except:
                            print("Volviendo al menu principal")
                    elif (opc1 == 5):
                        print ("Datos guardados")
                        break
                except:
                    print("Volviendo al menu principal")            
        elif (opc == 2):
            nombre = input("ingrese nombre:")
            rut = input("Ingrese el Rut")
            tipo = input("ingrese el tipo de huevo a comprar:")
            cont +=1
            client ['idkey'+str(cont)] = nombre, rut,tipo
            print (product)
        elif (opc == 3):
            print(product)
        elif (opc == 4):
            print (client)
        elif (opc == 5):
            print("Gracia, vuelva pronto")
            break
        else:
            print("Opcion ingresada no valida")
    except:
        print("Volviendo al menu principal")
