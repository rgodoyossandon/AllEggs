from operation import *


def menu(): 
     
   opc = int( input ("""                       _________________________________________
                      |Bienvenidos al Sistema de Reparto AllEggs| 
                      |_________________________________________| 
                      |1. Asignacion de precios de Huevo        | 
                      |2. Creacion de Despacho                  | 
                      |3. Listar Huevos                         | 
                      |4. Listar Despachos                      | 
                      |_________________________________________| 
                      
                      Elegir una opcion:"""))

   while opc!=5:
      if opc == 1:
         price()
         
 
 
  
  
