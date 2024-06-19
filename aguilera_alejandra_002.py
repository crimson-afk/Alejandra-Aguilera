def eliminar(id_e,listita):
for p in lista:
    if id_e==p[0]:
        cant=0
        acum=0
        prom=0
        listita.remove(p)
    print("Equipo eliminado correctamente...")

while (True):
    print ("")
    print (".-.-.-M E N U-.-.-.")
    print ("")
    print ("1.- Agregar equipo")
    print ("2.- Listar equipo")
    print ("3.- Actualizar nombre de equipo por id")
    print ("4.- Generar BBDD")
    print ("5.- Cargar BBDD")
    print ("6.- Estadísticas")
    print ("0.- Salir")
    print("")
    op=int(input("ingrese una opcion:"))

    if op==1:
        print("")
        print ("-.-.A G R E G A R  E Q U I P O-.-.-.-")
        print ("")

        id=int(input("ingrese id( NUMEROS ): "))
        nombre=input("ingrese nombre :")
        puntos=int(input("ingrese puntos:"))
        categoría=[id,nombre,puntos]
        lista append(categoria)
        print("")
        
    elif op==2:
        print("")
        print("-.-.-. L I S T A R  E Q U I P O .-.-.-")
        print("")
    for p in lista:
        print(f"id:{p[0]}nombre:{p[1]}puntos:{p[2]}")
        print(".-.-.-.")


    elif op==3:
        encontrado=false
        print("")
        print("-.-. A C T U A L I Z A R   N O M B R E  D E L  E Q U I P O  P O R  ID .-.- : ")
        print("")

    elif op==4:
        print(".-.G E N E R A N D O  B A S E  D E  D A T O S.-.")
        print("")
        with open("bbdd_categoria.csv','w',newline=")as bbdd_categoria:
            escritor_csv=csv.writer(bbdd_categoria)
            escritor_csv.writerow([id','nombre','puntos'])
            escritor_csv.writerows(lista)
                                   print("")
                                   print ("archivo generado correctamente")

   elif op==5:
       print("")
       print(".-. C A R G A N D O  B A S E  D E  D A T O S.-.")
       print("")
       lista.clear()
       cont=0
       with open ("bbdd_categoria.csv','r',newline=")as bbdd_categoria:
           lector_csv=csv.reader(bbdd_categoria)
           for fila in lector_csv:
               if cont==0
               cont+=1
               continue
            i=int(fila[0])
            n=(fila[1])
            p=int(fila[2])
            listita_chica=[i,n,p]
            lista.append(listita_chica)
            lista.pop(0)

    elif op==6
        acum=0
        print("")
        print(".-.E S T A D I S T I S C A S.-."
        print("")
          cant=len(lista)
          if cant>0:
          for p in lista:
          acum=acum+p[2]
          prom=acum/cant
          print("puntos:",cant)
          print("puntos:",acum)
          print("puntos:", prom)

    else:
        print("No hay puntajes agregados...")
        elif op==0:
            print("A D I O S !!!")
            break

        else:
            print("")
            print("ingresa una opcion valida ")
            print("")
         
